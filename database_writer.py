import sqlite3
import os
import re
conn = sqlite3.connect('Love2041.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE users
             (username TEXT, password TEXT, gender TEXT)''')

direcs = os.listdir('./students/')
idnum  = 0
for line in direcs:
	idnum += 1
	username = line
	file = "./students/%s/profile.txt" % username
	f = open(file,"r")
	flag = 0
	genderflag = 0
	for words in f:
		if flag == 1:
			password = words
			flag = 0;
		if genderflag == 1:
			if re.search("^\s*female",words):
				gender = "female"
			else:
				gender = "male"
			genderflag = 0

		if re.search("^\s*password:",words):
			flag = 1;
		if re.search("^\s*gender:",words):
			genderflag = 1

	info = {"1": username,"2":password, "3": gender}
	c.execute("INSERT INTO users VALUES ('%(1)s','%(2)s','%(3)s')" % info ) 
	f.close()
	

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
