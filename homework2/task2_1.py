# 📌 Создать страницу, на которой будет форма для ввода имени и возраста пользователя и кнопка "Отправить"
# 📌 При нажатии на кнопку будет произведена проверка возраста и переход на страницу с результатом или
# на страницу с ошибкой в случае некорректного возраста.

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/task2_1')
def task1():
    return render_template('task2_1.html')


@app.post('/task2_1')
def send_name():
    uname = request.form.get('username')
    age = request.form.get('age')
    print(uname, age)
    if age.isdigit() and 10 <= int(age) <= 110:
        return render_template('task2_1.html', age=age, uname=uname)
    error = 'Некорректный возраст'
    return render_template('task2_1.html', error=error)


@app.route('/task2_2')
def task2():
    return render_template('task2_2.html')


@app.route('/task2_3')
def task3():
    return render_template('task2_3.html')


@app.route('/task2_4')
def task4():
    return render_template('task2_4.html')
