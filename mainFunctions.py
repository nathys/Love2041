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

def get_profile(username):
	names = []
	if os.path.exists("./students/%s/matches" % username):
		f = open("./students/%s/matches" % username , "r")
		for line in f:
			name = re.sub("\n", "" , line)
			names.append(name)
		f.close()
	else:
		genderFlag = 0
		pref = open("./students/%s/preferences.txt" % username,"r")
		for line in pref:
			if genderFlag == 1:
				if re.match("\s*female\s*",line):
					genfer = "female"
				else:
					gender = "male"
			if re.match("\s*gender:\s*",line):
				genderFlag = 1
		pref.close()
		c.execute("SELECT year FROM users WHERE username = '%s'" % username)
		year = c.fetchone()
		print """
		<h1> %s </h1>
		""" % year
		info = {"1" : gender , "2": year}
		c.execute("SELECT username FROM users WHERE gender ='%(1)s' ORDER by ABS(year - %(2)s)" % info)
		names = c.fetchall()
		f = open("./students/%s/matches" % username, "w+")
		for users in names:
			f.write("%s\n" % users)
		f.close()
	return names
		

def search_profile(searchname):
	c.execute("SELECT username FROM users WHERE username LIKE '%%%s%%' COLLATE NOCASE LIMIT 100" % searchname)
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
		<input class="top-bar-button" id="button1" type="submit" name="Home Page" value="Home Page"/>
		<input class="top-bar-button" name="searchusername" value="Search Usernames" type="text" id="button2"/>
		<input class="top-bar-button" id="button3" type="submit" value="search"/>
		<input class="top-bar-button" id="button4" type="submit" name="logout" value="logout"/>
	</div>
	"""
