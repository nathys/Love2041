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
if "change" in form:
	change = int(form.getvalue("change"))
	if "next" in form:
		change = change + 10
	if "prev" in form:
		change = change - 10
	if change < 0:
		change = 0
	if change >= 100:
		change = 90
	if "Home Page" in form:
		change = 0
else:
	change = 0
	

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
print"""
<h1> %s </h1> 
""" % change
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
				pages.main_page(searchFlag = form.getvalue("searchusername"), offset = change)
			else:
				pages.profile_page(form.getvalue("searchusername"))
		else:
			pages.main_page(searchFlag = 0, offset = change)
	else:
		pages.main_page(searchFlag = 0, offset = change)
	info = {"1" : form.getvalue("username"), "2": form.getvalue("password"), "3" : login, "4": change } 
	print"""
	<input type="hidden" name="username" value="%(1)s">
	<input type="hidden" name="password" value="%(2)s">
	<input type="hidden" name="login" value="%(3)s">
	<input type="hidden" name="change" value="%(4)s">
	""" % info
	
mainFunctions.footer()
