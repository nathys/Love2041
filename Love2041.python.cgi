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

mainFunctions.header(title = "Love2041")
form = cgi.FieldStorage()
if "pageusername" in form:
	pages.profile_page(form.getvalue("pageusername"))
else:
	pages.main_page()
	
mainFunctions.footer()
