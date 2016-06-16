class Parser():
	oplist='+', '-', '*', '/', '%'
	def __init__(self,expression,position,lookahead):
		print ('The main Constructor of the Assignment2')
		self.expression = expression # this is the main expression which will be in form of complete line
		self.position = position # this isthe position holder for the character
		self.lookahead = lookahead # this lookahead holds character passed by the main function!
		self.lookahead = self.next_()  # this increment the index by 1
		#for i in range(0,len(expression) - 1):
			#self.lookahead = self.next_()
			#print (self.lookahead)
		self.EXP()
		print ('#_______^This is the Constructor^________#')
	def next_(self):
		self.position += 1  # position is incremented every time the next_ function is called
		self.lookahead = self.expression[self.position]
		return self.lookahead  # this return the lookahead which is read fromthe next Function
	def Factor(self):
		print ('This is the factor function')
		self.EXP()
		self.digits()
	def term(self):
		print ("This is hte Simple Term function")
		self.Factor()
		self.term_R()
		return
	def term_R(self):
		print ("This is the Recursive term Function")
		self.Factor() # you need to write if and else statments and the pritn stuff
		print ('* or /')
		self.term_R()
		return
	def POW_R(self):
		print ('This is the Power Recursive function')
		self.term()
		self.POW_R()
		print ('^')
		return
	def POW(self):
		print ('This is the Single POWER FUNCTION')
		self.term()
		self.POW_R()
		return
	def EXP(self):
		print ('This is the expression function')
		if self.lookahead not in self.oplist:
			self.term()  # This sends the first to the term function (lookahead first value ) :)
		self.EXP_R()
		return
	def EXP_R(self):
		print ("This is the EXPRESSION RECURSIVE FUNCTION")  # Expression recursion will be done here
		self.term() # You need to write the test cases
		self.EXP_R()
		return

	def digits(self):
		print ('this is digit recursive function')
		self.digit()
		self.digits()
		return
	def digit(self):
		print ('There are simple digit 0|2|3...|9')
		return

def main():
	if __name__ == '__main__':
		print ('The main Program has been started')
		place_number = -1
		Input_Expression = raw_input("Enter the Complete Expression here ->")
		PS = Parser(Input_Expression,-1,"")

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
   digits--> signed digit digits | signed digit decimal
   digit --> 0|1|2|3|...|9
   digits -->digit digits|digit
   '''
