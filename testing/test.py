#!/usr/bin/python
import json, sqlite3

post = json.load(open('data.json'))
print post
print post['body']

conn = sqlite3.connect('blog.db')
c = conn.cursor()
c.execute("INSERT INTO posts(title, body) VALUES (?,?)", (post['title'], post['body']))
conn.commit()
conn.close()
conn = sqlite3.connect('blog.db')
c = conn.cursor()
for row in c.execute("SELECT * FROM posts"):
  print row
