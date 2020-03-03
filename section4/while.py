x = 0

while x < 5:
    print(f'The current value of x is {x}')
    x += 1
else:
    print('x is not less than 5')


# break: break out of the current closest enclosing loop
# continue: goes to the top of the closest enclosing loop
# pass: does nothing at all - this is mainly used to fill in a place where node is needed, but you don't yet implement it!

x = [1,2,3]

for item in x:
    pass

print('end of my script')

myString = 'Sammy'

for letter in myString:
    if letter == 'a':
        continue
    print(f'Letter is {letter}')


for letter in myString:
    if letter == 'a':
        break
    print(f'Letter is {letter}')


x = 0

while x < 5:
    if x == 2:
        break
    print(x)
    x += 1