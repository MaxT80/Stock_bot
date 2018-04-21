from moex_bot.db_moex import Prise
import csv

stock_list = ['AFLT', 'GAZP', 'SBER', 'MFON']


#  функция для записи данных в csv файл для отрисовки на сайте
def data_selection():
    #  в цикле проходит по списку акций
    for stock in stock_list:
        #  переменая которая содержит даные по акции
        prise = Prise.query.filter(Prise.secid == stock).order_by(Prise.tradedate.desc()).all()
        #  открываем файл для записи в формате csv
        with open('.\static\{}.csv'.format(stock), 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            #  в цикле перебераем данные по столбцам БД и записываем в csv
            for date_stock in prise:
                all_date_stock = (date_stock.tradedate, date_stock.secid,
                                  date_stock.value, date_stock.opens, date_stock.low,
                                  date_stock.high, date_stock.close)
                writer.writerow(all_date_stock)


if __name__ == "__main__":
    data_selection()

"""

#User.query.filter(User.last_name.like('%ов%'))
       # .order_by(User.first_name).all()  # обьединение методов

date_stock = Prise.query.order_by(Prise.tradedate).all()  # сортировка по возрастанию
# date_stock_revers = Prise.query.order_by(Prise.tradedate.desc()).all()  # сортировка по убыванию

# выводим значение столбца в списочным вырожением
data_date_stock = [row.tradedate for row in Prise.query.all()]
data_value_stock = [row.value for row in Prise.query.all()]
data_open_stock = [row.opens for row in Prise.query.all()]
data_low_stock = [row.low for row in Prise.query.all()]
data_high_stock = [row.high for row in Prise.query.all()]
data_close_stock = [row.close for row in Prise.query.all()]

print(date_stock)
# print(data_value_stock)
"""
