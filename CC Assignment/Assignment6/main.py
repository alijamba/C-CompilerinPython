class pre_processer:  # this function will be used to check the preprocessoer class
	print("This is the preprocessoer class")
	filename = ""
	index = 0
	check = 0

	def __init__(self, filename):
		self.filename = filename  # this intializes the file name such that the file name is saved in the variable.
		data = self.read_data()  # this gets the data form the file
		for line in data:
			line = line.strip()  # removes the extra spaces
			exit() #only for debuggin
			self.check_line(line) # passes the current line to the check  function to check the specific line


	def read_data(self):
		file_reader = open(self.filename, 'r')
		data = file_reader.readlines()  # this reads all the data from the file
		return data

	def check_line(self, line, check):
		self.check = check
		header_file_name = ""
		if line[check] == '#' and line[check + 1] == 'i' and line[check + 2] == 'c' and line[check + 3] == 'l' and \
					 line[check + 4] == 'u' and line[check + 5] == 'd' and line[check + 6] == 'e':
			print ('Include detected!')
			self.check = check + 6
			if line[self.check] =='<':
				self.check += 1
				try:
					while line[self.check] !='>':
						header_file_name += line[self.check]
						self.check+= 1
				except:
					print ('Systax error at ',self.check,"  position")

		elif line[check] == '#' and line[check + 1] == 'd' and line[check + 2] == 'e' and line[check + 3] == 'f' and \
					 line[check + 4] == 'i' and line[check + 5] == 'n' and line[check + 6] == 'e':
			print ('define detected!')

		elif line[check] == '#' and line[check + 1] == 'i' and line[check + 2] == 'f':
			print ('if detected')


# !!!!!!!!!!!!!!!!!!!GRAMMER CLASS CHECKING TECHNIQUE BELOW!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class grammer_checker:
	print("This is the grammer checker")
# !!!!!!!!!!!!!!!!!! GRAMMER CLASS CHECKING TECHNIQUE ENDING ABOVE!!!!!!!!!!!!!!!!!!!!!!!!!

# !!!!!!!!!!!!!!!!!! LEXICAL CHACKER STARTING TECHNIQUE
class lexical_checker:
	print("This is the lexical checker")
# !!!!!!!!!!!!!!!!!!!COMPILE CLASS WHICH WILL BE RESPONSIBLE FOR THE Printing of the Compiler three address code.


class Compiler:  # The main compiler class which will be responsibile for the line of the file to be matched!
	filename = ""

	def __init__(self, filename):
		self.filename = filename

	def compilerfile(self):
		if self.filename == "":
			print("No File inputed! exiting.....")
			exit()
		else:
			print('The file input is :' + self.filename)  # just for debugging purposes
			pre_object = pre_processer(self.filename)  # preprocesser file


class Main:
	print('Welcome to the compiler created by Muhammad Shafay Amjad 454-BSCS-13 from section E2 , GCU lahore')
	filename = input("Enter the file name of the file you want to compiler (cpp)")
	c = Compiler(filename)
	c.compilerfile()  # this is the call of the compiler function which will start th


if __name__ == '__main__':
	Main()  # class the main function of the class Main!
