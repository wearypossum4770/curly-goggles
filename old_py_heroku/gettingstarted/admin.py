import requests
from requests.auth import HTTPBasicAuth

from bs4 import BeautifulSoup
username="wearypossum4770"
gitlab_password="K2DNQyfx9SRLU!b"
github_password="!GN0r@mus234!@#"

auth=HTTPBasicAuth(username, gitlab_password )

url = "https://gitlab.com/"
page = requests.get(url)
# ~ soup = BeautifulSoup(page.content, 'html.parser')
# ~ gpg_target = soup.find(id='gpg_key_key')
# ~ print(gpg_target.prettify())
curl= '<html><body>You are being <a href="https://gitlab.com/users/sign_in">redirected</a>.</body></html>'

def navigate_to_git_lab():
	page = requests.get(url)
	filename='gitlab_home.html'
	with open(filename, 'wb') as fd:
		for chunk in page.iter_content(chunk_size=128):
			fd.write(chunk)
	return page.raw
def navigate_to_sign_in():
	url = 'https://gitlab.com/users/sign_in'
	page = requests.get(url)
	filename='gitlab_signin.html'
	with open(filename, 'wb') as fd:
		for chunk in page.iter_content(chunk_size=128):
			fd.write(chunk)
			
	return page.status_code
print(navigate_to_sign_in())
