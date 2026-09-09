import sys
import timeit

my_tuple = (1, 2, 3, 4, 5)

my_list = list(my_tuple)
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)

print(sorted(my_tuple))
print(type(my_tuple))

info_tuple = "Max", 28, "Boston"
name, age, city = info_tuple
print(name)
print(age)
print(city)

number_tuple = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

i1, *i2, i10 = number_tuple
print("i1: ", i1)
print("i2: ", i2)
print("i10: ", i10)


print("Size of tuple: ", sys.getsizeof(my_tuple), 'bytes')
print("Size of list: ", sys.getsizeof(my_list), 'bytes')


print("List: ", timeit.timeit(lambda: [x * 2 for x in range(1000)], number=10000))
print("Tuple: ", timeit.timeit(lambda: tuple(x for x in range(1000)), number=10000))