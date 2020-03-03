mySet = set()

print(mySet)
print(type(mySet))

mySet.add('fred')
print(mySet)

mySet2 = {1, 4, 'f'}
print(type(mySet2))
print(mySet2)

print(mySet2.union(mySet))

mySetA = {'a', 'b', 'c', 'd', 'e'}
mySetB = {'f', 'b', 'g', 'd', 'h', 'd'}

print(mySetA)
print(mySetA.union(mySetB))
print(mySetA.intersection(mySetB))

