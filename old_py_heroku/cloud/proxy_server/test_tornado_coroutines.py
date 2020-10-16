from tornado.gen import Return, multi,convert_yielded
from tornado.auth import GoogleOAuth2Mixin, FacebookGraphMixin,TwitterMixin
def app ():
	"""
	note: try not to use  tornado.wsgi.WSGIContainer use gunicorn or uwasgi
	
	"""     
@gen.coroutine
@gen.coroutine
def decorated_a():
	"""
	Decorated coroutines 
		1. can start running “in the background” as soon as they are called.
		2. Integrate with the concurrent.futures package, 
		3. Result of executor.submit to be yielded directly. 
		4. use "async" or "yield" all async funcs      
		5. always return a Future object.
		6. raise a special exception in PY2 "return" and "yield" cannot be mixed.  
	multi has quiet_exceptions: Union[Type[Exception], Tuple[Type[Exception], ...]] = ()
	"""                      
    b = yield c()   
    raise gen.Return(b)            
    
async def native_a():
	"""
	native coroutines
		1. use IOLoop.run_in_executor.
		2. are generally faster.
		3. can use async for and async with statements.
		4. do not run at all unless you await or yield them.
		5. return an awaitable object that is not a Future
	2. "async def" keywords  "await" all async funcs
	3. Return normally
	"""
	b = await c()

	return b
@convert_yielded.register(asyncio.Future)
def _(asyncio_future):
    return tornado.platform.asyncio.to_tornado_future(asyncio_future)
# ~ {
	# ~ "google_oauth": 
		# ~ {
			# ~ "key": CLIENT_ID, 
			# ~ "secret": CLIENT_SECRET
			# ~ }
	# ~ }   
	
	
# ~ results = yield multi(list_of_futures)
# ~ - equivalence -
# ~ results = []
# ~ for future in list_of_futures:
    # ~ results.append(yield future)
