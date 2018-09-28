from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'd9e8ea1f5fd439c92e2adb55d83cc093'

posts = [
    {
        'author': 'Donald Trump',
        'title': 'Fake news!',
        'content': 'CNN says I am not the best! CNN is FAKE!',
        'date_posted': 'September 26, 2018'
    },
    {
        'author': 'Bernie Sanders',
        'title': 'It was rigged!',
        'content': 'Hillary and the DNC rigged the primary! I should be president!',
        'date_posted': 'September 27, 2018'
    },
    {
        'author': 'Hillary Clinton',
        'title': 'Trump and Putin colluded!',
        'content': 'I should have won the election, but the Russian hackers helped Trump win!',
        'date_posted': 'September 28, 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.is_submitted():
        print("submitted")
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    print(form.errors)
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run()

