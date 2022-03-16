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

user_names()
print(user_names)
