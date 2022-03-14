
class Watch:

    def __init__(self, face, band_type, control, frame):
        self._watch_face = face
        self._watch_band = band_type
        self._control_style = control
        self._frame_shape = frame

    def show_time(self):
        return f' The {self._watch_band} band tight on your wrist, turned to view a \n' \
               f'{self._frame_shape} body with a {self._watch_face} style face. You notice a problem.\n' \
               f'Your watch isn\'t working.'

    @property
    def watch_face(self):
        return self._watch_face

    @watch_face.setter
    def watch_face(self):
        self._watch_face

    @property
    def watch_band(self):
        return self._watch_band

    @watch_band.setter
    def watch_band(self, material):
        self._watch_band = material

    @property
    def watch_control_style(self):
        return self._control_style

    @watch_control_style.setter
    def watch_control_style(self, style):
        self._control_style = style

    @property
    def frame_shape(self):
        return self._frame_shape

    @frame_shape.setter
    def frame_shape(self, shape):
        self._frame_shape = shape

    def show_watch(self):
        return f'This watch features {self._frame_shape} frame with a {self._watch_face} styled face. The {self._watch_band}\n' \
               f'band, and {self._control_style} control, makes this watch a functional and fashionable piece.\n'

my_watch = Watch('Diver', 'leather', 'crown', 'octoganal')
print(my_watch.show_watch())
print(my_watch.show_time())