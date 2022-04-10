from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY']="MIHIRMODI"

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
@app.route('/home')
def HomePage():
    return render_template('Home.html',posts=post,title="Home Page")

@app.route('/about')
def About():
    return render_template('About.html',title="About Page")


@app.route('/login',methods=['GET','POST'])
def Login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Logged In Successfully')
        return redirect(url_for("HomePage"))
    return render_template('Login.html',title="Login",form=form)


@app.route('/register',methods=['GET','POST'])
def Register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!')
        return redirect(url_for("HomePage"))
    return render_template('Register.html',title="Registration",form=form)


if __name__ == '__main__':
    app.run()
