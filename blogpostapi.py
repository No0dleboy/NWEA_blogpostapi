#! /usr/bin/python

# import sqlite3 module and connect to the database
import sqlite3
conn = sqlite3.connect('blog.db')

#Create cursor
c = conn.cursor()

# Insert a row of data
c.execute("INSERT INTO posts(title, body) VALUES ('TEST','Testing')")

# Commit changes
conn.commit()

# Select all rows and print to STDOUT
for row in c.execute("SELECT * FROM posts"):
  print row

# Cleanup while testing.  Leave DB empty.
c.execute("DELETE FROM posts")
conn.commit()
conn.close()
