from flask import Flask, render_template, abort

flask_app = Flask(__name__)
stock_list = ['AFLT', 'GAZP', 'SBER', 'MFON']


@flask_app.route('/')
def index():
    return render_template('index.html')


@flask_app.route('/<name>_info')  # имя прописано в ссылке в index.html и передаеться в шаблон
def stock_info(name):
    if name not in stock_list:  # имя сравнивает из списка если нет, выдает ошибку
        abort(404)

    return render_template('stock_info_moex.html',
                           title='Sock  {}'.format(name), link='{}  Chart'.format(name),
                           name=name,
                           support=220, resistance=190,
                           stop=3)


@flask_app.route('/<name>_chart')  # имя для ссылки подтягивает из выражения name=name в предыдушей станицы
def stock_chart(name):
    if name not in stock_list:
        abort(404)

    return render_template('stock_chart_moex.html',
                           data_link='/static/{}.csv'.format(name),
                           title_name='{} stock MOEX'.format(name), name=name,
                           support=220, resistance=190)


if __name__ == "__main__":
    flask_app.run(debug=True)
