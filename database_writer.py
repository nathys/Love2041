import sqlite3
import os
import re
conn = sqlite3.connect('Love2041.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE users
             (username TEXT, password TEXT, gender TEXT, year INTEGER, height DOUBLE)''')

direcs = os.listdir('./students/')
idnum  = 0
for line in direcs:
    idnum += 1
    username = line
    file = "./students/%s/profile.txt" % username
    f = open(file,"r")
    flag = 0
    genderflag = 0
    yearflag = 0
    heightflag = 0
    for words in f:
        if flag == 1:
            password = words
            flag = 0
        if genderflag == 1:
            if re.search("^\s*female",words):
                gender = "female"
            else:
                gender = "male"
            genderflag = 0
        
        if yearflag == 1:
            yearwith = re.sub("/[0-9]{2}/[0-9]{2}", "",words)
            year = re.sub("\t|\n|  +", "" , yearwith)
            yearflag = 0

        if heightflag == 1:
            height = re.sub("\t|\n|  +" , "" , words)
            height = re.sub("m", "", height)
            heightflag = 0

        if re.search("^\s*password:", words):
            flag = 1
        if re.search("^\s*gender:",words):
            genderflag = 1
        if re.search("\s*birthdate:", words):
            yearflag = 1
        if re.search("\s*height:", words):
            heightflag = 1

    info = {"1": username,"2":password, "3": gender, "4" : year, "5": height}
    c.execute("INSERT INTO users VALUES ('%(1)s','%(2)s','%(3)s','%(4)s','%(5)s')" % info ) 
    f.close()
    

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
