import pygame as p
import sys
from Input import Input
from Window import Window
from SceneStateMachine import SceneStateMachine
from SceneMenu import SceneMenu
from UICollection import UICollection


class Client:
    def __init__(self):
        self.input = Input()

        self.window = Window((960, 540), "Clue", self.input)

        self.scene_manager = SceneStateMachine()
        self.scene_manager.add(SceneMenu(self))

        self.is_running = True

        self.delta_time = 0
        self.last_frame_time = 0

    def update(self):
        self.scene_manager.update(self.delta_time)

    def draw(self):
        self.scene_manager.draw(self.window.window)
        self.window.end_draw()

    def calculate_delta_time(self):
        self.delta_time = (p.time.get_ticks() - self.last_frame_time) / 1000
        if self.delta_time == 0:
            self.delta_time = 0.001
        self.last_frame_time = p.time.get_ticks()

    def capture_input(self):
        for ev in p.event.get():
            if ev.type == p.QUIT:
                self.is_running = False
                p.quit()
                sys.exit()

            if ev.type == p.KEYDOWN:
                self.input.set_key(ev.key)

            if ev.type == p.KEYUP:
                self.input.reset_key(ev.key)

            if ev.type == p.MOUSEBUTTONDOWN or p.MOUSEBUTTONUP:
                self.input.set_buttons()