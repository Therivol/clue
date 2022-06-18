import pygame as p
from Scene import Scene
from UICollection import UICollection


class SceneMenu(Scene):
    def __init__(self, client):
        super().__init__("Menu", client)

    def draw(self, canvas):
        canvas.fill((100, 100, 100))

    def update(self, delta_time):
        pass
