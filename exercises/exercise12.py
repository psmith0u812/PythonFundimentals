# Exercise 12 Exception Handling

# 10-6 & 10-7
#while True:
    #val1 = input('Enter a number ')
    #if val1 == str:
        #break
    #val2 = input('Enter a second Number ')
    #if val2 == str:
        #break

    #try:
        #charlie = int(val1) + int(val2)
        #print(f'The answer is {charlie}')

    #except ValueError:
        #print('Not a correct value for number ')


# 10-8, 10-9
file1 = 'cats.txt'
file2 = 'dogs.txt'


print('Cats: ')
try:
    with open(file1, encoding='utf-8') as f:
        text = f.read()
except FileNotFoundError:
    pass
    # print(f'Sorry we\'re unable to locate {file1}')
else:
    print(text)

print('Dogs: ')
try:
    with open(file2, encoding='utf-8') as f:
        text = f.read()
except FileNotFoundError:
    pass
    # print(f'Sorry we\'re unable to locate {file2}')
else:
    print(text)




