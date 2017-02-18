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
	

removecomments()

#Hi!