from os import getenv
from pathlib import Path
from dotenv import laod_dotenv
from flask import Flask
from pusher import Pusher
BASE_DIR = Path("/home/gatorcollege2006/web_dev/apprenticeship/data")
env_path = BASE_DIR / ".env"
load_dotenv(dotenv_path=env_path)
# ~ from flask_environment import Config
# ~ class Application(Flask):
    # ~ config_class = Config
# ~ def create_app(test_config=None):
	# ~ app = Application(__name__, instance_relative_config=True)
	# ~ app.config.from_toml('config.toml', environment='develop')
def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=True)
	# ~ app.config.from_toml('config.toml', environment='develop')
	app.config.from_mapping(
	SECRET_KEY="dev",
	DATABASE= BASE_DIR / "flaskr.sqlite",
	# ~ CELERY_BROKER_URL='redis://localhost:6379',
	# ~ CELERY_RESULT_BACKEND='redis://localhost:6379'
	)

	if test_config is None:
		pusher_app = Pusher(
			app_id=getenv('PUSHER_APP_ID'),
			key=getenv('PUSHER_APP_KEY'),
			secret=getenv('PUSHER_APP_SECRET)',
			cluster=getenv('PUSHER_APP_CLUSTER)',
			ssl=True)
		app.config.from_pyfile("config.py", silent=True)
	else:
		# load the test config if passed in
		app.config.from_mapping(test_config)

		# ensure the instance folder exists
	try:
		Path.mkdir(app.instance_path)
	except OSError:
		pass

	# a simple page that says hello
	@app.route('/')
	def index():
	return render_template('index.html')

	@app.route('/dashboard')
	def dashboard():
	return render_template('dashboard.html')

	@app.route('/orders', methods=['POST'])
		def order():
		data = request.form
		pusher_app.trigger('order','place', {
		'units': data['units']
		})
	return "units logged"

	@app.route('/message', methods=['POST'])
	def message():
		data = request.form
		pusher_app.trigger('message', 'send', {
		'name': data['name'],
		'message': data['message']
		})
		return "message sent"

	@app.route('/customer', methods=['POST'])
	def customer():
		data = request.form
		pusher_app.trigger('customer', 'add', {
			'name': data['name'],
			'position': data['position'],
			'office': data['office'],
			'age': data['age'],
			'salary': data['salary'],
		})
		return "customer added"

	return app

if __name__ == '__main__':
	app.run(debug=getenv('FLASK_DEBUG')

