from re import findall
from os import popen
ssh_v = "OpenSSH_7.9p1 Debian-10+deb10u2, OpenSSL 1.1.1d  10 Sep 2019"
key_prompt = {
	1:
		{
		"algorithm": "ED25519 (preferred)",
		"public_key":"id_ed25519.pub",
		"private_key":"id_ed25519",
		"GitLab_md5": "2e:65:6a:c8:cf:bf:b2:8b:9a:bd:6d:9f:11:5c:12:16",
		"GitLab_SHA256":"eUXGGm1YGsMAS7vkcx6JOJdOGHPem5gQp4taiCfCLB8",
		},
	2:
		{
		"algorithm": "RSA (at least 2048-bit key size)",
		"public_key":"id_rsa.pub",
		"private_key":"id_rsa",
		"GitLab_md5": "b6:03:0e:39:97:9e:d0:e7:24:ce:a3:77:3e:01:42:09",
		"GitLab_SHA256":"ROQFvPThGrW4RuW",
		},
	3:
		{
		"algorithm": "DSA (deprecated)",
		"public_key":"id_dsa.pub",
		"private_key":"id_dsa",		
		"GitLab_md5": "7a:47:81:3a:ee:89:89:64:33:ca:44:52:3d:30:d4:87",
		"GitLab_SHA256":"p8vZBUOR0XQz6sYiaWSMLmh0t9i8srqYKool/Xfdfqw",
		},
	4:
		{
		"algorithm": "ECDSA",
		"public_key":"id_ecdsa.pub",
		"private_key":"id_ecdsa",
		"GitLab_md5": "f1:d0:fb:46:73:7a:70:92:5a:ab:5d:ef:43:e2:1c:35",
		"GitLab_SHA256":"HbW3g8zUjNSksFbqTiUWPWg2Bq1x8xdGUrliXFzSnUw",
		},
}


class GitLabGPG:
	"""
	OPEN PGG Best Practices 
	https://riseup.net/en/security/message-security/openpgp/best-practices 
	"""
	def __init__(self):
		self.repo = "https://gitlab.com/wearypossum4770/new_v2_backend/-/commits/master"
		self.ssh_ssl_info = findall('(openssh)(\d+[.]{1,}\d+)(\w+)\s+(.*)\,\s+(openssl)\s+(.*)\s+([0-9]{2}\s+\w+\s+[0-9]{4})',ssh.lower().replace('_',''))
		self.email_address = prompt("What's your email address?:")
	
	def create_gpg():
		"""
		Creates GPG Key
		"""
		gpg --full-gen-key
		first_prompt = "Please select what kind of key you want:\n(1) RSA and RSA (default)\n(2) DSA and Elgamal\n(3) DSA (sign only)\n(4) RSA (sign only)\nYour selection? 1"
		second_prompt = "RSA keys may be between 1024 and 4096 bits long.\nWhat keysize do you want? (2048) 4096\nRequested keysize is 4096 bits\n"
		third_prompt ="Please specify how long the key should be valid.\n0 = key does not expire\n<n>  = key expires in n days\n<n>w = key expires in n weeks\n<n>m = key expires in n months\n<n>y = key expires in n years\nKey is valid for? (0) 0\nKey does not expire at all\n"
		fourth_prompt="Is this correct? (y/N)"
		fifth_prompt="GnuPG needs to construct a user ID to identify your key.\nReal name: Mr. Robot\nEmail address: <your_email>\nComment:\nYou selected this USER-ID:\n\t\t'Mr. Robot <your_email>'\nChange (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? O\n"
			
	def read_gpg():
		to_shell=f"gpg --list-secret-keys --keyid-format LONG {self.email_address}"
		first_read_prompt = "sec   rsa4096/30F2B65B9246B6CA 2017-08-18 [SC]\nD5E4F29F3275DC0CDA8FFC8730F2B65B9246B6CA\nuid\t\t\t\t\t\t[ultimate] Mr. Robot <your_email>\nssb   rsa4096/B7ABC0813E4028C0 2017-08-18 [E]\n"
		self.fingerprint = findall('sec\s+\w+\/(\w+)',first_read_prompt)[0]
		to_shell=f"gpg --list-secret-keys --keyid-format LONG <your_email>"
		copy_gpg_public_key = f"gpg --armor --export  {self.fingerprint}"
		git_config_global=f"git config --global user.signingkey {self.fingerprint}"
		self.auto_sign_commit = prompt('Would you like to sign every commit?')
		git_config_auto_commit = "git config --global commit.gpgsign true" if self.auto_sign_commit else None
			
	def upload_gpg(self):
		"""
		Uploads GPG key to Gitlab
		"""
		
	def verify_gitlab_gpg():
		"""
		Checks to ensure gpg key is in gitlab settings
		"""
		regex="<code>(\w+)</code>|(key-created-at).*\s+.*datetime\W+([0-9]{4}-[0-9]{2}-\w+:\w+:\w+)"
		to_shell='git commit -S -m "My commit msg"'
		gpg_status_box_regex = '(gpg-status-box)\s+(.*)\"\s+'
		gpg_status_box,status,gpg_key_id,key_id = findall(gpg_status_box_regex)
	def CRUD_repo():
		"""
		Create a new repo and performs CRUD using GPG Key
		"""
		
class GitLabSSH:
	"""
	OPEN PGG Best Practices 
	https://riseup.net/en/security/message-security/openpgp/best-practices 
	"""
	def __init__(self):
		self.ssh_ssl_info = findall('(openssh)(\d+[.]{1,}\d+)(\w+)\s+(.*)\,\s+(openssl)\s+(.*)\s+([0-9]{2}\s+\w+\s+[0-9]{4})',ssh_v.lower().replace('_',''))
		self.key_prompt = prompt ('')
		self.key_type = "id_ed25519"
		self.add_known_host = "gitlab.com ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAfuCHKVTjquxvt6CM6tdG4SLp1Btn/nOeHHE5UOzRdf && gitlab.com ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCsj2bNKTBSpIYDEGk9KxsGh3mySTRgMtXL583qmBpzeQ+jqCMRgBqB98u3z++J1sKlXHWfM9dyhSevkMwSbhoR8XIq/U0tCNyokEi/ueaBMCvbcTHhO7FcwzY92WK4Yt0aGROY5qX2UKSeOvuP4D6TPqKF1onrSzH9bx9XUf2lEdWT/ia1NEKjunUqu1xOB/StKDHMoX4/OKyIzuS0q/T1zOATthvasJFoPrAjkohTyaDUz2LN5JoH839hViyEG82yB+MjcFV5MU3N1l1QL3cVUCh93xSaua1N85qivl+siMkPGbO5xR/En4iEY6K2XPASUEMaieWVNTRCtJ4S8H+9 && gitlab.com ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBFSMqzJeV9rUzU4kWitGjeR4PWSa29SPqJ1fVkhtj3Hw9xjLVXVYrU9QlYWrOLXBpQ6KWjbjTDTdDkoohFzgbEY="
		
	def update_rsa_encryption():
		to_shell = "ssh-keygen -o -f ~/.ssh/id_rsa"
	def create_ssh_passwd():
		password = prompt("Enter passphrase (empty for no passphrase):")
		confirm_password = prompt("Enter same passphrase again:")
	
	def update_ssh_passwd():
		self.create_ssh_passwd()
		old_password = "Enter old passphrase:"
		f "ssh-keygen -p -f $HOME/.ssh/"
		old_password = "Enter old passphrase:"
	
	def ssh_version():
		"""
		Check version of SSH
		"""
	def create_ssh():
		"""
		Creates ssh certificate for gitlab
		"""
		Generating public/private ed25519 key pair.
		filename = prompt("Enter file in which to save the key (/home/user/.ssh/id_ed25519):")
		password = prompt("Enter passphrase (empty for no passphrase):")
		confirm_password = prompt("Enter same passphrase again:")
	
		to_shell = 'ssh-keygen -t ed25519 -C "<comment>"'
	def upload_gpg(self):
		"""
		Uploads GPG key to Gitlab
		"""
		
"/html/body/div/div[2]/div[3]/div/div[2]/div[2]/div[1]/form/div[1]/textarea"				
# ~ def gitlab_ssh():
	# ~ regex = "(title)\W+href\W+(.*)\"\>(.*)\s+.*\s+(.*)\s+"
	# ~ ssh_regex = "(title)\W+href\W+(.*)\"\>(.*)\s+.*\s+(.*)\s+.*\s+.*\s+.*(last-used-at)\s+.*\s+\w+\s+\w+\W+.*(datetime)\=\"([0-9]{4}[-]{1}[0-9]{2}[-]{1}\w+:\w+:\w+).*(\d+\s+\w+\s+\w+).*\s+.*\s+.*(expires)\s+.*\s+\w+:\s+(\w+)\s+.*\s+.*(key-created-at).*\s+.*(datetime)\=\"([0-9]{4}[-]{1}[0-9]{2}[-]{1}\w+:\w+:\w+)"
	# ~ ssh_data = findall(ssh_regex, document)
	# ~ ssh_meta_data = []
	# ~ for _meta_data in ssh_data:
		# ~ ssh_meta_data.append( {
			# ~ "href":_meta_data[1],
			# ~ "name":_meta_data[2],
			# ~ "fingerprint":_meta_data[3],
			# ~ _meta_data[4]:_meta_data[6],
			# ~ "last_used_test":_meta_data[7],
			# ~ _meta_data[8]:_meta_data[9],
			# ~ "date_created":_meta_data[12],
			# ~ })
	# ~ return ssh_meta_data[0]
# ~ print(gitlab_ssh())
