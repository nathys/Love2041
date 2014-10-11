#!/usr/bin/python

import re
import os
import cgi
import cgitb





##########




def header(title,background):
	print "Content-type: text/html"
	print
	print """
	<html xmlns="http://www.w3.org/1999/xhtml" lang="en-US" xml:lang="en-US">
	<head>
	<title>%(1)s</title>
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
	</head>
	<body bgcolor="#%(2)s">

	""" % {"1" : title, "2": background}



def footer():
	print """
	</body>
	</html>
	"""


def main_page(username):
	print """
	<img src="./images/logo.png" style="vertical-align:middle; text-align:center" alt="Love2041">
	"""
	file = "students/"+ username + "/profile.txt"
	f = open(file,"r")
	hobbies = []
	namecounter = 0
	name = ""
	for line in f:
		if namecounter == 1:
			name = re.sub("\t|\n|  +", "", line)
			namecounter = 0
		if re.search("name:",line):
			namecounter = 1
		if re.search("favourite_movies",line):
			newline = f.readline()
			while re.search("^\s",newline):
				hobby = re.sub("\t|\n|  +","",newline)
				hobbies = hobbies.append(hobby)
				newline = f.readline()
			
	hobbylist = '\n'.join(hobbies)
	movies = ""
	info = {"1":username, "2":name, "3":movies, "4":hobbylist}
	print """
	<text> 
	
	
	<img src="./students/$(1)s/photo00.jpg" style="vertical-align:middle" alt="Profile Photo"
	
	
	Name:
	
	%(2)s
	
	
	Favourite Movies:
	
	$(3)s
	
	Hobbies:
	
	$(4)s
	</text>
	""" % info
	
	



header(title = "Love2041",background = "D4A1F6")
main_page(username = "TenderPuppy60")
footer()
