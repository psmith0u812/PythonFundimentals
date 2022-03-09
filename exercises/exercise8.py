# Exercise 8 Decisions and Collections.

# Page 89 Try it Yourself 5-8

# staff = ['Admin', 'Jaden', 'Jim', 'Pam', 'Dwight']
#

def hello_admin():
    for person in staff:
        if person == "Admin":
            print("Hello Admin, would you like a status report?")
        else:
            print("Hello, {} welcome back".format(person))

# hello_admin()

# Page 89 Try it Yourself 5-9
staff = []
    # ['Admin', 'Jaden', 'Jim', 'Pam', 'Dwight']

def hello_admin2():
    if len(staff) == 0:
        print('We need to find some users!')
    for person in staff:
        if person == "Admin":
            print("Hello Admin, would you like a status report?")
        else:
            print("Hello, {} welcome back".format(person))

# hello_admin2()

# Page 89 Try it Yourself 5-10
current_users = ['John', 'Dave', 'Frank', 'Michael', 'Sylvia']
new_users = ['John', 'Katie', 'Hugo', 'Sarah', 'Betty']
def user_names():
    if set(current_users).intersection(set(new_users)):
        alpha = [user.upper() for user in current_users]
        for person in new_users:
            if person.upper() in alpha:
                print(person)
                print('This Username already exists.')
    else:
        print('User name is Available')


# user_names()


# Page 89 Try it Yourself 5-11

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def num_place():
    for num in num_list:
        if num == 1:
            print('{}st'.format(num))
        elif num == 2:
            print('{}nd'.format(num))
        elif num == 3:
            print('{}rd'.format(num))
        else:
            print('{}th'.format(num))

# num_place()


# Page 99 Try it Yourself 6-1
person_block1 = {'First Name': 'Olfina','Last Name': 'Greymane', 'Age': '27', 'City': 'Whiterun'}
def print_dict():
    for val in person_block1:
        print(person_block1[val])

# print_dict()

# Page 112 Try it Yourself 6-7
person_block2 = {'First Name': 'Ulfric', 'Last Name': 'Stormcloak', 'Age': '34', 'City': 'Windhelm'}
person_block3 = {'First Name': 'Thorald', 'Last Name': 'Greymane', 'Age': '25', 'City': 'Whiterun'}

people = [person_block1, person_block2, person_block3]

def show_persons():
    for blocks in people:
        print(blocks['First Name'])
        print(blocks['Last Name'])
        print(blocks['Age'])
        print(blocks['City'])

show_persons()

# Was trying to find a way to format dictionary values to print nicer, couldn't figure out how to combine.
# didn't have the time I wanted to mess with it.
#       for cat, val in person_block1.items():
#            print(cat,'-',val)
#       for bat, gal in person_block2.items():
#            print(bat,'-',gal)
#       for gat, sal in person_block3.items():
#           print(gat,'-',sal)
#        print(people)

