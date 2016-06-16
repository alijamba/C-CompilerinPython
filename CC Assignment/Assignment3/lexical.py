class LexicalAnalyzer:
	oplist_holder = list()
	position = int
	digit_list_holder = list()
	lexical_tokens = list()  # this list hold the token which are generated such that it hold all the data
	keyword_listholder_size5 = list()
	keyword_listholder_size4 = list()
	keyword_listholder_size3 = list()
	keyword_listholder_size2 = list()
	id_holder = ""
	regeneration_codefromlist = ""
	check = 0

	def __init__(self, line, position):
		self.line = line  #
		self.position = position  # this keeps the position of the specific place
		self.oplist()  # this creates a list of operators
		self.keyword_list()  # this creates a lise of key words (depending upon the size of the keyword
		self.digit_list()  # this hold the numeric check
		self.character_checker()  # this is passing the line to the chacter checker !
		print ('Lexical analyzer has finished the specific line check')
		for i in range(0,len(self.lexical_tokens) - 1):           # this is the bakward generation of the expression
			self.regeneration_codefromlist += str(self.lexical_tokens[i][1])
		#print ('Regenerating from the lexical tokens: -->"' + self.regeneration_codefromlist+'"<--')
		self.regeneration_codefromlist =""
		for i in range(0,len(self.lexical_tokens) - 1):           # this is the bakward generation of the expression
			self.regeneration_codefromlist += str(self.lexical_tokens[i][0])+" "
		#print ('Regenerating from the lexical tokens: -->"' + self.regeneration_codefromlist + '"<--')
	def oplist(self):
		self.oplist_holder = ['+', '-', '*', '/', '%', '(', ')', '[', ']', '{', '}', '^', '=', '<', '>', ':', ';', '.']
		return  # this is the operation checker

	def keyword_list(self):
		self.keyword_listholder_size5 = ['while', 'print', 'scanf', 'getch']
		self.keyword_listholder_size4 = ['else', 'cout', 'case', 'void', 'main', 'endl']
		self.keyword_listholder_size3 = ['for', 'cin']
		self.keyword_listholder_size2 = ['if', 'do']
		return  # this is the keyword list checker

	def digit_list(self):
		self.digit_list_holder = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
		return

	def character_checker(self):
		while self.position < len(self.line):  # this is the while loop to read the complete all character are read
			if self.line[self.position] in self.oplist_holder:  # this is to check the operator
				self.lexical_tokens.append(['op', str(self.line[self.position])])  # this append the lexical system
				self.position += 1
				self.check = 1  # just a reminder to differentiate between the code you wrote
			elif self.line[self.position] in self.digit_list_holder:  # this is to check the digit holder
				self.lexical_tokens.append(['NUM', str(self.line[self.position])])
				self.position += 1
				self.check = 1  # just a reminder to differentiate between the code you wrote
			elif self.line[self.position] + self.line[self.position + 1] in self.keyword_listholder_size2:  # 2size char
				temporaryvariable = self.line[self.position] + self.line[self.position + 1]
				self.lexical_tokens.append(['KW', str(temporaryvariable)])
				self.position += 2
				self.check = 1  # just a reminder to differentiate between the code you wrote
			elif self.line[self.position] + self.line[self.position + 1] + self.line[
						self.position + 2] in self.keyword_listholder_size3:
				temporaryvariable = self.line[self.position] + self.line[self.position + 1] + self.line[
					self.position + 2]
				self.lexical_tokens.append(['KW', str(temporaryvariable)])
				self.position += 3
				self.check = 1  # just a reminder to differentiate between the code you wrote
			elif self.line[self.position] + self.line[self.position + 1] + self.line[self.position + 2] + self.line[
						self.position + 3] in self.keyword_listholder_size4:  # 4 size character
				temporaryvariable = self.line[self.position] + self.line[self.position + 1] + self.line[
					self.position + 2
					] + self.line[self.position + 3]
				self.lexical_tokens.append(['KW', str(temporaryvariable)])
				self.position += 4
				self.check = 1  # just a reminder to differentiate between the code you wrote
			elif (self.line[self.position] + self.line[self.position + 1] + self.line[self.position + 2] + self.line[
					self.position + 3] + self.line[self.position + 4]) in self.keyword_listholder_size5:
				temporaryvariable = self.line[self.position] + self.line[self.position + 1] + self.line[
					self.position + 2] + self.line[self.position + 3] + self.line[self.position + 4]
				self.lexical_tokens.append(['KW', str(temporaryvariable)])
				self.position += 5
				self.check = 1  # just a reminder to differentiate between the code you wrote

			else:
				# print ('Not matched!!')
				if self.position < len(self.line):
					if self.line[self.position] is ' ':
						self.position += 1
						continue
					while (self.line[self.position] not in self.oplist_holder) and (self.line[self.position] not in self.digit_list_holder) and((self.line[self.position] + self.line[
								self.position + 1]) not in self.keyword_listholder_size2) and ((self.line[self.position] + self.line[self.position + 1] + self.line[
								self.position + 2]) not in self.keyword_listholder_size3) and ((self.line[self.position] +
								self.line[self.position + 1] + self.line[self.position + 2] + self.line[
								self.position + 3]) not in self.keyword_listholder_size4):
						self.id_holder += self.line[self.position]
						self.position += 1
					self.lexical_tokens.append(['ID', str(self.id_holder)])
					self.id_holder = ""
				else:
					#print (self.lexical_tokens)
					exit()
		print (self.lexical_tokens)
		scope = 0

		for lexem_token in self.lexical_tokens:
			#print(lexem_token)  # this is just for the debuggin purposes
			if str(lexem_token).__contains__('{'):
				startvalue = self.lexical_tokens.index(lexem_token)  # this is the start value which will be used to save the index of the chukr
				for i in range(len(self.lexical_tokens)):
					if str(i).__contains__('}'):
						scope -= 1
						break
				scope += 1
				self.create_symbol_table(scope, lexem_token)
			else:
				self.create_symbol_table(scope, lexem_token)
	def create_symbol_table(self, scope, attribute):
		symbollist = list()
		symbollist.append((attribute, scope))
		print (symbollist)



if __name__ == '__main__':
	print ('The Program has been started !')
	filename = raw_input('Enter the file name to read!')
	if filename is '':
		print ('None detected file , no input going to a valid file to check!')
		filename = 'characterstream'
	try:
		file_reader = open(filename, 'r')
		line_number = 1
		tempobj = 0
		# print (file_reader.readlines())
		file_data = file_reader.readlines()
		list_data = ""
		for liner in file_data:
			liner = liner.strip()
			list_data += liner
		#print ("%^&*()*REW#@$%^&*(" +list_data)
		LA_Object = LexicalAnalyzer(list_data, 0)  # this is passing the data to the class lexical analyzer
		line_number += 1
		print ('line tokenized : ' + str(line_number - 1))
	except ValueError:
		print (ValueError)
		exit(0)
