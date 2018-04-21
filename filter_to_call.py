from moex_bot.db_moex import Prise


# функция формирует значения low, high за вчерашний днь
def filters_to(stock):
    # запрос в БД за вчерашний день
    prise = Prise.query.filter(Prise.secid == stock).order_by(Prise.tradedate.desc())[:1]
    # дастаем из столбца БД значения low, high за вчерашний днь
    price_low_stock = [row.low for row in prise]
    price_high_stock = [row.high for row in prise]

    return price_low_stock[0], price_high_stock[0]


if __name__ == "__main__":
    wg = filters_to(stock='GAZP')
    print(wg)
