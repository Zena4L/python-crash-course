myList =[]
for value in range(1,11):
    square = value**2
    myList.append(square)

print(myList)
print(min(myList))
print(max(myList))
print(sum(myList))

list2 = [1,2,3,4,5]
list3 = list2[:]
print(list3)