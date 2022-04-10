from flask import Flask, render_template

app = Flask(__name__)

post=[
    {
        'author':'Mihir Modi',
        'title':'Blog Post 1',
        'content':'first post content',
        'date_posted':'april 20,2018'
    },
    {
        'author':'Ruchit Modi',
        'title':'Blog Post 1',
        'content':'first post content',
        'date_posted':'april 20,2018'
    },
    {
        'author':'Ayush Modi',
        'title':'Blog Post 1',
        'content':'first post content',
        'date_posted':'april 20,2018'
    }
]

@app.route('/')
@app.route('/Home')
def hello_world():
    return render_template('Home.html',posts=post,title="Home Page")


if __name__ == '__main__':
    app.run()
