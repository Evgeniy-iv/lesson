from time import perf_counter
from sys import getsizeof

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# используем List Comprehensions
start = perf_counter()
t1_start = perf_counter()
start = perf_counter()
src_list = [i for i in src[1:] if i > src[src.index(i) - 1]]
t1_stop = perf_counter()

# используем генератор
t2_start = perf_counter()
src_generator = (i for i in src[1:] if i > src[src.index(i) - 1])
src_generator_list = list(src_generator)
t2_stop = perf_counter()



print(type(src_list), getsizeof(src_list))
print(src_list, t1_stop-t1_start)


print(type(src_generator), getsizeof(src_generator))
print(src_generator_list, t2_stop-t2_start)
