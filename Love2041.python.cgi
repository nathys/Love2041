#!/usr/bin/python

import re
import os
import cgi
import cgitb
import os
import random




##########




def header(title,background):
	print "Content-type: text/html"
	print
	print """
	<html xmlns="http://www.w3.org/1999/xhtml" lang="en-US" xml:lang="en-US">
	<head>
	<link rel="stylesheet" type="text/css" href="style.css">
	<title>%(1)s</title>
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
	</head>
	<body bgcolor="#%(2)s">

	""" % {"1" : title, "2": background}



def footer():
	print """
	</body>
	</html>
	"""


def main_page(username):
	print """
	<img src="./images/logo.png" style="vertical-align:middle; text-align:center" alt="Love2041">
	"""
	file = "students/"+ username + "/profile.txt"
	f = open(file,"r")
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
	info = {"1":username, "2":name, "3":movielist, "4":hobbylist, "5":booklist, "6":showlist, "7":bandlist}
	print """
	<text> 
	<pre>
	
	
	<img src="./students/%(1)s/photo00.jpg" style="vertical-align:middle" alt="Profile Photo">
	
	
	Name:
	
		%(2)s
	
	
	Favourite Movies:
	
		%(3)s
	
	Hobbies:
	
		%(4)s
	
	Favourite Books:
	
		%(5)s
	
	Favourite Tv Shows:
	
		%(6)s
		
	Favourite Bands:
	
		%(7)s
	</pre>
	</text>
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
header(title = "Love2041",background = "D4A1F6")
main_page(username)
footer()
