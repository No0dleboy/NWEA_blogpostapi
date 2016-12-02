#!../flask/bin/python
from flask import Flask, request, jsonify
import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


#c.execute("SELECT * FROM posts")
#posts = c.fetchall()
#conn.close
app = Flask(__name__)


@app.route('/posts', methods=['GET'])
def get_posts():
    conn = sqlite3.connect('blog.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    posts = c.execute("SELECT * FROM posts").fetchall()
    conn.close
    return jsonify({'posts': posts})

@app.route('/post', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'title': request.json['title'],
        'body': request.json.get('body', "")
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
