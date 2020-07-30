from re import findall 


def install_memcache ():
	memcache_url = "http://www.memcached.org/files/memcached-1.6.6.tar.gz"
	memcached_regex = 'memcached\-(\d).(\d).(\d)\.tar.gz'
	major,minor,bug = findall(memcached_regex,memcache_url)[0]
	script = f" wget {memcache_url} && tar -zxvf memcached-{major}.{minor}.{bug}.tar.gz && cd memcached-{major}.{minor}.{bug} && ./configure && make -j6 && make test && sudo make install"
	return script
print(install_memcache())
#Debian/Ubuntu: apt-get install libevent-dev Redhat/Centos: yum install libevent-devel
