#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from pro.database import db_session,init_db
from pro.models import User
init_db()

u = User('123123213')
u.nickname='loki'
db_session.add(u)
db_session.commit()