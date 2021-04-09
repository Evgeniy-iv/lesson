import sys

def nums_generator(max_num):
    for num in range(1, max_num+1):
        yield  num


num_gen = nums_generator(15)
print(type(num_gen))
print(next(num_gen))
print(next(num_gen))
print(next(num_gen))
# если выводим в виде списка, то видим, что список начинается с того места где остановился генератор
print(list(num_gen))