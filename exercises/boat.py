class Boat:
    def __init__(self, deck, hull, helm, anchor ):
        self._deck_type = deck
        self._hull_type = hull
        self._helm_control_style = helm
        self._anchor_type = anchor

    def anchor_up_down(self):
        return (str.format('The boat is ready, {} anchor is up.', self._anchor_type))

    @property
    def deck_type(self):
        return self._deck_type

    @deck_type.setter
    def deck_type(self, num):
        self._deck_type

    @property
    def hull_type(self):
        return self._hull_type

    @hull_type.setter
    def hull_type(self, type):
        self._hull_type = type

    @property
    def helm_control_style(self):
        return self._helm_control_style

    @helm_control_style.setter
    def helm_control_style(self, style):
        self._helm_control_style = style

    @property
    def anchor_type(self):
        return self._anchor_type

    @anchor_type.setter
    def anchor_type(self, model):
        self._anchor_type = model

    def show_boat(self):
        return f'You stand on the {self._deck_type} deck of a {self._hull_type} boat. The {self._anchor_type}\n' \
               f'anchor, and {self._helm_control_style} helm, appear to be functional.\n'

my_boat = Boat('wood', 'fiberglass', 'mechanical', 'mushroom')
print(my_boat.show_boat())
print(my_boat.anchor_up_down())
