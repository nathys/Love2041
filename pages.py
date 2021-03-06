#!/usr/bin/python
import re
import os
import cgi
import cgitb
import os
import random
import sqlite3
import mainFunctions
import jinja2

templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
templateEnv = jinja2.Environment(loader=templateLoader)

conn = sqlite3.connect('Love2041.db')
c = conn.cursor()


def main_page(searchFlag,offset,username):
	print """
	<p class="profile-text">
	</p>
	<div class="thumbnail-container">
	"""
	if searchFlag == 0:
		user = mainFunctions.get_profile(username)
	else:
		user = mainFunctions.search_profile(searchname = searchFlag)
	counter = 0 + offset
	for i in range(1,6):
		for j in range(1,3):
			if counter < len(user):
				name = user[counter]
				username = "".join(name)
				file = "./students/%s/photo00.jpg" % name
				data = {"1": file, "2" : username, "3": username, "4": i, "5" : j}
				print"""
				<div class="thumbnail-profile" id="top%(4)s-left%(5)s">
				<input type="image" name="pageusername" value="%(3)s" class="thumbnail-img" src="%(1)s" alt="profile of %(2)s"/>
				<input type="image" name="pageusername" value="%(3)s" class="thumbnail-image" style="color: transparent; border: 0px; z-index: 500; width: 24em; height: 23em;"/>
				Username: %(3)s
				</div>
				""" % data
				counter += 1
	if (counter == 0):
		print """
		<p class="not-found-text">
		<pre>
		No users found matching your search
		</pre>
		</p>
		"""
	if searchFlag == 0:	
		print """
		<input type="submit" class="top-bar-button" id="button5" name="next" value="Next"/>
		<input type="submit" class="top-bar-button" id="button6" name="prev" value="Previous"/>
		"""
		
	print """
	</div>
	"""
	

def profile_page(username):
	file = "students/%s/profile.txt" % username
	f = open(file,"r")
	c.execute("SELECT gender FROM users WHERE username = '%s'" % username)
	gender = c.fetchone()
	hobbies = []
	movies = []
	bands = []
	books = []
	shows = []
	namecounter = 0
	moviecounter = 0
	bandcounter = 0
	hobbycounter = 0
	showcounter = 0
	bookcounter = 0
	name = ""
	for line in f:
		if namecounter == 1:
			name = re.sub("\t|\n|  +", "", line)
			namecounter = 0
		if moviecounter == 1:
			if re.search("^\s",line):
				movie = re.sub("\t|\n|  +","",line)
				movies.append(movie)
			else:
				moviecounter = 0
		if bandcounter == 1:
			if re.search("^\s",line):
				band = re.sub("\t|\n|  +","",line)
				bands.append(band)
			else:
				bandcounter = 0
		if hobbycounter == 1:
			if re.search("^\s",line):
				hobby = re.sub("\t|\n|  +","",line)
				hobbies.append(hobby)
			else:
				hobbycounter = 0
		if showcounter == 1:
			if re.search("^\s",line):
				show = re.sub("\t|\n|  +","",line)
				shows.append(show)
			else:
				showcounter = 0
		if bookcounter == 1:
			if re.search("^\s",line):
				book = re.sub("\t|\n|  +","",line)
				books.append(book)
			else:
				bookcounter = 0
		
		if re.search("^name:",line):
			namecounter = 1
		if re.search("^favourite_movies",line):
			moviecounter = 1
		if re.search("^favourite_bands",line):
			bandcounter = 1
		if re.search("^favourite_hobbies",line):
			hobbycounter = 1
		if re.search("^favourite_TV_shows",line):
			showcounter = 1
		if re.search("^favourite_books",line):
			bookcounter = 1
	movielist = "</li>\n<li class=\"profile-list\">".join(movies)
	bandlist = "</li>\n<li class=\"profile-list\">".join(bands)
	hobbylist = "</li>\n<li class=\"profile-list\">".join(hobbies)
	showlist = "</li>\n<li class=\"profile-list\">".join(shows)
	booklist = "</li>\n<li class=\"profile-list\">".join(books)
	info = {"1":username, "2":username, "3": gender[0], "4":movielist, "5":hobbylist, "6":booklist, "7":showlist, "8":bandlist}
	print """
	<div class="profile-container">
	<pre>
	<p>
	
	
	<img src="./students/%(1)s/photo00.jpg" style="vertical-align:middle" alt="Profile Photo">
	
	
	Username:
	
		%(2)s
	
	Gender:

		%(3)s

	Favourite Movies:
	
		<li class="profile-list">%(4)s
		</li>
	
	Hobbies:
	
		<li class="profile-list">%(5)s
		</li>
	
	Favourite Books:
	
		<li class="profile-list">%(6)s
		</li>
		
	Favourite Tv Shows:
	
		<li class="profile-list">%(7)s
		</li>
		
	Favourite Bands:
	
		<li class="profile-list">%(8)s
		</li>
	</p>
	</pre>
	</div>
	""" % info
	
	print """
	<pre>
	<input type="submit" name="Home Page" value="Home Page"/>
	</pre>
	"""
	
	
def login_page(loginstatus):
	template = templateEnv.get_template("login.html")
	info = {"login": loginstatus}
	output = template.render(info)
	print output
	
	
def not_found():
	template = templateEnv.get_template("notFound.html")
	output = template.render()
	print output
