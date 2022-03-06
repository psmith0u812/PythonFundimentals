# On page 78 of your book, do 5-1 of the Try it Yourself. Put all your code
# in your exercise5.py file.

cup = 'stein'
# print("Is cup == 'stein'? I predict true.")
# print(cup == 'stein')

# print("\nIs cup == 'mug'? I predict False.")
# print(cup == 'mug')

# Create as least 5 tests that evaluate true and 5 that evaluate false.
# 1
dog = 'mutt'
# print("Is dog == 'mutt'? I predict true.")
# print(dog == 'mutt')

# 2
# print("\nIs dog == 'tramp'? I predict False.")
# print(dog == 'tramp')

# 3
toy = 'new'
# print("Is toy == 'new'? I predict true.")
# print(toy == 'new')

# 4
# print("\nIs toy == 'old'? I predict False.")
# print(toy == 'old')

# 5
cat = 'alive'
# print("Is cat == 'alive'? I predict true.")
# print(cat == 'alive')

# 6
# print("\nIs cat == 'dead'? I predict False.")
# print(cup == 'dead')

# 7
fire = 'hot'
# print("Is fire == 'hot'? I predict true.")
# print(fire == 'hot')

# 8
# print("\nIs fire == 'dim'? I predict False.")
# print(fire == 'dim')

# 9
aliens = 'real'
# print("Are aliens == 'real'? I predict true.")
# print(aliens == 'real')

#10
# print("\nAre aliens == 'made up'? I predict False.")
# print(aliens == 'made up')


# On page 78 of your book, create new examples that meet the bullet points
# of 5-2
# Test for equality and inequality with strings
def eq_ineq(val1, val2):
    result_eq = val1 == val2
    # print(result_eq)
    result_not = val1 != val2
    # print(result_not)

# eq_ineq('MSG', 'msg')

# Tests using the lower() method

    result_eq = val1.lower() == val2
    print(result_eq)
    result_not = val1.lower() != val2
    print(result_not)

# eq_ineq('MSG', 'msg')


# Numerical tests involving equality and inequality, greater than and less than
#, greater than or equal to and less than or equal to.

num1 = 6
num2 = 4
num3 = 24

def num_equal_test():
    num_eq = num1 == num1
    print(num_eq)
    num_not = num3 != num2
    print(num_not)
    num_gt = num1 > num2
    print(num_gt)
    num_lt = num2 < num3
    print(num_lt)
    num_gt_eq = num3 >= num2 * num1
    print(num_gt_eq)
    num_lt_eq = num2 <= num3 / num1
    print(num_lt_eq)

# num_equal_test()

# Tests using the "and" keyword and the "or" keyword
def vals_and_or():
    val_and = (10 < num1 and num1 > num2)
    print(val_and)
    val_or = (32 > num3 or num2 < num3)
    print(val_or)

# vals_and_or()

# Test whether an item is in a list
# test whether an item is not in a list
list = 'The quick brown fox jumps over the lazy dog'

def check_list():
    check_is = ('fox') in list
    print(check_is)

    check_not = ('Jumps') not in list
    print(check_not)

# check_list()

# Write a function that will take 2 arguments. Inside the function provide examples
# of all the arithmetic operators. Provide a Variable for each solution and print
# the results of each.

def math_mash(val1, val2, val3):
    answer1 = val1 + val2 - val3
    answer2 = val3 * 10 / val2
    answer3 = val3 ** 3 % 5
    answer4 = val2 ** 2 // 12
    print(answer1)
    print(answer2)
    print(answer3)
    print(answer4)

# math_mash(41, 66, 32)

# Write a function that takes only 1 argument. Inside the function provide examples
# of Assignment operators: modulus equals, minus equals, exponent equals & plus
# equals. Provide a variable for each solution and print the results of each.

def eq_maths(val1, val2):
    alpha = 4
    val1 %= alpha
    print(val1)
    val1 -= alpha
    print(val1)
    val2 **= alpha
    print(val2)
    val2 += alpha
    print(val2)


eq_maths(6, 3)

