class Parser():
	oplist='+', '-', '*', '/', '%'
	digitlist = '0','1','2','3','4','5','6','7','8','9','0'
	final_check=""
	def __init__(self,expression,position,lookahead):
		print ('The main Constructor of the Assignment2')
		self.expression = expression # this is the main expression which will be in form of complete line
		self.position = position # this isthe position holder for the character
		self.lookahead = lookahead # this lookahead holds character passed by the main function!
		self.lookahead = self.next_()  # this increment the index by 1
		self.sizeofexp = len(self.expression)
		#for i in range(0,len(expression) - 1):
			#self.lookahead = self.next_()
			#print (self.lookahead)
		self.expr()
		print ('#_______^This is the Constructor^________#')
	def next_(self):
		self.position += 1  # position is incremented every time the next_ function is called
		self.lookahead = self.expression[self.position]
		return self.lookahead  # this return the lookahead which is read fromthe next Function
 	def expr(self):
		self.term()    #starting term is send to the term function so that it can be translated
		self.Rest()    #Rest is send back to the Rest function (recursively)
	def term(self):
		if self.lookahead in self.digitlist:  # this is to check if the term is a digit !
			print ('[' + str(self.lookahead) + ']')
			self.final_check += '[' + str(self.lookahead) + ']'
			if self.position < len(self.expression)-1:
				self.lookahead = self.next_()
				if self.lookahead in self.digitlist:
					self.final_check += '[' + str(self.lookahead) + ']'
					if self.position < len(self.expression)-1:
						self.lookahead = self.next_()
			#if self.lookahead is '\r' or ' ':
				#exit()
	def Rest(self):
		#self.lookahead = self.next_()
		if self.lookahead == '+':
			self.lookahead = self.next_()  # this will bring the next operand in such a way that out of bpund doesnt occur
			self.term()  # this is the term checker
			print('+')  # Post expression listner
			self.final_check += '+'
			self.Rest()
		elif self.lookahead == '-':
			self.lookahead = self.next_()  # this will bring the next operand in such a way that out of bpund doesnt occur
			self.term()  # this is the term checker
			print('-')  # Post expression listner
			self.final_check += '-'
			self.Rest()
		elif self.lookahead == '*':
			self.lookahead = self.next_()  # this will bring the next operand in such a way that out of bpund doesnt occur
			self.term()  # this is the term checker
			print('*')  # Post expression listner
			self.final_check += '*'
			self.Rest()
		elif self.lookahead == '/':
			self.lookahead = self.next_()  # this will bring the next o5*9perand in such a way that out of bpund doesnt occur
			self.term()  # this is the term checker
			print('/')  # Post expression listner
			self.final_check += '/'
			self.Rest()

		print (self.final_check)
	def NULL(self):
		print ("")
def main():
	if __name__ == '__main__':
		print ('The main Program has been started')
		place_number = -1
		Input_Expression = raw_input("Enter the Complete Expression here ->")
		try:PS = Parser(Input_Expression,-1,"")
		except ValueError:
			print ('Error in the expression')
			exit(0)
main()
#char lookahead= next();
# This is the call to the main function of the parser

'''
Grammer according to Muhammad Shafay Amjad 454-BSCS-13 E-2 , C.R
   expr --> term Rest
   Rest --> +term {print ('+')}Rest | - term{print ('-')} Rest | NULL
   term --> 0 print (0) and so on| factor RestFactor
   RestFactor --> *factor Restfactor | /factor Restfactor | NULL
   '''
#