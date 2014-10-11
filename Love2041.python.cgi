#!/usr/bin/python

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
	<img src="./images/logo.png" style="horizontal-align:middle; text-align:center" alt="Love2041">
	"""
	file = "students/"+ username + "/profile.txt"
	f = open(file,"r")
	print """
	<text> %s </text>
	""" % f.read()
	



header(title = "Love2041",background = "D4A1F6")
main_page(username = "TenderPuppy60")
footer()
