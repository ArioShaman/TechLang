#!/usr/bin/env python
from app import app
#app.run(debug = True,threaded=True)
app.run(host='0.0.0.0', port=5000,debug = True,threaded=True)

from flask.ext.mail import Message
from app import app, mail