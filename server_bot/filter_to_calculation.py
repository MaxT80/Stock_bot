from db_moex import Prise

name = ['AFLT', 'GAZP', 'SBER', 'MFON']


# показывает значения недельной свечи low, high, close делаеться в субботу
def filter_to(name):
    # запрос в БД по срезу за 5 последних дней (неделя)
    prise = Prise.query.filter(Prise.secid == name).order_by(Prise.tradedate.desc())[5:10]
    # в цикле списочного выражения достает из столбца low значения, выводит min
    price_low_stock = min([row.low for row in prise])
    # в цикле списочного выражения достает из столбца high значения, выводит max
    price_high_stock = max([row.high for row in prise])
    # в цикле списочного выражения достает из столбца close значения последнего дня
    price_close_stock = [row.close for row in prise]

    return price_low_stock, price_high_stock, price_close_stock[0]


if __name__ == "__main__":
    ee = filter_to(name='GAZP')
    print(ee)
