# Try it yourself Bood assignment page25
# 2.3 Personal Message: Use a variable to represent a person's name, and print a message
# your message should be simple, such as "Hello Eric, would you like to learn some Python today?"

message = 'Hello {0}, would you like to learn some Python today?'
name = 'Eric'
print(message.format(name))


# 2-4 Name cases: Use a variable to represent a person's name, then print that persons name
# lower case. upper case, and Title case

student = 'John Doe'

print(student.upper())
print(student.lower())
print(student.title())

# 2-5 Famous Quote: Find a quote from a famous person you admire Print
# the quote and the name of its author. Your output should look something
# like the following Including quotation marks:
#     Albert Einstein once said, "A person who never made a
#     mistake never tried anything new."

# quote = '\tNelson Mandela once said, \"It always seems impossible \n\tuntil it\'s done\"'

# print(quote)

# 2-6 Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person's
# name using a variable called famous_person. then compose your message
# and represent it with a new variable called message. Print your message.


message = '\t{0} once said, \"It always seems impossible \n\tuntil it\'s done\"'
famous_person = 'Nelson Mandela'

print(message.format(famous_person))

# 2-7 Stripping Names: Usa a variable to represent a person's name, and include
# some whitespace characters at the beginning and end of the name. Make sure you use
# each character combination, "\t" and "\n, at least once.
#   Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().

person = ' Dave '

print(person)
print(person.lstrip())
print(person.rstrip())
print(person.strip())



