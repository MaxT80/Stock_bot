from datetime import datetime
from flask import render_template, abort

from core import flask_app
from calculation_of_levels import calculation

stock_list = ['AFLT', 'GAZP', 'SBER', 'MFON']


@flask_app.route('/')
def index():
    return render_template('index.html', clock=datetime.strftime(datetime.now(), '%A, %d %B %Y %H:%M'))


@flask_app.route('/<name>_info')  # имя прописано в ссылке в index.html и передаеться в шаблон
def stock_info(name):
    if name not in stock_list:  # имя сравнивает из списка если нет, выдает ошибку
        abort(404)
    levels = calculation(name)  # функция вычесляет уровни срабатывает при открытии страницы
    return render_template('stock_info_moex.html', clock=datetime.strftime(datetime.now(), '%A, %d %B %Y %H:%M'),
                           title='Sock  {}'.format(name), link='{}  Chart'.format(name),
                           name=name, support_1=levels[2], support_2=levels[1], support_3=levels[0],
                           resistance_1=levels[3], resistance_2=levels[4], resistance_3=levels[5],
                           stop=3)


@flask_app.route('/<name>_chart')  # имя для ссылки подтягивает из выражения name=name в предыдушей станицы
def stock_chart(name):
    if name not in stock_list:
        abort(404)
    levels = calculation(name)
    return render_template('stock_chart_moex.html',
                           data_link='/static/{}.csv'.format(name),
                           title_name='{} stock MOEX'.format(name), name=name,
                           support_1=levels[2], support_2=levels[1], support_3=levels[0],
                           resistance_1=levels[3], resistance_2=levels[4], resistance_3=levels[5])


if __name__ == "__main__":
    flask_app.run(debug=True)
