myList: list[int | str] = [0, 1, "two"]
print(myList.count(0))

if 0 in myList:
    print("0 is in the list")

myList.append(4)
print(myList)