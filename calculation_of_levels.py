import csv
import os


# расчет уровней за прошедшую неделю, происходит динамически на сайте из статических данных
def calculation(stock):
    #  открываем файл csv для чтения, дастаем данные
    with open('.\static\{}_prise.csv'.format(stock), 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            # преобразует строковые данные из csv файла в числовые
            list_prise = list(map(float, row))
            # расчет центрального уровня
            central_level = round(((list_prise[1] + list_prise[0] + 2 * list_prise[2]) / 4), 1)
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
    ee = calculation(stock='GAZP')
    print(ee)
# print(os.path.relpath('calculation_of_levels.py', start='moex_bot'))