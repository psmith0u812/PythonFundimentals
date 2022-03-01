# Write a function called simple() Assign a diffrent message to 5
# variables and print each message.

def simple():
    """Agree with user"""
    print(bookname), 'Was my favorite too!'
def simple(name):
    """Simple greeting"""
    print("Hello!"+ name)

bookname = 'Count of Monte Cristo'
name = 'dave'
name2 = 'frank'
name3 = 'jill'
name4 = 'sarah'
name5 = 'Bob'

simple(name)
simple(name2)
simple(name3)
simple(name4)
simple(name5)

# Write a function called simple2(). Assign a message to a variable
# then print out that variable.
# Change the message and assign it to the
# variable again, but after the first print statement.
# Print the second message.
# Do these steps 2 more times. You should have 4 messages assigned
# to the same variable and 4 print functions showing the results.


def simple2():
    """print """
    print(duck)

duck = ('Mallard')
print(duck)
duck = ('Woodduck')
print(duck)
duck = ('Buffelhead')
print(duck)
duck = ('Pintail')

simple2()

# Write a function called message that takes 1 argument.
# Inside that function, write a print function that takes the argument.

def message(student):
    """Brief Message"""
    print("Welcome to class, " + student)

student = 'Bob'

message(student)

print(student)
