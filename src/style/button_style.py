from kivy.uix.button import Button


class StyledButton(Button):
    def __init__(self, **kwargs):
        super(StyledButton, self).__init__(**kwargs)
        self.background_color = (0.2, 0.2, 0.2, 1)
        self.color = (1, 1, 1, 1)

