

class Scene:
    def __init__(self, name, client):
        self.game = client
        self.name = name
        self.window = client.window
        self.input = client.input
        self.scene_manager = client.scene_manager

    def on_destroy(self):
        pass

    def on_activate(self):
        pass

    def early_update(self, delta_time):
        pass

    def update(self, delta_time):
        pass

    def late_update(self, delta_time):
        pass

    def draw(self, canvas):
        pass
