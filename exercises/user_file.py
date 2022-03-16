
class User:
    # Define class User, and attributes
    def __init__(self, first_name, last_name, current_weight, first_weight, goal_weight, login_attempts=0):
        self._first = first_name
        self._last = last_name
        self.cur = current_weight
        self.start = first_weight
        self.goal = goal_weight
        self.log_at = login_attempts

    def describe_user(self):
        # Display message using full list of user values
        return (f'{self._first} {self._last} your first weigh-in was {self.start}lbs.\n'
                f'Your last recorded weight was {self.cur}lbs, you are ({int(self.cur) - int(self.goal)})lbs\n'
                f'from your goal weight of {self.goal}lbs, Keep it up champ! You\'ve got this!\n')

    def greet_user(self):
        # Display Message using partial values
        return (f' Welcome {self._first} {self._last}! We\'re excited to have you \n'
                f'continue you\'re weight-loss journey with us!\n')

    def increment_login_attempts(self):
        # Increment log in attempts
        self.log_at += 1
        return (f'( We\'re sorry, your login ID or password failed \n'
                f'Attempt Number {self.log_at}')

    def reset_login_attempts(self):
        # reset value for login attempts
        self.log_at = 0
        return 'You\'re Login has been reset'



my_user = User('Ted', 'Kazinsky', 250, 280, 176,)
#['Add New User', 'Remove User', 'Edit User Entries'])
#my_admin.show_privileges()



