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

def search_profile(searchname):
	c.execute("SELECT username FROM users WHERE username LIKE '%s' LIMIT 10" % searchname)
	names = c.fetchall()
	return names


def footer():
	print """
	</form>
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
	<form action="" method="POST">
	""" % {"1" : title}
	
	
	print """
	<div class="header-container">
		<img src="./images/logo.png" alt="Love2041" class="img-title">
		<input class="top-bar-button" id="button1" type="submit" value="Home Page"/>
		<input class="top-bar-button" name="searchusername" value="Search Usernames" type="text" id="button2"/>
		<input class="top-bar-button" id="button3" type="submit" value="search"/>
		<input class="top-bar-button" id="button4" type="submit" name="logout" value="logout"/>
	</div>
	"""
