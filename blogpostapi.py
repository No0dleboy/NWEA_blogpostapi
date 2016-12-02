#! /usr/bin/python

# import required modules
from flask import Flask, request, jsonify
import sqlite3

#  Format the results of a sql row from a list into a set of key/value pairs (to get the column names)
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# Set app as Flask object
app = Flask(__name__)

# Setup GET method for /posts uri
@app.route('/posts', methods=['GET'])
# Connect to database, retrieve all posts and convert to json
def get_posts():
    conn = sqlite3.connect('blog.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    posts = c.execute("SELECT * FROM posts").fetchall()
    conn.close
    return jsonify({'posts': posts})

# Run the app on the host IP
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
