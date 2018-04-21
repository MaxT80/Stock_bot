import csv
from moex_bot.db_moex import Prise

stock_list = ['AFLT', 'GAZP', 'SBER', 'MFON']


# записывает значения недельной свечи low, high, close, работает 1 раз в субботу
def filter_to():
    #  в цикле проходит по списку акций
    for stock in stock_list:
        # запрос в БД по срезу за 5 последних дней (неделя)
        prise = Prise.query.filter(Prise.secid == stock).order_by(Prise.tradedate.desc())[:5]
        # в цикле списочного выражения достает из столбца low значения, выводит min
        price_low_stock = min([row.low for row in prise])
        # в цикле списочного выражения достает из столбца high значения, выводит max
        price_high_stock = max([row.high for row in prise])
        # в цикле списочного выражения достает из столбца close значения последнего дня
        price_close_stock = [row.close for row in prise]
        #  открываем файл для записи в формате csv для каждого stock отдельно
        with open('.\static\{}_prise.csv'.format(stock), 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            #  передаем в переменую нужные значения и записываем ее в csv
            prise_stock = (price_low_stock, price_high_stock, price_close_stock[0])
            writer.writerow(prise_stock)


if __name__ == "__main__":
    filter_to()
