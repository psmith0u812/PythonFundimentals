# Control Flow Statements
# page 84, Try it Yourself 5-3

# alien_color = 'green'
# if alien_color == 'green':
   # print('player earned 5 points')
# if alien_color == 'red':
   # print('player earned 5 points')


# page 84, Try it Yourself 5-4

#alien_color = 'red'
#if alien_color == 'green':
    #print('player earned 5 points')
#else:
    #print('player earned 10 points')

#if alien_color == 'green':print('player earned 5 points')
#else:
    #print('player earned 10 points')

# page 84, Try it Yourself 5-5
alien_color1 = 'green'
if alien_color1 == 'green':
    print('player earned 5 points')
elif alien_color1 == 'yellow':
    print('player earned 10 points')
else:
    print('player earned 15 points')

alien_color2 = 'yellow'
if alien_color2 == 'green':
    print('player earned 5 points')
elif alien_color2 == 'yellow':
    print('player earned 10 points')
else:
    print('player earned 15 points')

alien_color3 = 'red'
if alien_color3 == 'green':
    print('player earned 5 points')
elif alien_color3 == 'yellow':
    print('player earned 10 points')
else:
    print('player earned 15 points')
# page 84, Try it Yourself 5-6

def life_stages(age):
    if age < 2:
        print('Person is Baby.')
    elif age >= 2 and(age < 4):
        print('Person is a Toddler.')
    elif age >= 4 and(age < 13):
        print('Person is a kid.')
    elif age >= 13 and(age < 20):
        print('Person is a teenager.')
    elif age >= 20 and(age <= 65):
        print('Person is an Adult')
    else:
        print('Person is an Elder')

#life_stages(13)

# Write a function that takes an argument. Check this argument to see if it is
# a Boolean using the bool method. Call the method and use the below values as your
# argument. Using Comments,provide the name of the argument and if it was true or false
# from running the code.  12, 1.2, 0, 0.4, 0.0

def bool_checker(arg):
    print(bool(arg))

bool_checker(0.0)
# Bool_checker , argument value results
# arg = 12, result = True
# arg = 1.2, result = True
# arg = 0, result = False
# arg = 0.4, result = True
# arg = 0.0, result = False