
class Parser:
	position = -1
	def __init__(self,line,position):
		self.line = line
		self.position = position
		#self.match()
		print (self.LookAhead(self.line))

		print ('Assignment2 Running')
	def match(self,next):
		print 'This is the match function'
		#if self.LookAhead(self.line) is ''
	def LookAhead(self,line):
		lookahead = self.Next(self.line)   # this is the look ahead function calling the next function and having the next value
		return lookahead
	def Next(self,line):  # This isthe next function whcih increments the fuinction by 1 .
		self.position += 1
		return line[self.position]


class Main:
	def main(self):
		if __name__ == '__main__':  # main start of the file !
			linenumber=0  # to keep the track of the specific line
			print ('The main Program has just started!')
			file_reader=open('symbolictree.cpp','r')  # this is the file being read which needs to be parssed
			for line in file_reader:
				line = line.strip()
				position = -1
				print ('___________________NEXTLINE_________________')  # to seperate the parser with th line such that we can differentiate
				PSCHECK=Parser(line,position)   # This is passing to the line of the parser
				#PSCHECK.Lookahead(line)
				linenumber += 1   # this is to increment the line number in such a way that the track is kept inthe record

M_Entry=Main() # Class object of the main class
M_Entry.main() # main funtion call of the main class


# the grammer is like -->
'''  exp --> term exp`
         exp` --> +term exp` | -term exp`| NULL
         term --> factor term`
         term` --> *factor term` | /factor term` | NULL
         factor --> exp | digits
         digits --> signed digit digits | signed digit| signed DECIMALDIGIT
         DECIMIALDIGIT --> digits DECIMAL
         DECIMAL --> POINT digit| POINT digits
         digit --> 0|1|2......|9
         signed --> +|-|NULL

    '''