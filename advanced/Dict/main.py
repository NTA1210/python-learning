my_dict = {"name": "Max", "age": 28, "city": "Boston"}
print(my_dict)

my_dict2 = dict(name="Max", age=28, city="Boston")
print(my_dict2)

my_dict3 = dict([('name', 'Max'), ('age', 28), ('city', 'Boston')])
print(my_dict3)

if 'age' in my_dict:
    print("age is in the dict")

for key in my_dict:
    print(key, my_dict[key])

mydict_cpy = my_dict.copy()
print(mydict_cpy)

mydict_cpy2 = dict(my_dict)
print(mydict_cpy2)

mydict_cpy3 = {**my_dict}
print(mydict_cpy3)