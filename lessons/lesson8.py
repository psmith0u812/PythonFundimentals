# Lesson 8 Collections

# list collection
# Ordered collection that can be changleable and allow duplicates
# and uses square brackets to define the collected data

colors = ['red', 'blue', 'green', 'purple', 'magenta', 'black',
          'white', 'orange']
sizes = [42, 32, 156, 89, 34, 23, 8, 19]

mixed = [23, 'happy', 'python', 90, 45, 'snow', 'car', 56]


# direct print
def simple_print():
    print(colors)


# simple_print()

# print 1 item
def simple_single():
    print(sizes[3])

# simple_single()


# for loop of list
def simple_for_print():
    for mix in mixed:
        print(mix)

# simple_for_print()

# range of the list
# range of values in a list is the same as in strings.
def simple_range():
    print(colors[2:5])
    print(colors[-5:-2])

# simple_range()

# using len to get the lenght of a list
def simple_length():
    my_colors = len(colors)
    print(len(colors))
    value = 0
    while value < my_colors:
        print(colors[value])
        value += 1

# simple_length()

# using in keyword to search a list for the item
def simple_search():
    if 89 in sizes:
        print('89 is in the lise')
    else:
        print('89 is not in the list')

# simple_search()


# append and insert to a list
# append will insert at the end of the list
def simple_append():
    mixed.append('Friday')
    for mix in mixed:
        print(mix)

# simple_append()


# insert will allow you to insert at a specific index position
def simple_insert():
    mixed.insert(3,'Friday')
    for value in mixed:
        print(value)

# simple_insert()


# Removing items from a list by remove(), pop(), del and clear()
# the remove function will remove from a specified value from the list
def simple_remove():
    colors.remove('green')
    for color in colors:
        print(color)

# simple_remove()

# The pop method will removed an item from a specified index.
# not picking an index will take the last item.
def simple_pop():
    colors.pop(5)
    for value in colors:
        print(value)

# simple_pop()


# the del keyword can removed a value at a specific index, and
# can also delete the list entirely
def simple_del():
    del colors[3]
    for color in colors:
        print(color)

# simple_del()


# del with no index removes the list completely
def simple_del_none():
    trucks = ['chevy', 'ford', 'dodge']
    del trucks
    # trucks.append('Toyota')
    # for value in trucks:
    #    print(value)

# simple_del_none()

# clear method will empty a list, but no removed the list
def simple_clear():
    mixed.clear()
    mixed.append('Python')
    for mix in mixed:
        print(mix)

# simple_clear()

# list operations: Concatenation, repeate, membership, and iterate
# concatenation
def sijmple_join():
    values1 = [1, 2, 3, 4]
    values2 = [5, 6, 7, 8]
    total = values1 + values2
    for val in total:
        print(val)

# sijmple_join()

# repeat will repeat a list a certain amount of times.
def simple_repeat():
    values = [1,2,3]
    print(values * 3)


# simple_repeat()

# membership
def simple_membership():
    result = 'red' in colors
    print(result)

# imple_membership()


# iterate
def simple_iterate():
    for color in colors:
        print(color, end=' ')

# simple_iterate()

# the tuple collection
# Ordered collection that Can NOT be changed.
my_fruits = ('apple', 'banna', 'cherry', 'orange')
# print(my_fruits)

def simple_tuple():
    for fruit in my_fruits:
        print(fruit)

    print(my_fruits[-3:-1])

# simple_tuple()


# Change a alue in a tuple, by converting to list then back again.
def simple_change_tuple():
    fruity = list(my_fruits)
    fruity.append('peach') # ---> adds to existing list
    # fruity[2] = 'peach'   --->  replaces existing index
    my_fruit = tuple(fruity)
    for fruit in my_fruit:
        print(fruit)

# simple_change_tuple()

# Part 2 of collections with Set and Dictionary
# set collection
# this collection is an unordered and un-indexed. this means
# the order of the items vary
ice_cream = {'chocolate', 'vanilla', 'strawberry', 'neopolitan',
             'chocolate chip', 'rocky road', 'cookie dough'}

def simple_set():
    for flavor in ice_cream:
        print(flavor)

# simple_set()

# adding items to a set can be done by add() and update()
# add method
def simple_set_add():
    ice_cream.add('bunny tracks')
    for value in ice_cream:
        print(value)

# simple_set_add()

# update method
def simple_set_update():
    ice_cream.update({'butter pecan', 'bunny tracks', 'peanunt butter cup'})
    for flavor in ice_cream:
        print(flavor)

# simple_set_update()

# Removing items can be done in three ways: remove(), discard() & pop()
# removed will generate an erro if the item being removed does not exist
def simple_set_remove():
    num_windows = {34, 23, 78, 98, 37}
    num_windows.remove(98)
    for num in num_windows:
        print(num)

# simple_set_remove()


# discard will remove without generating an erro
# if the value is not in the list
def simple_set_discard():
    letters = {'a', 'b', 'c', 'd', 'e', 'f'}
    letters.discard('a')
    for letter in letters:
        print(letter)

# simple_set_discard()


# pop will remove the last item from the list so you don't know what it is.
def simple_set_pop():
    letters = {'a', 'b', 'c', 'd', 'e', 'f'}
    letters.pop()
    for alpha in letters:
        print(alpha)

# simple_set_pop()

# Joining set collections by update, union and | opperator
even = {2, 4, 6, 8, 10}
odd = {1, 3, 5, 7, 9}
tens = {10, 20, 30, 40, 50}

# update
def simple_set_join():
    even.update(odd)
    for num in even:
        print(num)

# simple_set_join()

# union
def simple_set_union():
    values = tens.union(odd)
    for item in values:
        print(item)

# simple_set_union()

# | operator
def simple_set_pipe():
    numbers = odd | even | tens
    for val in numbers:
        print(val)

# simple_set_pipe()

# Dictionaries are collections consisting of a key and value
# the key is unique and can not be duplicated, making immutable
# the value however can be duplicated. Defined using curly braces
trucks = {101: 'silverado', 102: 'f150', 103: 'ram'}
# print(trucks)
# print(trucks[102])
# print(trucks.get(103))

# add and update
# trucks[104] = 'titan'
# trucks[102] = 'f250'
# print(trucks)

# looping through lists: basic print
def simple_dict_loop():
    for truck in trucks:
        print(truck)

# simple_dict_loop()

# loop using []
def simple_dict_square():
    for truck in trucks:
        print(trucks[truck])

# simple_dict_square()

# loop using values() method
def simple_dict_values():
    for some in trucks.values():
        print(some)

# simple_dict_values()

# Loop getting both key and value
def simple_dict_both():
    for able, beta in trucks.items():
        print(able, ' - ', beta)

#simple_dict_both()

# nested dictionaries refer to having a dictionary within a dictionary
my_pallet = {'color':{'primary':'red','secondary': 'maroon'},
             'color2': {'primary': 'blue', 'secondary': 'royal'}}

def simple_dict_multi():
    for col1, col2 in my_pallet.items():
        print(col1, ' - ', col2)

# simple_dict_multi()

