

class Horse:

    def __init__(self, tail, hooves, mane, body):
        self._tail_length = tail
        self._hooves_condition = hooves
        self._mane_style = mane
        self._horse_frame = body

    def mount_horse(self):
        return f' The horse shudders as you mount up. Its {self._horse_frame} body, breathing beneath your weight.\n' \
               f' You stroke its {self._mane_style} mane to reasure it.' \
               f' its {self._tail_length} tail stops swaying. What now?'

    @property
    def tail_length(self):
        return self._tail_length

    @tail_length.setter
    def tail_length(self, length_description):
        self._tail_length = length_description

    @property
    def hooves_condition(self):
        return self._hooves_condition

    @hooves_condition.setter
    def hooves_condition(self, condition):
        self._hooves_condition = condition

    @property
    def mane_style(self):
        return self._mane_style

    @mane_style.setter
    def mane_style(self, style):
        self._mane_style = style

    @property
    def horse_frame(self):
        return self._horse_frame

    @horse_frame.setter
    def horse_frame(self, body):
        self._horse_frame = body


    def show_horse(self):
        return f' Before you stands a {self._horse_frame} horse, its {self._mane_style} mane glistening in the sun\n' \
               f'{self._tail_length} swaying idly, and see its hooves in {self._hooves_condition} conditon.' \
               f'\n It notices you.\n'


class Zebra(Horse):
    def __init__(self,  tail, hooves, mane, body, ears):
        super().__init__( tail, hooves, mane, body)
        self._ears = ears

    @property
    def ears(self):
        return self._ears

    @ears.setter
    def ears(self, ears):
        self._ears = ears


class Pony(Horse):
    def __init__(self,  tail, hooves, mane, body, bow):
        super().__init__( tail, hooves, mane, body)
        self._bow = bow

    @property
    def bow(self):
        return self._bow

    @bow.setter
    def bow(self, bow):
        self._bow = bow


my_horse = Horse('long', 'good', 'long', 'heavy')
print(my_horse.show_horse())
print(my_horse.mount_horse())