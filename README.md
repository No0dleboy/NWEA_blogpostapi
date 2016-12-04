# Blog Post API Assignment

NWEA DevOps job application code evaluation.
This is a blog post API designed to write single posts to the database and retrieve a list of all posts from the database.

## Installation

```
git clone https://github.com/No0dleboy/NWEA_blogpostapi.git
sudo pip install -r requirements.txt
# If you do not have sudo access, you can install into your home: pip install --user -r requirements.txt
./NWEA_blogpostapi/blogpostapi.py
```
At this point, the api should start up and be reachable at http://localhost:5000/posts via a web browser or curl.
```
# Retrieve posts:
curl -i http://localhost:5000/posts
# Create new post:
curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Title of Post","body":"Content of post."}' http://localhost:5000/post
```
### Prerequisites

* Python 2.6+
* pip

