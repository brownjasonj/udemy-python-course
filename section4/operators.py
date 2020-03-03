myList = [1,2,3]

# number generator 'range(start, stop, step)'
for num in range(0,11,2):
    print(num)


# the following is quite common kind of code with indicies
index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count += 1

# you can use enumerate
word = 'abcde'

for item in enumerate(word):
    print(item)

for index,letter in enumerate(word):
    print(f'Letter at index {index} is {letter}')


# zip function
myList1 = [1,2,3]
myList2 = ['a','b','c']

for item in zip(myList1, myList2):
    print(item)


myList3 = [100,200,300]
for item in zip(myList1, myList2, myList3):
    print(item)


print(list(zip(myList1, myList2, myList3)))


# the 'in' operator can be used to check 'in'-ness with list, strings and dictionaries

print('x' in ['x','y','z'])
print('w' in 'a world')
print('k1' in {'k1':2})

