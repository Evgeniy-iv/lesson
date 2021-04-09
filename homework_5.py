src = [2, 2, 2, 7, 8, 12, 4, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


un_number_set = set()
#  реализуем в виде строкового включения
unique_list = [x for x in src if x not in un_number_set and (un_number_set.add(x) or True)]

#  тоже самое, но в виде генератора
un_number_set_1 = set()
unique_generator = (x for x in src if x not in un_number_set_1 and (un_number_set_1.add(x) or True))

print(unique_list, type(unique_list))

print(list(unique_generator), type(unique_generator))

