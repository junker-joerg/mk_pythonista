import sqlite3

persons = [("Hugo", "Boss"), ("Calvin", "Klein")]

con = sqlite3.connect("mktemp.db")

# Create the table
con.execute("create table person(firstname, lastname)")

# Fill the table
con.executemany("insert into person(firstname, lastname) values (?, ?)",
																persons)

# Print the table contents
for row in con.execute("select firstname, lastname from person"):
	print(row)

print("I just deleted", con.execute("delete from person").rowcount, "rows")

# Test 19.4.2020
