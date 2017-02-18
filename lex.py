import re
from sys import argv
#Removing comments

def removecomments():
	with open ("input.c", "r") as myfile:
		string=myfile.read()
	string = re.sub(re.compile("[^\"]/\*.*?\*/",re.DOTALL ) ,"" ,string) # remove all occurance streamed comments (/*COMMENT */) from string
	string = re.sub(re.compile("//.*?\n" ) ,"" ,string) # remove all occurance singleline comments (//COMMENT\n ) from string
	print string
	string=string.split("\n")
	string="\n".join(string)
	print string
	with open("output","w+") as f:
		for i in string:
			f.write(i)
	

removecomments()

