from datetime import datetime
from moex_bot.server_bot.db_moex import Stock
from moex_bot.server_bot import url_moex


#  функцие принимает данные для формирует словарь
def filter_data(data):
    information_list = []
    for value in data['history']['data']:
        # переводим строку в формат время
        value[1] = datetime.strptime(value[1], '%Y-%m-%d')
        # по уникальному имени связываем данные и дабавляем в словарь
        secid_name = Stock.query.filter(Stock.stock_name == value[3]).first()
        information_list.append({'tradedate': value[1],
                                 'secid': value[3],
                                 'value': value[5],
                                 'opens': value[6],
                                 'low': value[7],
                                 'high': value[8],
                                 'close': value[9],
                                 'stock_ticker_id': secid_name.id})

    return information_list


if __name__ == "__main__":
    result = filter_data(url_moex(number_days=6, stock='AFLT'))
    print(result)

    """
    data = url_moex(number_days, stock)
    передаем в функцию filter_data() данные полученые спомощью функции url_moex()
    ввиде функции за один день по инструменту AFLT
    """
