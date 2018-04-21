from moex_bot.calculation_of_levels import calculation
from moex_bot.filter_to_call import filters_to


# функция проверяет на касания ценой уровня, каждый день (интервал)
# возвращает список рекамендаций
def action(stock):
    # функция фильтер для сигнала дает low, high за прошлый день
    price_range = filters_to(stock)
    # функция калькулятор дает список уровней за прошедшую неделю
    price_livels_range = calculation(stock)
    # делим список на 2 для покупри и продажи
    buy_price = price_livels_range[:3]
    sale_price = price_livels_range[3:]

    buy_list = []
    sale_list = []

    # сравниваем значения и складываем в list
    if price_range[0] <= buy_price[2]:
        buy_list.append('Покупаем {} от {} на 20%'.format(stock, buy_price[0]))
    if price_range[0] <= buy_price[1]:
        buy_list.append('Покупаем {} от {} на 20%'.format(stock, buy_price[1]))
    if price_range[0] <= buy_price[0]:
        buy_list.append('Покупаем {} от {} на 20%'.format(stock, buy_price[2]))

    if price_range[1] >= sale_price[0]:
        sale_list.append('Продаем {} от {} на 20%'.format(stock, sale_price[0]))
    if price_range[1] >= sale_price[1]:
        sale_list.append('Продаем {} от {} на 20%'.format(stock, sale_price[1]))
    if price_range[1] >= sale_price[2]:
        sale_list.append('Продаем {} от {} на 20%'.format(stock, sale_price[2]))
    # обединяем строки через ';', при отсутствии совпадений выводим 'Ждем'
    return ('; '.join(sale_list) if sale_list else 'Сигнала для продажи {} нет'.format(stock),
            '; '.join(buy_list) if buy_list else 'Сигнала для покупки {} нет'.format(stock))


if __name__ == "__main__":
    wr = action(stock='GAZP')
    print(wr)
