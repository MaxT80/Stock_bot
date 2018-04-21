from moex_bot.db_moex import db_session, Prise
from moex_bot.filter_data_moex import filter_data
from moex_bot.forms_url_moex import url_moex

stock_list = ['AFLT', 'GAZP', 'SBER', 'MFON']
# запись даных в субботу за прошедшую неделю
number_days = 5


#  функция добавляет даные по инструментам из списка за выбранное количество деней в базу данных
def add_history_days():
    for stock in stock_list:
        data = url_moex(number_days, stock)

        for data_secid in filter_data(data):
            table_data = Prise(data_secid['tradedate'], data_secid['secid'],
                               data_secid['value'], data_secid['opens'],
                               data_secid['low'], data_secid['high'],
                               data_secid['close'], data_secid['stock_ticker_id'])
            db_session.add(table_data)

        db_session.commit()


if __name__ == "__main__":
    add_history_days()
