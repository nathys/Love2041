#!/usr/bin/python

import re
import os
import cgi
import cgitb
import os
import random
import sqlite3
import pages
import mainFunctions

conn = sqlite3.connect('Love2041.db')
c = conn.cursor()

##########
form = cgi.FieldStorage()

if "username" in form and "password" in form:
	c.execute("Select password FROM users WHERE username = '%s'" % form.getvalue("username"))
	matched = c.fetchone()
	if matched is None:
		login = 3
	else:
		toMatch = re.sub("\t|\n|  +", "", matched[0])
		if form.getvalue("password") == toMatch :
			login = 1
		else:
			login = 2
else:
	login = 0
	
if "logout" in form:
	login = 0

mainFunctions.header(title = "Love2041")
if not "login" in form:
	pages.login_page(loginstatus = login)
elif login != 1:
	pages.login_page(loginstatus = login)
else:
	if "pageusername" in form:
		pages.profile_page(form.getvalue("pageusername"))
	elif "searchusername" in form:
		if form.getvalue("searchusername") != "Search Usernames":
			c.execute("Select username FROM users WHERE username = '%s'" % form.getvalue("searchusername"))
			search = c.fetchone()
			if search is None:
				pages.main_page(searchname = search)
			else:
				pages.profile_page(form.getvalue("searchusername"))
		else:
			pages.main_page(0)
	else:
		pages.main_page(0)
	info = {"1" : form.getvalue("username"), "2": form.getvalue("password"), "3" : login } 
	print"""
	<input type="hidden" name="username" value="%(1)s">
	<input type="hidden" name="password" value="%(2)s">
	<input type="hidden" name="login" value="%(3)s">
	""" % info
	
mainFunctions.footer()
