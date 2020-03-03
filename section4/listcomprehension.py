myString = 'Hello World'

myStringList = []

for letter in myString:
    myStringList.append(letter)

print(myStringList)

# achieve the samething using list comprehensions
myStringList2 = [letter for letter in myString]
print(myStringList2)


myList = [num**2 for num in range(0,100)]
print(myList)

myList = [num**2 for num in range(0,100) if num%2 == 0]
print(myList)


celcius = [0,10,20,34.5]

fahrenheit = [(9/5*temp + 32) for temp in celcius]
print(fahrenheit)


# embedded loops
myList = []

for x in range(0,10,2):
    for y in range(0,1000,100):
        myList.append(x*y)

print(myList)

myList = [x * y for x in range(0,10,2) for y in range(0,1000,100)]
print(myList)
