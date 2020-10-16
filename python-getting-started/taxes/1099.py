
class Form(object):

	def deadline(self):
		pass
	def do_i_file(self):
		return True
		pass


class Form1099(Form):
	def __init__(self):
		self.__title__ = "Title"
		self._name = "Miscellaneous Income and Nonemployee Compensation"
	def title(self):
		return self.__title__
		
new_1099 = Form1099().do_i_file()
print(new_1099)
print(Form1099.__dict__)
print(dir(Form1099))
