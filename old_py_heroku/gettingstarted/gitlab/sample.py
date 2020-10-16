from os import popen
from unittest import main, TestCase
import pytest
from pprint import PrettyPrinter	
pp = PrettyPrinter(indent=4)	
class TestSample(TestCase):
	def test_command_args(self):
		to_shell='ls -a'
		expected = [".","..","gitlab_com_profile_gpg_keys.txt","gitlab_com_profile_keys.txt","gpg_setup.py","init_gpg_data.json","sample.py","test_gpg_setup.py"]
		cmd_line_output=[]
		with popen(to_shell) as cmd_line_input:
			cmd_line_output= cmd_line_input.read().split('\n')[:-1]
		assert cmd_line_output == expected
if __name__ == "__main__":
	main()


# ~ import subprocess
# ~ subprocess.call("ls")
