def name_of_function(name: str):
    '''
    DOCSTRING: Information about the function
    INPUT: name
    OUTPUT: Hello ...
    '''
    print("Hello " + name)

help(name_of_function)
name_of_function("Jose")

def name_function():
    print("Hello")

name_function()

def say_hello(name: str = 'NAME'):
    print("hello " + name)

say_hello()
say_hello('John')


# function that takes a string and returns a string
def say_hello(name: str = 'NAME') -> str:
    return 'hello ' + name

result = say_hello("Jose")
print(result)

# function with an arbitrary number or arguments.  use the '*' in front of the argument name
# and the args value will be a tuple with all the values passed to the function
def myfunc(*args : float) -> float:
    for item in args:
        print(item)
    return sum(args) * 0.05

print(myfunc(10,20,30,1,4,5,5,6))


# function with an arbitratry number of named arguments, use '**kwargs'.  kwargs will contain 
# a dictionary where the key is the name of the argument and the value is the value of that argument
def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

myfunc(fruit='apple', veggie='carrot')

# it is possible to combine *args and **kwargs
def myfunc(*args, **kwargs):
    print('I would like {} {}'.format(args[0],kwargs['food']))


myfunc(10, food='burgers')


def myfunc(astring):
    returnStringArray = []
    x = 0;
    for c in astring:
        if x%2 == 0:
            returnStringArray.append(c.upper())
        else:
            returnStringArray.append(c.lower())
        x += 1
    print(''.join(returnStringArray))

myfunc('abcdef')