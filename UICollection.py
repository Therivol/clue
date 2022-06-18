

class UICollection:
    def __init__(self, client):
        self.client = client
        self.input = client.input
        self.surfaces = []
        self.buttons = []

    def add_surface(self, surface):
        self.surfaces.append(surface)

    def add_button(self, button):
        self.buttons.append(button)

    def get_button_down(self, button):
        if self.input.get_button_down(button.activator):
            mouse_pos = self.client.window.get_mouse_pos()
            if button.rect.collidepos(mouse_pos):
                return True

        return False

    def draw(self, canvas):
        pass


class Button:
    def __init__(self, rect, activator):
        self.rect = rect
        self.activator = activator
