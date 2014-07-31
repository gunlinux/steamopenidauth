#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pro import app
from flask import render_template,url_for,redirect,request,session,flash,abort,jsonify,g
from pro.models  import User
import json
from functools import wraps
from flask import  Response
from pro import db
from pro.database import db_session
from sqlalchemy import or_
from pro import oid


import urllib2

def get_steam_userinfo(steam_id):
    url = 'http://api.steampowered.com/ISteamUser/' \
          'GetPlayerSummaries/v0001/?key=%s&steamids=%s'%(app.config['STEAM_API_KEY'],steam_id)
    rv = json.load(urllib2.urlopen(url))
    return rv['response']['players']['player'][0] or {}

import re

_steam_id_re = re.compile('steamcommunity.com/openid/id/(.*?)$')

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html',users=users)

@app.route('/login')
@oid.loginhandler
def login():
    if g.user is not None:
        return redirect(oid.get_next_url())
    return oid.try_login('http://steamcommunity.com/openid')

@oid.after_login
def create_or_login(resp):
    match = _steam_id_re.search(resp.identity_url)
    g.user = User.get_or_create(match.group(1))
    steamdata = get_steam_userinfo(g.user.steam_id)
    g.user.nickname = steamdata['personaname']
    db_session.commit()
    session['user_id'] = g.user.id
    flash('You are logged in as %s' % g.user.nickname)
    return redirect(oid.get_next_url())

@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(oid.get_next_url())


