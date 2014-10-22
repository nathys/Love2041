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


if not "login" in form:
	if "username" in form and "password" in form:
		login = 0;
		c.execute("Select password FROM users WHERE username = '%s'" % form.getvalue("username"))
		matched = c.fetchone()
		if form.getvalue("password") == matched:
			login = 1
		else:
			login = 2
else:
	login = "".join(form.getvalue("login"))

mainFunctions.header(title = "Love2041")
if not "login" in form:
	pages.login_page(loginstatus=0)
elif "%s" % form.getvalue("login") != "1":
	pages.login_page(login)
else:
	if "pageusername" in form:
		pages.profile_page(form.getvalue("pageusername"))
	else:
		pages.main_page()
	info = {"1" : form.getvalue("username"), "2": form.getvalue("password"), "3" : form.getvalue("login") } 
	print"""
	<form>
	<input type="hidden" name="username" value"%(1)s">
	<input type="hidden" name="username" value"%(2)s">
	<input type="hidden" name="username" value"%(3)s">
	</form>
	""" % info
	
mainFunctions.footer()
