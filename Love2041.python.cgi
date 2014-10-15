#!/usr/bin/python

import re
import os
import cgi
import cgitb
import os
import random
import sqlite3

conn = sqlite3.connect('Love2041.db')
c = conn.cursor()




##########




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



def footer():
	print """
	</body>
	</html>
	"""


def main_page(username):
	print """
	<div class="header-container">
		<img src="./images/logo.png" alt="Love2041" class="img-title">
	</div>
	"""
	file = "students/"+ username + "/profile.txt"
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
	</pre>
	</div>
	""" % info
	
	print """
	<pre>
	
	<form action="" method="post">
	<input type="submit" value="Next Profile"/>
	</pre>
	"""
	
def get_profile():
	number = random.randint(1,len(os.listdir('./students/')))
	counter = 0
	direcs = os.listdir('./students/')
	for line in direcs:
		if counter >= number:
			username = line
			break
		else:
			counter+=1
	return username
	
	
	
	

username = get_profile()
header(title = "Love2041")
main_page(username)
footer()
