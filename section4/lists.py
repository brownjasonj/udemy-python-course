from typing import List
myList : List[int] = [1, 2, 3]

print(myList)
print(type(myList))

myStringList : List[str] = ['one', 'two', 'three']
myStringList2 : List[str] = ['four', 'five']

print(myStringList[1:-1])
print(myStringList + myStringList2)

myStringList.append('six')
print(myStringList)

poppedItem : str = myStringList.pop()
print(myStringList)
print(poppedItem)

poppedItem = myStringList.pop(0)
print(myStringList)
print(poppedItem)

myStringList.sort()
print(myStringList)
