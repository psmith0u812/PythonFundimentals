

class Guitar:

    def __init__(self, strings, body, neck, pegs):
        self._guitar_strings_num = strings
        self._body_color = body
        self._neck_shape = neck
        self._tuning_pegs = pegs

    def play_string(self):
        return f' This guitar has a has {self._guitar_strings_num} strings.\n You pluck one at random.'


    @property
    def guitar_strings_num(self):
        return self._guitar_strings_num

    @guitar_strings_num.setter
    def guitar_strings_num(self, num):
        self._guitar_strings_num = num

    @property
    def body_color(self):
        return self._body_color

    @body_color.setter
    def body_color(self, color):
        self._body_color = color

    @property
    def neck_shape(self):
        return self._neck_shape

    @neck_shape.setter
    def neck_shape(self, neck):
        self._neck_shape = neck

    @property
    def tuning_pegs(self):
        return self._tuning_pegs

    @tuning_pegs.setter
    def tuning_pegs(self, pegs):
        self._tuning_pegs = pegs

    def show_guitar(self):
        return f' This guitar has a {self._body_color} body, {self._guitar_strings_num} strings.\n' \
               f' you look over its {self._neck_shape} neck and {self._tuning_pegs} tuning setup.\n'


my_guitar = Guitar('six', 'blue', 'c-shape', 'linear')
print(my_guitar.show_guitar())
print(my_guitar.play_string())