my_list = [1,2,3,4,5,6,7,8,9,10]

for item in my_list:
    print(item)


for num in my_list:
    # Check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')

list_sum : int = 0

for num in my_list:
    list_sum = list_sum + num
    print(list_sum)

my_string : str = 'Hello World'

for letter in my_string:
    print(letter)

# tuple iterbales
tup = (1,2,3)

for tup_item in tup:
    print(tup_item)

my_tup_list = [(1,2),(3,4),(5,6),(7,8)]

for item in my_tup_list:
    print(item)

# tuple unpacking with iterable
for (a,b) in my_tup_list:
    print(a)
    print(b)

# you can even remove the parentheses 
for a,b in my_tup_list:
    print(a)
    print(b)


myTripleTupList  = [(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
for a,b,c in myTripleTupList:
    print(a)
    print(b)
    print(c)

for item in myTripleTupList:
    a,b,c = item
    print(item)
    print(a)
    print(b)
    print(c)


# objects and iterables
my_object = {
    'firstname': 'fred',
    'secondname': 'jones'
}

for key in my_object.keys():
    print(key)

for value in my_object.values():
    print(value)

print(my_object.popitem())
print(my_object.popitem())
print(my_object)

myObjectList = [{'k1':1},{'k2':2},{'k3':3}]

for item in myObjectList:
    print(item)
    for k,v in item.items():
        print(f'Key {k} has value {v}')


myObject = {'k1':1,'k2':2,'k3':3}

for value in myObject.values():
    print(value)

for key,value in myObject.items():
    print(f'Key {key} has value {value}')
