#!/usr/bin/python

import re
import os
import cgi
import cgitb
import os
import random
import pages
import sqlite3

conn = sqlite3.connect('Love2041.db')
c = conn.cursor()

def get_profile():
	c.execute("SELECT username FROM users ORDER BY RANDOM() LIMIT 10")
	names = c.fetchall()
	return names


def footer():
	print """
	</body>
	</html>
	"""

def header(title):
	print "Content-type: text/html"
	print
	print """
	<html xmlns="http://www.w3.org/1999/xhtml" lang="en-US" xml:lang="en-US">
	<head>
	<link rel="stylesheet" type="text/css" href="style.css">
	<title>%(1)s</title>
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
	</head>
	<body>
	""" % {"1" : title}
	
	print """
	<form>
	<input type="hidden" name="username" value="%(1)s">
	<input type="hidden" name="password" value="%(2)s">
	<input type="hidden" name="login" value="%(3)s">
	</form>
	""" % formInfo
	
	print """
	<div class="header-container">
		<img src="./images/logo.png" alt="Love2041" class="img-title">
		<form action="http://cgi.cse.unsw.edu.au/~z5017806/Love2041.python.cgi" method="post">
		<input class="top-bar-button" id="button1" type="submit" value="Home Page"/>
		</form>
	</div>
	"""
