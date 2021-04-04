from flask import Flask
from flask_bootstrap import Boostrap

def create_app():
  app = Flask(__name__)
  Bootstrap(app)