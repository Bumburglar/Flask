from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Jon'}  # fake user
    posts = [  # fake array of posts
             {
                 'author': {'nickname': 'Katherine'},
                 'body': {'Beautiful day in Madison!'}
             },
             {
                 'author': {'nickname': 'Bob'},
                 'body': {'Austin was fun.'}
             }
            ]
    return render_template('index.html', user=user, posts=posts)
