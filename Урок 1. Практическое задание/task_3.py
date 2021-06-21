"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух) разной!! сложности
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

dict_base = dict(mimi='153445323', long='4455855685', cimi='45464674564', strong='15496265648451', down='1548946161564',
         viki='154946263558484', dowson='5494946156484')


def max_3_1(lst):
    for i in range(len(lst)):
        low_ind = i
        for j in range(i + 1, len(lst)):
            if lst[j][1] > lst[low_ind][1]:
                low_ind = j
            lst[i], lst[low_ind] = lst[low_ind], lst[i]
    return lst[0:3]

list_dict = list(dict_base.items())
for i in max_3_1(list_dict):
    print(i[0], ':', i[1])
print('Сложность O(n**2)')


def max_3_2(dict):
    in_max = {}
    for i in range(3):
        maxi = max(dict.items(), key=lambda k_v: k_v[1])
        del dict[maxi[0]]
        in_max[maxi[0]] = maxi[1]
    return in_max

print(max_3_2(dict_base))
print('Сложность O(n)')
print('Самое эффективное решение, так, как самая низкая сложность "линейная"')

list_dict = list(dict_base.items())
list_dict.sort(key=lambda i: i[1], reverse=True)
for i in range(3):
    print(list_dict[i][0], ':', list_dict[i][1])
print('Сложность O(n log n)')
