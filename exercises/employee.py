

class Employee:
# employee info
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, salary_raise=5000):
# add 5000 to anual
        self.salary += salary_raise
