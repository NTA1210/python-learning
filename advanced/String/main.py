string = "hello world"
print(string)


string = "hello\nworld"
print(string)

string1 = "hello"
string2 = "world"
print(string1 + " " + string2)

print(string1 * 3)

print(string1[0:5])

print(string1[::2])


string = "Python Programming"
print(string.upper())
print(string.lower())
print(string.title())
print(string.capitalize())
print(string.swapcase())
print(string.replace("Python", "Java"))

string = "  hello world  "
print(string.strip())
print(string.lstrip())
print(string.rstrip())


string = """
hello 
    world
"""
print(string)

# %, .format(), f-string
name = "John"
age = 30
print("Name: %s, Age: %d" % (name, age))
print("Name: {}, Age: {}".format(name, age))
print(f"Name: {name}, Age: {age}")