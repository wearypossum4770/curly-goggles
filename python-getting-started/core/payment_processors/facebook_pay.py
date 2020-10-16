from os import getenv

redirect_uri="http://YOUR_URL?code=<AUTHORIZATION_CODE>"
base_url = f"https://graph.facebook.com/{getenv('API_VERSION')}/oauth/access_token?"
params = {
	"client_id":getenv('YOUR_APP_ID'),
	"redirect_uri":getenv('YOUR_URL')},
	"client_secret":getenv("YOUR_APP_SECRET"),
	"code":getenv('AUTHORIZATION_CODE'),
}
