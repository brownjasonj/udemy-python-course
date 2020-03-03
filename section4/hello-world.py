print('hello world!')

myHeight: int = 1

myString : str = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p'
subString1 : str = myString[1:len(myString):2]
print(subString1)
# get the substring start from character 4 to the end
subString1 = myString[4:]
print(subString1)
# get the substring starting from the beginng up to the last character, but not including,
subString1 = myString[:-1]
print(subString1)
# get the substring starting from beginning, to the end
subString1 = myString[:]
print(subString1)
# weird.  get substring starting from the begiining, to the end with -1 step.  This in fact reverses the string!
subString1 = myString[::-1]
print(subString1)


