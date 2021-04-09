import sys


def nums_generator(*args):
    tutors = list(args[0])
    klasses = list(args[1])
    for row_1, row_2 in zip(tutors, klasses):

        while len(tutors) > len(klasses):
            klasses.append(None)

        else:

            yield row_1, row_2
    return 'Генератор пуст'


num_gen = nums_generator(['Евгений', 'Алексей', 'Ирина', 'Сергей', 'Ольга', 'Александр', 'Петр', 'Татьяна'],
                         ['8В', '9Б', '10А', '9В', '10В', '7А'])
print(type(num_gen))  # проверяем что функция является генератором
print(next(num_gen), '\n', next(num_gen), '\n', next(num_gen), '\n',
      next(num_gen), '\n', next(num_gen), '\n', next(num_gen), '\n',
      next(num_gen), '\n', next(num_gen), '\n', next(num_gen), '\n')
# print(next(num_gen)) если раскомментировать строку, можно убедиться, что генератор пуст
