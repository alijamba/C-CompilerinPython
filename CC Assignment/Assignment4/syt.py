class SymbolTable:
	name = ''  # Variable which hold's the name of the file
	data = ""  # this will be holding the over all data
	scopedata = ""
	def __init__(self):  # the constructor of the class symbol table
		print("We are in symbol table")  # Debugging purpose

	def symbolize_a_file(self, name):  # A function which will use to symbolize the file.
		self.name = name  # this intializes the name with the file name
		file_reader = open(name + '.txt', 'r')  # this is the command used for the reading of the file
		data_in_file = file_reader.readlines()  # reads all the lines fromthe file
		parentscope = list()
		for line in data_in_file:
			line = line.strip()  # strips the extra spaces
			self.data += line # adds the line to the data holding variable
		output_seperated_list = self.data.split('{')  # splits the list into seperated output files.
		for item in output_seperated_list:
			self.scope_symbol_table(item)

	def scope_symbol_table(self, inner_data):
		counter = 0
		while inner_data[counter] != '}':
			self.scopedata += inner_data[counter]
			counter += 1
	def spliter_semicolon(self,scope):
		pass
