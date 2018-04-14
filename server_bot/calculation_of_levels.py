from moex_bot.server_bot.filter_to_calculation import filter_to


# расчет уровней за прошедшую неделю делаеться в субботу
def calculation(name):
    list_prise = filter_to(name)
    # расчет центрального уровня
    central_level = round(((list_prise[0] + list_prise[1] + 2 * list_prise[2]) / 4), 1)
    # расчет поддержок
    support_level_1 = round((2 * central_level - list_prise[1]), 1)
    support_level_2 = round((central_level - list_prise[1] + list_prise[0]), 1)
    support_level_3 = round((support_level_1 + list_prise[0] - list_prise[1]), 1)
    # расчет сопративлений
    resistance_level_1 = round((2 * central_level - list_prise[0]), 1)
    resistance_level_2 = round((central_level + list_prise[1] - list_prise[0]), 1)
    resistance_level_3 = round((resistance_level_1 + list_prise[1] - list_prise[0]), 1)

    return support_level_3, support_level_2, support_level_1, \
           resistance_level_1, resistance_level_2, resistance_level_3


if __name__ == "__main__":
    rr = calculation(name='GAZP')
    print(rr)
