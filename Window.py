import pygame as p


class Window:
    def __init__(self, size, title, input):

        self.input = input

        self.window_size = size
        self.window = p.display.set_mode(size)
        p.display.set_caption(title)

    def update(self, dt):
        pass

    def end_draw(self):
        p.display.update()

    def get_mouse_pos(self):
        return p.mouse.get_pos()
