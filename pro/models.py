#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String,DateTime,ForeignKey

from pro.database import Base,db_session
from pro import database , db,app





class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	steam_id = Column(String(40))
	nickname = Column(String(80))
	def __init__(self,steam_id):
		self.steam_id = steam_id
	@staticmethod
	def get_or_create(steam_id):
		rv = User.query.filter_by(steam_id=steam_id).first()
		if rv is None:
			rv = User(steam_id)
			db_session.add(rv)
		return rv
	def __repr__(self):
		return '<User %s>'%self.id


