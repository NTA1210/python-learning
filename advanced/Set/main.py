my_set: set[int] = {1, 2, 3, 4, 5, 5, 5, 5, 5, "asd"}
print(my_set)

my_set2: set[int] = set([1, 2, 3, 4, 5, "acb"])
print(my_set2)

if 1 in my_set:
    print("1 is in the set")

my_set2.add(6)
print(my_set2)

my_set2.remove(6)
print(my_set2)

my_set2.discard(6)
print(my_set2)

my_set2.pop()
print(my_set2)

for i in my_set2:
    print(i)

char_set = set("hello world")
print(char_set, len(char_set))


odds: set[int] = {1, 3, 5, 7, 9}
evens: set[int] = {2, 4, 6, 8, 10}

print(odds.union(evens))

set1: set[int] = {1, 2, 3, 4, 5}
print(set1.intersection({1, 2, 3, 8, 9}))

set1.update([6, 7, 8, 9, 10])
print(set1)

print(set1.difference({1, 2, 3, 4, 5}))
print(set1.symmetric_difference({1, 2, 3, 4, 5}))
