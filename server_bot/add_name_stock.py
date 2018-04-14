from moex_bot.server_bot.db_moex import db_session, Stock

stock_list = ['AFLT', 'GAZP', 'SBER', 'MFON']


# функция добовляет список инструментов в базу данных
def add_name():
    for a in stock_list:
        stocks = Stock(a)
        db_session.add(stocks)

    db_session.commit()


if __name__ == "__main__":
    add_name()

'''
s = Stock

datas = s.query.all()
data = s.query.filter(s.stock_name == 'SBER').all()
sber_bank = s.query.filter(s.stock_name == 'SBER').first()

for row in Prise.query.all():  # выводим значение столбца 'tradedate' в цикле
    print(row.tradedate)

# выводим значение столбца 'tradedate' списочным вырожением
# date_auction_stock = [row.tradedate for row in PriseAFLT.query.all()]


# print(datas)
# print(data)
# print(sber_bank.id)
# print(dates_stock)
# print(date_stock_revers)
'''
