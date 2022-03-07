# Exercise 7 Looping Statements.
# Page 60 Try it Yourself 4-3
# Use a for loop to print the numbers from 1 to 20 inclusive.

def number_for():
    for alpha in range(1, 21):
        print(alpha)

# number_for()

# Page 60 Try it Yourself 4-6
# Use the third argument of the range() function to make a list
# of the odd numbers from 1 to 20. Use a for loop to print each number.

def odd_for():
    for beta in range(1, 20):
        if beta%2 != 0:
            print(beta)

# odd_for()



# Page 60 Try it yourself 4-7
# Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.
def threebies():
    for charlie in range(3, 31, 3):
        if charlie % 3 == 0:
            print(charlie)

# threebies()


# Page 60 Try it yourself 4-8
# Make a list of the first 10 cubes (that is the cube of each integer from
# 1 through 10) and use a for loop to print out the value of each cube.

def cubes():
    for delta in range(1, 11):
        print(delta**3)

cubes()
