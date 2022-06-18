from Debug import Debug


class SceneStateMachine:
    def __init__(self):
        self.stack = []
        self.last_scene = None
        self.cur_scene = None

    def early_update(self, delta_time):
        self.cur_scene.early_update(delta_time)

    def update(self, delta_time):
        self.cur_scene.update(delta_time)

    def late_update(self, delta_time):
        self.cur_scene.late_update(delta_time)

    def draw(self, canvas):
        self.cur_scene.draw(canvas)

    def add(self, scene):
        Debug.log(f"Scene Added -- {scene.name}")
        self.stack.append(scene)
        self.cur_scene = scene

    def remove(self):
        Debug.log(f"Scene Removed -- {self.cur_scene.name}")
        self.cur_scene.on_destroy()
        self.stack.pop()
        self.cur_scene = self.stack[-1]

    def remove_all(self):
        while len(self.stack) > 1:
            self.remove()
