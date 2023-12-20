from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from forms import LoginForm
from flask_sqlalchemy import SQLAlchemy
from models import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'GeekBrains$ecretKey'
csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdatabase.sqlite'
db.init_app(app)


@app.route('/')
@app.route('/index3.html')
def index():
    return render_template('index3.html')


@app.route('/registration', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        if not User.query.filter(User.username == username).all():
            email = form.email.data
            password = form.password.data
            user = User(username=username, email=email, password=password)
            db.session.add(user)
            db.session.commit()
            message = " Вы успешно зарегистрированы"
            return render_template('index3.html', form=form, username=username, message=message)
        else:
            message = " Вы уже зарегистрированы в нашей ситсеме"
            return render_template('index3.html',  username=username, message=message)

    return render_template('registration.html', form=form)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')