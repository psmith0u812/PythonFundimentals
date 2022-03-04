# Try it yourself Page 29
# 2-8 Number Eight:
# write addition, subtraction, multiplaction, and
# division operations that each result in the number 8

print(4+4)
print(9-1)
print(2*4)
print(16/2)

# 2-9 Favorite Number: use a variable to represent your favorite number.
# Then using that variable, create a message that reveals your favorite number.
# print the message.

message = 'My favorite number is {0}'
favorite_number = (40+7)
print(message.format(favorite_number))

# Assign variables to following sets of numbers. Use underscores to make
# them more readable.
# Write a function called number_sets and print each variable inside the
# function. Call the function to verify your results.

def number_sets():
    print(val ,val2 ,val3 ,val4)

val = (456_234)
val2 = (68_423_791)
val3 = (13_794_628)
val4 = (96_374)

number_sets()

# Write a function that will take 2 arguments. Using Type conversion, convert
# the first argument from int to float. Convert the second argument from float to int.
# call the function and provide the correct values for each argument to varify your results.
# one argument should be a float and the other an int.

def number_sets2():
    print(float(val5), int(val6))

val5 = (46)
val6 = (87.9)

number_sets2()

# Write a function that will have two inputs. The first input method should ask
# "What is your favorite movie" the second input method should ask
# "How many times have you seen it?". The second input should be inside an int
# function. Each input method should be assigned to a variable. In a print
# statement using placeholders, the output result should be
# " I have seen {favorite movie} {number of times} times".


message = 'I have seen {0} {1} {2}.'
favorite_movie = input('What is your favorite Movie?')
times_seen = int(input('How many times have you seen it?'))
word = 'times'
if times_seen == 1:
    word = 'time'
print(message.format(favorite_movie, int(times_seen), word))




