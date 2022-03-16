#Designs that need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']

def print_models(unprinted_designs, completed_models):
# Simulate printing each design, until there are not left

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing Model: {current_design}')
        completed_models.append(current_design)

def show_completed_models(completed_models):
# Display all completed models
    print('\nThe following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)


completed_models = []

print_models()

