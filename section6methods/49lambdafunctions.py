
def square(n : int) -> int:
    return n**2

my_nums = [1,2,3,4,5,6,7,8,9]

print(list(map(square, my_nums)))

def even(n: int) -> int:
    return n%2 == 0

print(list(filter(even, my_nums)))

# simple lambda function example
print(list(map(lambda num: num ** 2, my_nums)))

