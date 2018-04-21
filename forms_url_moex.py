from datetime import datetime, timedelta
from moex_bot.connect import connect_moex


#  функция формирует url и возвращает данные через функцию соединения
def url_moex(number_days, stock):
    date_today = datetime.now()
    # переводит дату в строку
    date_till = datetime.strftime(date_today, '%Y-%m-%d')
    # вычисляет разницу между двумя датами
    delta_period = date_today - timedelta(days=number_days)
    # переводит дату в строку
    date_from = datetime.strftime(delta_period, '%Y-%m-%d')
    url = 'https://iss.moex.com/iss/history/engines/stock/markets/shares/boards/TQBR/securities/{}/.json?from={}&till' \
          '={}&interval=24&start=0'.format(stock, date_from, date_till)
    return connect_moex(url)


if __name__ == "__main__":
    url_moex()


# res = url_moex(number_days=120, stock='AFLT')
# print(res)
