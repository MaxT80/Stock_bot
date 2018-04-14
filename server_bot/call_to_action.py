from moex_bot.server_bot.db_moex import Prise
from moex_bot.server_bot.calculation_of_levels import calculation


# проверка на касания уровня каждый день (интервал)
def action(name):
    # запрос в БД за вчерашний днь
    prise = Prise.query.filter(Prise.secid == name).order_by(Prise.tradedate.desc())[2:3]
    # дастаем из столбца БД значения low, high за вчерашний днь
    price_low_stock = [row.low for row in prise]
    price_high_stock = [row.high for row in prise]
    # функция калькулятор дает список уровней за прошедшую неделю
    price_range = calculation(name)
    # делим список на уровни дла покупри и продажи
    buy_line = price_range[:3]
    line_sale = price_range[3:]
    print(price_low_stock[0])
    print(price_high_stock[0])
    print(buy_line)
    print(line_sale)

    # проверка на касания уровня ценой

    if price_low_stock[0] <= buy_line[0]:
        return 'Покупаем от {}'.format(buy_line[0])
    if price_low_stock[0] <= buy_line[1]:
        return 'Покупаем от {}'.format(buy_line[1])
    if price_low_stock[0] <= buy_line[2]:
        return 'Покупаем от {}'.format(buy_line[2])
    s = []
    if price_high_stock[0] >= line_sale[0]:
        s.append('Продаем от {}'.format(line_sale[0]))
    if price_high_stock[0] >= line_sale[1]:
        s.append('Продаем от {}'.format(line_sale[1]))
    if price_high_stock[0] >= line_sale[2]:
        s.append('Продаем от {}'.format(line_sale[2]))

    return '; '.join(s) if s else 'Ждем'


if __name__ == "__main__":
    wr = action(name='GAZP')
    print(wr)
