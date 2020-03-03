
my_dictionary = { 'id': 12345, 'value': 2.99}

print(type(my_dictionary))
print(my_dictionary.get('id'))

print(my_dictionary)
my_dictionary['k3'] = 'fred'
print(my_dictionary)
my_dictionary['id'] = 'an id'
print(my_dictionary)
print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.items())


myDictionary2 = {
    'id': 123456,
    'person' : {
        'first': 'John',
        'surname': 'Doe'
    }
}

print(myDictionary2)
print(myDictionary2['person']['first'])