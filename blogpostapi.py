#! /usr/bin/python

# import required modules
import sqlite3, os
from flask import Flask, request, jsonify, abort

dbase = os.path.dirname(os.path.realpath(__file__)) + '/blog.db' 

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
    conn = sqlite3.connect(dbase)
    conn.row_factory = dict_factory
    c = conn.cursor()
    posts = c.execute("SELECT * FROM posts").fetchall()
    conn.close
    return jsonify({'posts': posts})

# Setup POST method for /post uri
@app.route('/post', methods=['POST'])
# Connect to database, and set post value to json input.
def create_post():
    conn = sqlite3.connect('dbase')
    c = conn.cursor()
    post = request.json
    # Try to insert values from post array into database, then return post as json.
    try:
        c.execute("INSERT INTO posts(title, body) VALUES (?,?)", (post['title'], post['body']))
        conn.row_factory = dict_factory
        postid = c.lastrowid
        newpost = c.execute("SELECT * FROM posts WHERE post_id=?", (postid,)).fetchone()
        conn.commit()
        conn.close()
        return jsonify({'posted': newpost}),200
    # If unable to post, abort with 400 return code.
    except:
        conn.close()
        abort(400)

# Run the app on the host IP
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    #app.run(debug=True, host='localhost')
