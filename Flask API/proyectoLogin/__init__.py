import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

gestor = LoginManager()
app = Flask(__name__)

app.config['SECRET_KEY'] = 'clavesecreta'

directorio = os.path.abspath(os.path.dirname(__file__))         # obtención del directorio de trabajo
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directorio,'loginbd.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

basededatos = SQLAlchemy(app)
Migrate(app,basededatos)            # conecta app con bd

gestor.init_app(app)
gestor.login_view = 'login'
