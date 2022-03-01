print("Hello World")
# Can you make a typo that generates an error?
# Yes, changing or removing correct syntax will generate an error.
# print('Hello World)

# Can you make sense of the error message?
# Yes, Error Message displayed in the terminal hints at the potential problem.
# Terminal: SyntaxError: unterminated string literal (detected at line 11)

# Can you make a typo that doesn't generate an error?
# Yes, print('Hhello World')

# why do you think it didn't make an error?
# Because that particular typo had nothing to do with syntax.
# most syntax related errors will be reported in the terminal

# Zen of Python principles checked by Python, Path, String, CategoryInfo,
# Object, Command, FullyQualifiedErrorId

# Assign a message to a variable and then print that message
message = "This is a change of the message testing variables and messages"
print(message)

# Assign a message to a variable and print that message. Then change
# the value of the variable to a new message, and print the new message.
# Original message "This is a test of variables and messages"


def display_message():
    """print chapter topics"""
    print("This chapter is about functions and arguments")


display_message()


def favorite_book():
    """Prints a brief book related message"""
    print("One of my favorite books is Alice in Wonderland.")

favorite_book()
