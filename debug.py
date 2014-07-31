#!/usr/bin/env python
from pro import app
app.debug=True
app.secret_key = app.config['SECRET']
app.run(port=app.config['PORT'],host="127.0.0.1")
