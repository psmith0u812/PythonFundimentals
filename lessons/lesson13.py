# Lesson 13 - Modules & Packages
# import happy

# print(happy.express())

import happy as hey
from math import pi
import house

print(hey.express(False))

print('The value for pi is {0}'.format(pi))

house3 = house.House(21, 'wood', 'bamboo', 'green')
print(house3.door_color)


if __name__ == '__main__':
    house2 = house.House(21, 'dirt', 'straw', 'blue')
    print(house2.door_open_close())