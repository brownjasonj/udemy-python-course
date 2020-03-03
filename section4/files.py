myfile = open('myfile.txt')

file: str = myfile.read()

print(file)

with open('myfile.txt', mode='r') as my_new_file:
    fileLines = my_new_file.readline()
    print(fileLines)

with open('myfile.txt', mode='a') as f:
    f.write("this is another line\n")

# open and create a file if it doesn't exist
with open("abcded.txt", mode='w') as f:
    f.write("I created this file!")

with open('abcded.txt', mode='r') as f:
    print(f.read())




