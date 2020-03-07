

def add(a, b):
    try:
        result = a + b
    except TypeError:
        print('incorrect type for one of the parameters')
    else:
        print('Add worked!')
        print(result)


number1 = 10
number2 = 20
number3 = "20"

add(number1, number2)
add(number1, number3)


def openfile():
    try:
        f = open('testfile', 'r')
        f.write("Write a test line")
    except TypeError:
        print("There was a type error!")
    except OSError:
        print('There is an OS Error')
    finally:
        print('I always run')

openfile()