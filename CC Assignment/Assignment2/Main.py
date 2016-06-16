def Id_checker(ID_opcheck):  # 8th function call
	return ('ID--->'+str(ID_opcheck))  # this is the id checker to check the id s (returned to the 7th function)
def op_termchecker(op_temp):   # This is the term checker to check the term  (7th function call )
	return ('term-->',Id_checker(op_temp)) #This is the term  returned to the 6th checekr call
def left_rightplacechecker(left_opexpr,right_opexpr,op): #6th function call
	print ('')  # Services in progress :P
	if op == '=':
		print ('opexp-->'+str(op_termchecker(left_opexpr))+'\t opexpr-->"=" ,opexpr-->'+str(op_termchecker(right_opexpr))) # Here you need to pass this to a term
	try:
		temp_rop=int(right_opexpr) #this is hte temporary variabble to check the datatype of the right side
		print ('opexpr-->')
	except :
		print ('There is an operation error in the righthandside')
def opexprchecker(opexpr_single):  #5th call form the funciton
	print ('') # optional expression are checked through this function
	if '<' in opexpr_single:   # This is the place where the lesser sign is checked and then splited into different methods
		print ('THe opexpr is being splited in to the specified expressions')
	elif '>' in opexpr_single: # This is the place where the greate sign is taken in an account
		print ('')
		try:
			print ('')
			opexpr_singlelist=opexpr_single.split('>')  # here you are working on the greate condition
			left_opexpr = opexpr_singlelist[0] # equal sign left side consideration.
			right_opexpr = opexpr_singlelist[1]  # equal sign right side consideration.
			op='>'
			left_rightplacechecker(left_opexpr,right_opexpr,op) # this is the function is used to pass to the left-right checker
		except :
			print ('')
	elif '=' in opexpr_single: # This is the place where the opexpr of the equal sign is checked
		try:
			opexpr_singlelist=opexpr_single.split('=')
			left_opexpr = opexpr_singlelist[0] # equal sign left side consideration.
			right_opexpr = opexpr_singlelist[1]  # equal sign right side consideration.
			op='='
			left_rightplacechecker(left_opexpr,right_opexpr,op)# just checking the left side of the operational syntax '''You need to update here'''
			# here you need to check the datatype and the lft and the right specifier ''' Update here!!! <-------'''
		except :
			print ('There is an error in the opexpr production',opexpr_single) # this will be the error which will be replaced ( to show the fail result)
	elif '++' in opexpr_single:
		print ("unary increment!")
	elif opexpr_single is None:
		print ('opexpr -->Null')
def exprcheck(expr_single):
	print ('This is for the single expression check')
def Anonomous_function(exprs): # fiver4 call from the main function , conjucated by the other fucntion
	lengthofexps=len(exprs)  #this tells the length of the expressions
	checked = 0
	string_ofstatments = ""
	while checked < lengthofexps:
		if checked < lengthofexps-1:
			string_ofstatments += 'opexp;'   # This is before the ending of the opexpression such that it has a semicolon
			checked += 1
		else:
			string_ofstatments += 'opexp'  # this is the ending of the opexpression such that it doesnt have semicolon
			checked += 1
	return string_ofstatments
def StatmentChecker(statments):  # fiver3 call to the process (in such a way that the statment is checked. (fiver3 Call )
	if ';' in statments:
		explist=statments.split(';')  # this is to seperate the semicolon statments
		print ('statment-->',Anonomous_function(explist) )
		for i in explist:  # here we have a single experession splited in the way
			print ('opexp-->',i)  #*********************************Here adding the work by
			opexprchecker(i)
			' Here you need to write the different condition and then see the different condition.'
	else:
		if statments is bool: # if the statment in the known expression is while (True stuff)
			print('THe statment is boolean')
		elif '<' in statments:
			print ( 'exp--> "<" ',statments)  # if there is a single statment and it need to be represented  # here are the ***EXPR
		elif '>' in statments:
			print ('exp--> ">" ',statments)  # This is when there is the greatersign  of the operand   # Here are the EXPR
		elif '==' in statments:
			print ('exp--> "<" ',statments)   # This is when there is a lesser sign of the operand presend in the optional expression  # HERE are the expr
def Defined_FunctionCheck(predefined): # This is the second call  (2nd call)
	if predefined == 'if':
		print ('statment--> if')
	elif predefined == 'for':
		print ('statment-->for')
		if 'for' not in data_holding_list.values():

			data_holding_list['keyword'+str(KW)]='for'
			for iterator in data_holding_list:
				print (iterator,data_holding_list[iterator]) # This is adding the for in the dictionary such that it is east to see.
	elif predefined == 'while':
		print ('statment-->while')
		if 'while' not in data_holding_list.values():
			data_holding_list['keyword']
	else:
		print ('Error at line '+str(linenumber))
def Parenth_opencheck(line):   # This indicates the opeing of the parenthesis (fiver1 call)
	print ("THe parenthesis are being checked")
	line = line.strip()
	try:
		line = line.split('(')   # split at the starting of the parenthesis
		checker = 0
	except:
		print ('There is an Error in the starting parentesis')
		exit(0)
	Defined_FunctionCheck(line[0])
	print ('statment--->(')
	try:
		if checker==0:
			Rest_withoutstart=line[1].split(')')  # splits through the ending of the parenthesis
		else:
			print ('ERROR SYNTAX')
			exit(0)
	except:
		print ('There is an error in the closing parenthesis ')
		exit(0)
	P_withinstatment = Rest_withoutstart[0]  # To check the statments with in the ()
	P_afterstatment = Rest_withoutstart[1]  # the Statment after the parentesis finished ()statment;
	StatmentChecker(P_withinstatment) # the with in statment in the parenthesis is passed to the statment checker for the experession check and stuff
	print ('statment--->)')
	print ('statment--->',P_afterstatment)  # Here you need to write the after statment     # The #  # The Fi
if __name__ == '__main__':
	i = 0
	linenumber=0
	KW = 0  # this isthe keyword to remember the keys that will be stored when the key word will be detected
	Op_counter = 0
	print ('The main Program has just started!')
	file_reader=open('symbolictree.cpp','r')
	data_holding_list = dict()
	for line in file_reader:
		Parenth_opencheck(line)  #this is the place where the Main Assignment2 Starts creating a Parse tree stuff
		linenumber += 1

# you need to work on the > < and stuff of the op expression 8/3/2016 6:30PM
