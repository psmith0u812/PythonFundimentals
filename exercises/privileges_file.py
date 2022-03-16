


class Privileges:
    # Define Privileges
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        # Display list of privileges
        print('Current Admin Privileges:')
        for privilege in self.privileges():
            print(f' - {privilege}')


