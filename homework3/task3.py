from flask import Flask, render_template,request
from flask_wtf.csrf import CSRFProtect
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'GeekBrains$ecretKey'
csrf = CSRFProtect(app)


@app.route('/')
@app.route('/index3.html')
def index():
    return render_template('index3.html')


@app.route('/registration', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        lastname = form.lastname.data
        email = form.email.data
        password = form.password.data
        print(username, lastname, email, password)
    return render_template('registration.html', form=form)

