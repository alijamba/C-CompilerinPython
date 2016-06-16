class Parser():
	oplist='+', '-', '*', '/', '%'
	digitlist = list()
	temp_holder_sign = ''
	for tem_counter in range(0,):
		digitlist.append(tem_counter)
	def digitIntialized(self):
		self.digitlist = self.digitlist
		#print (self.digitlist)
	final_check=""
	def __init__(self,expression,position):
		print ('The main Constructor of the Assignment2')
		self.expression = expression # this is the main expression which will be in form of complete line
		self.position = position # this isthe position holder for the character
		self.sizeofexp = len(self.expression)
		if self.sizeofexp <= 0:
			print ('To short')
			exit()
		# this lookahead holds character passed by the main function!
		self.lookahead = self.next_()  # this increment the index by 1 ( -1 is changesd to +1 ) so that it is east to use
		self.digitIntialized() #this just checks the digit list
		#for i in range(0,len(expression) - 1):
			#self.lookahead = self.next_()
			#print (self.lookahead)
		print ('#_______^This is the Constructor^________#')
		self.expr()  # This is the main entry for the expression in such a way that the expression are easily expressed.
		print ('Mathematical exp was :' + str(self.expression))
		print ('After Parsing stuff :->'+str(self.final_check))
		print ('Checked !')
	def next_(self):
		self.position += 1  # position is incremented every time the next_ function is called
		self.lookahead = self.expression[self.position]
		return self.lookahead  # this return the lookahead which is read fromthe next Function
 	def expr(self):  #First Entry POint
		print ('exp --> term exp`')
		self.term()    #starting term is send to the term function so that it can be translated
		self.expr_R()    #Rest is send back to the Rest function (recursively)
		return
	def expr_R(self):  #fiver3 entry point
		print ("exp`-->+term exp`|-term exp`| NULL")
		if self.lookahead == '+':
			self.lookahead = self.next_()
			print (self.lookahead)
			self.term()
			#print ('+')
			self.final_check += '+'
			self.expr_R()
			return
		elif self.lookahead == '-':
			self.lookahead = self.next_()
			self.term()
			#print ('-')
			self.final_check += '-'
			self.expr_R()
			return
		else:
			return
	def term(self):  #2nd entry point
		print ('term--> factor term`')
		if self.lookahead =='%' or self.lookahead =='/' or self.lookahead =='*':
			print('Error in the expression Bae!')
			exit()
		self.factor() # this calls the factor program  suh a way that the main program is accessible !!!! <-- :*
		self.term_R()
		return
	def term_R(self):
		print ('*factor term` | /factor term` | NULL')
		if self.lookahead =='*':
			self.lookahead = self.next_()
			if self.lookahead =='*':
				print ('There is a logical error in the expression')
				exit()
			self.factor()
			#print ('*')
			self.final_check += '*'
			self.term_R()
			return
		elif self.lookahead =='/':
			self.lookahead = self.next_()
			if self.lookahead =='/':
				print ('There is a logical error in the division expression')
				exit()
			self.factor()
			#print ('/')
			self.final_check +='/'
			self.term_R()
			return
		else:
			return
	def factor(self):  # fiver3 entry point  is here !
		print ('factor-->(exp) | digits.')
		if self.lookahead =='(':

			print ('(')
			self.lookahead = self.next_()
			self.expr()  #fiver4 entry point if possible
			self.lookahead = self.next_()
			print (')')
			return
		else:
			self.digits()
			return
	def digits(self):
		print('digits--> digit digits')
		if self.lookahead == '-' or self.lookahead == '+':
			self.signed()
		self.digit()
		if self.lookahead in self.digitlist:
			self.digits()
			print('^&*(*&*(*&(&*')
		return
	def signed(self):
		if self.lookahead == '-':
			self.temp_holder_sign = '-'
		elif self.lookahead =='+':
			self.temp_holder_sign = '+'
		elif self.lookahead =='*':
			print ('There is an error in the expression')
			exit()
		elif self.lookahead =='/':
			print ('There is an error in the expression')
			exit()
		self.lookahead=self.next_()  # this will be holding the sign of the number
		print ('we are here')
		return
	def digit(self):
		print ('-->Digit an increment here')
		#if str(self.lookahead) in self.digitlist:
		#print (self.lookahead)
			#print (self.lookahead)
		self.final_check += '['+str(self.temp_holder_sign)+str(self.lookahead)+']'
		self.temp_holder_sign=''
		if self.position < self.sizeofexp - 1:
			self.lookahead = self.next_()
			return
		#else: # there is an error in this place logical error such that theprogram is unable to execute!
			#print (self.lookahead)
		#	print ('There is an error here !!!!!!!!!') # this will show an error if the expression is false so that it can detect errors
		#	exit(0)
def main():
	if __name__ == '__main__':
		print ('The main Program has been started')
		place_number = -1
		Input_Expression = raw_input("Enter the Complete Expression here ->")
		try:PS = Parser(Input_Expression, -1)
		except ValueError:
			print ('Error in the expression')
			exit(0)
main()
#char lookahead= next();
# This is the call to the main function of the parser

'''
Grammer according to Muhammad Shafay Amjad 454-BSCS-13 E-2 , C.R
   exp --> term exp`
   exp`-->+term exp`|-term exp`| NULL
   L.H.S
   term--> factor term`
   term`-->*factor term` | /factor term` | NULL
   factor-->(exp) | digits.
   digits --> signed digit digits|signed digit
   digit --> 0|1....|9
   signed --> +| -|Null
   '''
#