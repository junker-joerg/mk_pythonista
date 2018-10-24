#!python
# definiere eine einfache Datenstruktur
# schreibe sie in eine Datenbank
# schreibe sie in ein Textfile
# schließe alles 
# schreibe den Fortschritt in ein Logfile

import pprint as pp
import sqlite3
import csv
import logging
import logging.handlers as handlers
import time

def readwriteData(mod):
	if (mod == 1):
		with open("mktest.csv", "r") as f:
			mkDaten = f.read()# liest die gesamte Datei
		logger.info("Datei mktest.csv eingelesen") 
	elif (mod == 2):
		with open("mktest.csv", "r") as f:
			mkDaten = f.write()# schreibt die gesamte Datei	
		logger.info("Datei mktest.csv geschrieben")
	else:
		logger.info("Error Datei mktest.csv")
		# Error in Log schreiben
   
# Funktion zum Öffnen der Datei und schreiben in Textdatei
def writeData():
	fileName ="mktest.txt"
	mkDatei = open(fileName, 'w')
	for i in range(5):
		mkDatei.write("\n Zeile"+" "+str(i))
		mkDatei.write("\n")
		mkDatei.write(str(i))
	mkDatei.close()		

# Funktion
def readData():
	fileName ="mktest.txt"
	mkDatei = open(fileName, 'r')
	mkDatei.read()		
												
"""
    #'r'(read), 'w'(write), 'a'(appending), 'r+'(both reading and writing)
    f = open('file_name', 'w')
    
    # Reads entire file
    f.read() 
    
    # Reads one line at a time
    f.readline() 
    
    # Writes the string to the file, returning the number of char written
    f.write('Add this line.') 
    
    f.close()e + " Refsnes")
    
    import sqlite3
conn = sqlite3.connect('example.db')


c = conn.cursor()

# Create table
c.execute('''CREATE TABLE stocks
			 (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
"""


class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

"""
p1 = Person("John", 36)
p1.myfunc()
"""

def sqlShell():
	
	# A minimal SQLite shell for experiments

	con = sqlite3.connect(":memory:")
	con.isolation_level = None
	cur = con.cursor()

	buffer = ""
	
	print("Enter your SQL commands to execute in sqlite3.")
	print("Enter a blank line to exit.")
	
	while True:
		line = input()
		if line == "":
			break
		buffer += line
		if sqlite3.complete_statement(buffer):
			try:
				buffer = buffer.strip()
				cur.execute(buffer)
	
				if buffer.lstrip().upper().startswith("SELECT"):
					print(cur.fetchall())
			except sqlite3.Error as e:
				print("An error occurred:", e.args[0])
			buffer = ""
	
	con.close()
	
def mylogging():
	pass
  
if __name__ == "__main__":
	# starte logging
	logger = logging.getLogger(__name__)
	logger.setLevel(logging.INFO)
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')	
	logHandler = logging.FileHandler('mk_app.log', mode="a")	
	logHandler.setFormatter(formatter)
	logger.addHandler(logHandler)	
	logger.info("Starte Logging")
	
	pp.pprint('Start')
	readwriteData(mod=1)
	readwriteData(mod=2)
	#sqlShell()
	 



