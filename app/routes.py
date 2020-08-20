from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kirill'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Moscow!'
        },
        {
            'author': {'username': 'Vasya'},
            'body': 'Nice vodka!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
