import re
from moex_bot.call_to_action import action

stock_list = ['AFLT', 'GAZP', 'SBER', 'MFON']


# функция формируем список рекомендайий по списку акций
def list_to():
    list_email = []
    # перебераем акции из списка
    for stock in stock_list:
        # получаем для акции рекомендации из функции action()
        lists = action(stock)
        # складываем общий рекомендации в общий список ввиде словаря
        list_email.append('Рекомендация по {} на сегодня: {}'.format(stock, lists))
    # в цикле регулярным выражением заменяет скодки справо и слево на пробелы
    clean_list_email = []
    for row in list_email:
        clean_list_email.append(re.sub(r'\(|\)', '', row))

    return clean_list_email


if __name__ == "__main__":
    eee = list_to()
    print(eee)
