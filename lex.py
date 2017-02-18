import re
from sys import argv
#Removing comments

def removecomments():
	with open ("input.c", "r") as myfile:
		string=myfile.read()

	string = re.sub(re.compile("[^\"]/\*.*?\*/",re.DOTALL ) ,"" ,string) # remove all occurance streamed comments (/*COMMENT */) from string
	string = re.sub(re.compile("//.*?\n" ) ,"" ,string) # remove all occurance singleline comments (//COMMENT\n ) from string
	string = re.sub(re.compile("\n{2,}|[\t]+\n|[\t]+") ,"" ,string) # remove multiple spaces
	
	string=string.split("\n")

	with open("output","w+") as f:
		for i in string:
			i+="\n"
			f.write(i.lstrip())
	

#removecomments()
valueStack = []
def getNextToken():
	with open ("input_without_comments.c", "r") as myfile:
		string=myfile.read()
	
	operators = { '=': 'Assignment Operator','+': 'Additon Operator', '-' : 'Substraction Operator', '/' : 'Division Operator', '*': 'Multiplication Operator', '++' : 'increment Operator', '--' : 'Decrement Operator'};
	optr_keys = operators.keys()
	header = {'.h': 'header file'}
	header_keys = header.keys()
	
	datatype = {'int': 'Integer','float' : 'Floating Point', 'char': 'Character','long': 'long int'}
	datatype_keys = datatype.keys()
	delimiter = {';':'terminator symbol semicolon (;)'}
	delimiter_keys = delimiter.keys()

	blocks = {'{' : 'Blocked Statement Body Open', '}':'Blocked Statement Body Closed'}
	block_keys = blocks.keys()

	non_identifiers = ['_','-','+','/','*','`','~','!','@','#','$','%','^','&','*','(',')','=','|','"',':',';','{'
,'}','[',']','<','>','?','/']
	string.replace('\n',' ').replace('  ',' ')
	program =  string.strip().split(' ')
	print string

getNextToken();
	
	
	

	

	

	
	
	

#Hi!