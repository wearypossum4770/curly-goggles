from hashlib import sha1
from pathlib import Path
import pytest

import gpg_setup
mock_gpg_page = Path.cwd() / "gitlab_com_profile_gpg_keys.txt"
mock_ssh_page = Path.cwd() / "gitlab_com_profile_keys.txt"
json_filename = Path.cwd() / "init_gpg_data.json"
html_filename = Path.cwd() / "gitlab_com_profile_keys.txt"

ssh_start = 'ssh-keygen -t ed25519 -C "<comment>"'
frist = f"Generating public/private ed25519 key pair.\nEnter file in which to save the key (/home/user/.ssh/id_ed25519):"

GITLAB_ENV = dict()

def test_command_args():
	from os import popen
	to_shell='ls -a'
	test_input = popen(to_shell).read()

	expected = '.\n..\ngitlab_com_profile_gpg_keys.txt\ngitlab_com_profile_keys.txt\ngpg_setup.py\ninit_gpg_data.json\ntest_gpg_setup.py\n'
	assert test_input == expected

# ~ class TestGPGSetup:

	# ~ def setUp(self):
		
		# ~ self.gpg_regex = "(title)\W+href\W+(.*)\"\>(.*)\s+.*\s+(.*)\s+.*\s+.*\s+.*(last-used-at)\s+.*\s+\w+\s+\w+\W+.*(datetime)\=\"([0-9]{4}[-]{1}[0-9]{2}[-]{1}\w+:\w+:\w+).*(\d+\s+\w+\s+\w+).*\s+.*\s+.*(expires)\s+.*\s+\w+:\s+(\w+)\s+.*\s+.*(key-created-at).*\s+.*(datetime)\=\"([0-9]{4}[-]{1}[0-9]{2}[-]{1}\w+:\w+:\w+)"
		# ~ self.GITHUB_ENV
		# ~ self.gpg_data = findall(gpg_regex, document)
	
	# ~ def test_(self):
		# ~ pass

	# ~ def test_ssh_in_terminal():
		# ~ to_shell = "ssh -T git@gitlab.com"
		# ~ ssh_connect_gitlab = prompt('Are you sure you want to continue connecting (yes/no)?')
		# ~ prompt_expected = "The authenticity of host 'gitlab.com (35.231.145.151)' can't be established.\nECDSA key fingerprint is SHA256:HbW3g8zUjNSksFbqTiUWPWg2Bq1x8xdGUrliXFzSnUw.\nAre you sure you want to continue connecting (yes/no)? \nWarning: Permanently added 'gitlab.com' (ECDSA) to the list of known hosts."
		# ~ should_return = f"Welcome to GitLab, {GITLAB_ENV.get('USERNAME','@wearypossum4770')}!"

if __name__ == "__main__":
	main()
