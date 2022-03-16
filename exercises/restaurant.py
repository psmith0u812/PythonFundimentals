
class Restaurant:
    # instantiate and Define attributes of Restaurant"
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.name = restaurant_name
        self.type = cuisine_type
        self.served = number_served

    def describe_restaurant(self):
        # Display message using Restaurant values
        return(f'{self.name} is a family friendly establishment, '
          f'serving\nonly the best {self.type} style cuisine folks know and love.\n')


    def open_restaurant(self):
        # Display simple open message
       return(f'{self.name} is now open!')

    def set_number_served(self, customers):
        # Display Result for total number of customers served
        return f'{self.served + customers} customers served.'


    def incremet_number_served(self, customers):
        # Define value for current number served
        self.served += customers
        if customers >= self.served:
            return 'No new customers'

class IceCreamStand(Restaurant):

        # Import superclass Restaurant values for subclass IceCreamStand
        def __init__(self, restaurant_name, cuisine_type, icecream_flavors):
            super().__init__(restaurant_name, cuisine_type)
            self._flavors = icecream_flavors

        def icecream_menu(self):
         # Display IceCream Menu
            print(f'Today\'s Icecream Flavors are: ')
            for self._flavors in self._flavors:
                print(f'{self._flavors}')


my_restaurant = Restaurant('Shananagains', 'Americian', 124)
my_restaurant.set_number_served(65)
print(my_restaurant.open_restaurant())
print(my_restaurant.describe_restaurant())
print(my_restaurant.set_number_served(65))
print(my_restaurant.incremet_number_served(35))



my_icecream = IceCreamStand('Ice Box', 'Icecream', ['Chocolate', 'Vanilla', 'Strawberry'])

IceCreamStand.icecream_menu(my_icecream)

