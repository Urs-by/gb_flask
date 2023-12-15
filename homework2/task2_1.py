# 📌 Создать страницу, на которой будет форма для ввода имени и возраста пользователя и кнопка "Отправить"
# 📌 При нажатии на кнопку будет произведена проверка возраста и переход на страницу с результатом или
# на страницу с ошибкой в случае некорректного возраста.

from flask import Flask, render_template, request, flash, redirect, url_for, make_response, session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.get('/task2_1')
def task1():
    return render_template('task2_1.html')


@app.post('/task2_1')
def send_name():
    username = request.form.get('username')
    age = request.form.get('age')

    if age.isdigit() and 10 <= int(age) <= 110:
        if 10 <= int(age) <= 20:
            message = "Вы очень юны!"
        elif 21 <= int(age) <= 40:
            message = "Вы уже кое-что видели!"
        elif 41 <= int(age) <= 60:
            message = "Да вы многое уже повидали!"
        elif 61 <= int(age) <= 90:
            message = "Как быстро летит время...."
        else:
            message = "Вы поняли этот мир..."
        return render_template('task2_1.html', age=age, username=username, message=message)

    return render_template('task2_1.html', error='Вы ввели некорректный возраст, попробуйте еще раз!')




@app.get('/task2_2')
def task2():
    return render_template('task2_2.html')


@app.post('/task2_2')
def square():
    num = request.form.get('number')
    try:
        if float(num):
            result = float(num) ** 2
            return render_template('/task2_2.html', num=num, result=result)
    except:
        return render_template('/task2_2.html', error='Вы ввели не число, попробуйте еще раз')


@app.route('/task2_3')
def task3():
    return render_template('task2_3.html')


@app.post('/task2_3')
def flash_name():
    if not request.form.get('username'):
        flash('Необходимо ввести имя!', 'danger')
        return redirect(url_for('flash_name'))
    username = request.form.get('username')
    flash(f"Привет, {username} !", 'success')
    return render_template('/task2_3.html', username=username)


@app.route('/task2_4')
def task4():
    return render_template('task2_4.html')


@app.post('/cookie')
def del_cookie():
    response = make_response(render_template('/task2_4.html', cook="Cookie удалены!"))
    response.set_cookie('name', expires=0)
    return response


@app.post('/task2_4')
def cookie_write():
    if not (request.form.get('username') and request.form.get('email')):
        flash('Необходимо заполнить все поля!', 'danger')
        return redirect(url_for('cookie_write'))
    username = request.form.get('username')
    response = make_response(render_template('/hellochel.html', username=username))
    response.set_cookie('name', username)
    # session['1'] = [username, email]
    return response
