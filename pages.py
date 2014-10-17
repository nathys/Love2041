#!/usr/bin/python
import re
import os
import cgi
import cgitb
import os
import random
import sqlite3
import mainFunctions

conn = sqlite3.connect('Love2041.db')
c = conn.cursor()


def main_page():
	print """
	<p class="profile-text">
	</p>
	<div class="thumbnail-container">
	"""
	for i in range(1,6):
		for j in range(1,3):
			keys = {"1":i,"2":j}
			user = mainFunctions.get_profile()
			for name in user:
				username = "".join(name)
				file = "./students/%s/photo00.jpg" % name
				data = {"1": file, "2" : username, "3": username}
				print"""
				<pre>
				<p class="thumbnail-text">
				<div class="thumbnail-profile" id="top%(1)s-left%(2)s">
				""" % keys
				print"""
				<img class="thumbnail-img" src="%(1)s" alt="profile of %(2)s"/>
				Username: %(3)s
				<form class="profile-button" action="" method="post">
				<input type="hidden" name="pageusername" value="%(3)s"/>
				<input type="submit" value="View Profile"/>
				</form>
				</p>
				</pre>
				</div>
				""" % data
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
	movielist = "\n\t\t".join(movies)
	bandlist = "\n\t\t".join(bands)
	hobbylist = "\n\t\t".join(hobbies)
	showlist = "\n\t\t".join(shows)
	booklist = "\n\t\t".join(books)
	info = {"1":username, "2":name, "3": gender[0], "4":movielist, "5":hobbylist, "6":booklist, "7":showlist, "8":bandlist}
	print """
	<div class="profile-container">
	<pre>
	<p class="profile-text">
	
	
	<img src="./students/%(1)s/photo00.jpg" style="vertical-align:middle" alt="Profile Photo">
	
	
	Name:
	
		%(2)s
	
	Gender:

		%(3)s

	Favourite Movies:
	
		%(4)s
	
	Hobbies:
	
		%(5)s
	
	Favourite Books:
	
		%(6)s
	
	Favourite Tv Shows:
	
		%(7)s
		
	Favourite Bands:
	
		%(8)s
	</p>
	</pre>
	</div>
	""" % info
	
	print """
	<pre>
	
	<form action="http://cgi.cse.unsw.edu.au/~z5017806/Love2041.python.cgi" method="post">
	<input type="submit" value="Home Page"/>
	</pre>
	"""