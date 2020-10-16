import asyncio
from motor.motor_tornado import MotorClient
import tornado.ioloop
import tornado.web import RequestHandler, authenticated

# ~ def create_client():
	# ~ client = MotorClient('mongodb://localhost:27017')

	# ~ db = client['test_database']
	# ~ return db
	



# ~ SESSION_INFO = {}
# ~ RESPONSE_HEADER_INFO = {"PROXY_TOKEN":"aGVsbG86d29ybGQ=",}
# ~ class AsyncMongoDB(RequestHandler):
	# ~ def initialize(self, database_name):
		# ~ self.database_name = database_name
	
	# ~ def response_header():
		# ~ _header = dict([
			# ~ ["Set-Cookie", f"{SESSION_INFO.get('COOKIE_NAME')}={SESSION_INFO.get('COOKIE_VALUE')}"],
			# ~ ["Host","server.example.com:80"]
			# ~ ["Proxy-Authenticate", "Basic realm='Access to the internal site'"],
			# ~ ["Proxy-Authorization", f"basic {RESPONSE_HEADER_INFO.get('PROXY_TOKEN')}"],
			# ~ ])
		# ~ return _header
		
	# ~ def get(self):
		# ~ self.write("hello, world")

	# ~ def delete():
		# ~ pass
	# ~ def put():
		# ~ pass
	# ~ def patch():
		# ~ pass	
	# ~ def connect():
		# ~ """
		# ~ 1. Access websites that use SSL (HTTPS). 
		# ~ 2. The HTTP Proxy server tunnels the TCP connectionl
		# ~ 3. The server connects on behalf of the client.  
		# ~ 4. TCP stream to and from the client.
		# ~ For example:
			# ~ # todo 
		# ~ """
		# ~ CONNECT = "server.example.com:80 HTTP/1.1" 

	# ~ def head():
		# ~ pass
	# ~ def options():
		# ~ pass
	# ~ def trace():
		# ~ pass

		
# ~ class AsyncMongoDB:
	# ~ def __init__(self):
		# ~ pass
	# ~ def create_db():
		# ~ pass
	# ~ def create_table():
		# ~ collection = db['test_collection']
	# ~ def create_row():
		# ~ document = {}
		# ~ result = await db.test_collection.insert_one(document)
		# ~ print f"result {result.inserted_id}"
		
	# ~ def query_one_result():
		# ~ document = await db.test_collection.find_one({'i': {'$lt': 1}})	
	# ~ def query_multiple_records():
		# ~ cursor = db.test_collection.find({'i': {'$lt': 5}}).sort('i')
		# ~ for document in await cursor.to_list(length=100):
			# ~ pprint.pprint(document)
	# ~ async def for_each_record():
		# ~ c = db.test_collection
		# ~ async for document in db.test_collection.find({'i': {'$lt': 2}}):
			# ~ pprint.pprint(document)
	
	# ~ def server_spinup():
		# ~ application = tornado.web.Application([
		# ~ (r'/', MainHandler)
		# ~ ], db=db)

		# ~ application.listen(8888)
		# ~ tornado.ioloop.IOLoop.current().start()
class BaseHandler(tornado.web.RequestHandler):
	def get_current_user(self):
		return self.get_secure_cookie("user")

class MainHandler(BaseHandler):
	@authenticated
	def get(self):
		if not self.current_user:
			self.redirect("/login")
			return
		name = tornado.escape.xhtml_escape(self.current_user)
		self.write("Hello, " + name)

class LoginHandler(BaseHandler):
	def get(self):
		self.write('<html><body><form action="/login" method="post">'
		'Name: <input type="text" name="name">'
		'<input type="submit" value="Sign in">'
		'</form></body></html>')

	def post(self):
		self.set_secure_cookie("user", self.get_argument("name"))
		self.redirect("/")

application = tornado.web.Application([
	(r"/", MainHandler),
	(r"/login", LoginHandler),
	], cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__")


def run_server():
	app = make_app()
	server = tornado.httpserver.HTTPServer(app)
	server.bind(8888)
	server.start(0)  # forks one process per cpu
	IOLoop.current().start()

# ~ ulimit	
if __name__ == '__main__':
    run_server()
