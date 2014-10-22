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

if "username" in form and "password" in form:
	login = 0;
	c.execute("Select password FROM users WHERE username = %s" % form.getvalue("username"))
	matched = c.fetchone()
	matchedString = "".join(matched)
	if form.getvalue("password") == matchedString:
		login = 1
	else:
		login = 0

mainFunctions.header(title = "Love2041")
form = cgi.FieldStorage()
if not "login" in form:
	pages.login_page()
else:	
	if "pageusername" in form:
		pages.profile_page(form.getvalue("pageusername"))
	else:
		pages.main_page()
if login == 1:
	print"""
	<form>
	<input type="hidden" name="username" value"%(1)s">
	<input type="hidden" name="username" value"%(1)s">
	
mainFunctions.footer()
