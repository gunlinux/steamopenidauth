#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, redirect, session, json, g,render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.openid import OpenID


app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)
oid = OpenID(app)

from pro import view

from pro.database import db_session

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

