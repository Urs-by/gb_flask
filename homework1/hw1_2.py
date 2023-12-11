#Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна
# (шапка, меню, подвал), и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/dress')
def dress():
    return render_template('dress.html')

@app.route('/shoes')
def shoes():
    return render_template('shoes.html')

@app.route('/accessories')
def accessories():
    return render_template('accessories.html')

if __name__ == '__main__':
    app.run(debug=True)

