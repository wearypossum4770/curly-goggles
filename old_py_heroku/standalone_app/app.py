from flask import Flask
from flask_environment import Config

from whitenoise import WhiteNoise

class CreateFlaskApp(Flask):
	config_class = Config

def application():
	app = CreateFlaskApp(__name__)
	app.config.from_toml('config.toml')
	app.wsgi_app = WhiteNoise(app.wsgi_app, root='static/')

