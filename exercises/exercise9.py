# Exercise 9 Python Fundamentals

# page 137 exercise 8-3 through 8-5

def make_shirt(arg1, arg2='large'):
    print(arg2+' - '+arg1)

# make_shirt('I Love Python')
# make_shirt('I Love Python', 'Medium')
# make_shirt('I love Python', 'XXL')

def describe_city(city, country='iceland'):
    print(f'{city.capitalize()} is in {country.capitalize()}.')
# describe_city('reykjavik')

# page 146 exercise 8-9 through 8-11
# 8-9


# def show_message():
    # for message in messages:
        # print(message)

# show_message()

# 8-10
def show_messages():
    for message in messages:
        print(message)

# show_messages()
messages = ['sup', 'wtf bro!?', 'o\'rily', 'what\'cha doin\'?']
sent_messages = []

def send_messages():
    while messages:
        message = messages.pop()
        print(f'\n{message} sending\n')
        sent_messages.append(message)
        for sent in sent_messages:
            print(f'{sent} delevered')

# send_messages()


# page 162 exercise 9-1 through 9-3
# 9-1

# class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def discribe_restaurant(self):
        return(f'{self.name} is a family friendly establishment, '
          f'serving\nonly the best {self.type} style cuisine folks know and love.\n')


    def open_restaurant(self):
       return(f'{self.name} is now open!')

# 9-2

# my_restaurant = Restaurant('Shenanigans', 'Americian')
# my_cajun_joint = Restaurant('Mama O\'de\'s', 'Creole-Cajun')
# my_pizza_place = Restaurant('Sophia Petrillo\'s', 'Italian')
# my_taco_stand = Restaurant('Cuba Pete\'s', 'Mexician')
# print(my_restaurant.discribe_restaurant())
# print(my_restaurant.open_restaurant())
# print(my_pizza_place.discribe_restaurant())
# print(my_taco_stand.discribe_restaurant())
# print(my_cajun_joint.discribe_restaurant())


# 9-3
# class User:

    def __init__(self, first_name, last_name, current_weight, first_weight, goal_weight):

        self.first = first_name
        self.last = last_name
        self.cur = current_weight
        self.start = first_weight
        self.goal = goal_weight

    def describe_user(self):
        return (f'{self.first} {self.last} your first weigh-in was {self.start}lbs.\n'
        f'Your last recorded weight was {self.cur}lbs, you are ({int(self.cur) - int(self.goal)})lbs\n'
        f'from your goal weight of {self.goal}lbs, Keep it up champ! You\'ve got this!\n')


    def greet_user(self):
        return (f' Welcome {self.first} {self.last}! We\'re excited to have you \n'
                f'continue you\'re weight-loss journey with us!\n')



# user_101 = User('Richard', 'Head', 275, 342, 195)
# user_102 = User('Ted', 'Kazinsky', 250, 280, 176)
# user_103 = User('Michael', 'Hunt', 222, 271, 200)
# print(user_101.greet_user())
# print(user_101.describe_user())

# print(user_102.greet_user())
# print(user_102.describe_user())

# print(user_103.greet_user())
# print(user_103.describe_user())

# page 167 exercise 9-4 and 9-5

# 9-4
# class Restaurant:

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.name = restaurant_name
        self.type = cuisine_type
        self.served = number_served

    def discribe_restaurant(self):
        return(f'{self.name} is a family friendly establishment, '
          f'serving\nonly the best {self.type} style cuisine folks know and love.\n')


    def open_restaurant(self):
       return(f'{self.name} is now open!')

    def set_number_served(self, customers):
        return f'{(self.served) + (customers)} customers served.'


    def incremet_number_served(self, customers):
        self.served += customers
        if customers >= self.served:
            return 'No new customers'



# my_restaurant = Restaurant('Shenanigans', 'Americian', 5)
# my_restaurant1 = Restaurant('Shenanigans', 'Americian', 6)
# my_restaurant2 = Restaurant('Shenanigans', 'Americian', 6)
# my_restaurant3 = Restaurant('Shenanigans', 'Americian', 3)
# my_restaurant.set_number_served(65)

# print(my_restaurant1.discribe_restaurant())
# print(my_restaurant1.open_restaurant())
# print(my_restaurant1.incremet_number_served(35))
# print(my_restaurant1.set_number_served(65))


# 9-5
class User:
    def __init__(self, first_name, last_name, current_weight, first_weight, goal_weight, login_attempts=0):

        self.first = first_name
        self.last = last_name
        self.cur = current_weight
        self.start = first_weight
        self.goal = goal_weight
        self.log_at = login_attempts


    def describe_user(self):
        return (f'{self.first} {self.last} your first weigh-in was {self.start}lbs.\n'
                f'Your last recorded weight was {self.cur}lbs, you are ({int(self.cur) - int(self.goal)})lbs\n'
                f'from your goal weight of {self.goal}lbs, Keep it up champ! You\'ve got this!\n')


    def greet_user(self):
        return (f' Welcome {self.first} {self.last}! We\'re excited to have you \n'
                f'continue you\'re weight-loss journey with us!\n')

    def increment_login_attempts(self):
        self.log_at += 1
        return (f'( We\'re sorry, your login ID or password failed \n'
                f'Attempt Number {self.log_at}')

    def reset_login_attempts(self):
        self.log_at = 0
        return 'You\'re Login has been reset'

user_101 = User('Richard', 'Head', 275, 342, 195)

# user_102 = User('Ted', 'Kazinsky', 250, 280, 176)
# user_103 = User('Michael', 'Hunt', 222, 271, 200)
# print(user_101.greet_user())
# print(user_101.describe_user())
print(user_101.increment_login_attempts())
print(user_101.reset_login_attempts())
#print(user_102.greet_user())
#print(user_102.describe_user())
#print(user_102.increment_login_attempts(1))
#print(user_103.greet_user())
#print(user_103.describe_user())



