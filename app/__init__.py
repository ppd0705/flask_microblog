import os
from flask import Flask
from flask_msearch import Search
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir
from .momentjs import Momentjs


app = Flask(__name__)
lm = LoginManager()
search = Search()
app.config.from_object('config')
db = SQLAlchemy(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))
lm.init_app(app)
lm.login_view = 'login'
search.init_app(app)
mail = Mail(app)

app.jinja_env.globals['momentjs'] = Momentjs

from app import views, models

# if not app.debug:
#     import logging
#     from logging.handlers import RotatingFileHandler
#     file_handler = RotatingFileHandler('tmp/microblog.log', 'a', 1 * 1024 * 1024, 10)
#     file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
#     app.logger.setLevel(logging.INFO)
#     file_handler.setLevel(logging.INFO)
#     app.logger.addHandler(file_handler)
#     app.logger.info('microblog startup')