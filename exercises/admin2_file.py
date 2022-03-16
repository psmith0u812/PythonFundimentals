

class Admin(User):
    # Import superclass User values for subclass Admin
    def __init__(self, first_name, last_name, current_weight, first_weight, goal_weight, privileges):
        super().__init__(self, first_name, last_name, current_weight, first_weight, goal_weight)
        self.privileges = Privileges(privileges)


