# 11-1  City, Country

#import unittest
#from city_functions import get_city_country

#class CityCountryTestCase(unittest.TestCase):
    # Test city_functions.py

        #def test_city_country(self):
            # do formated city country pairs work?
            formatted_city_country = get_city_country('city', 'country')
            self.assertEqual(formatted_city_country, 'City, Country')

        #def test_city_country_population(self):
            formatted_input = get_city_country('City', 'Country', 50000000)
            self.assertEqual(formatted_input, 'City, Country - Population 5000000')

#if __name__ == '__main__':
    #unittest.main()



# 11-3

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    # test Employee class
    def setup(self):
        first_name = 'Bob'
        last_name = 'Ross'
        self.salary = 50000
        self.employee = Employee(first_name, last_name, self.salary)

    def test_give_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, self.salary + 5000)

    def test_corporate_theft(self):
        custom_raise = 10000
        self.employee.give_raise(custom_raise)
        self.assertEqual(self.employee.salary, self.salary + custom_raise)

    if __name__ == '__main__':
        unittest.main()
