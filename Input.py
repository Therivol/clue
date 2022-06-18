import pygame as p
import json


class Input:
    def __init__(self):

        self.key_binds = {}
        self.load_key_binds("../settings/key_binds.json")

        self.actions = {action: False for action in self.key_binds.values()}
        self.raw_keys = {}
        self.mouse_buttons = {}
        self.handled_keys = []
        self.handled_buttons = []

    def load_key_binds(self, path):
        pass

    def reset(self):
        for action in self.actions:
            self.actions[action] = False

    def set_key(self, key):
        key_name = p.key.name(key)
        # Debug.log(key_name)
        self.raw_keys[key_name] = True
        if key_name in self.key_binds.keys():
            self.actions[self.key_binds[key_name]] = True

    def reset_key(self, key):
        key_name = p.key.name(key)
        self.raw_keys[key_name] = False
        if key_name in self.handled_keys:
            self.handled_keys.remove(key_name)
        if key_name in self.key_binds.keys():
            self.actions[self.key_binds[key_name]] = False

    def set_buttons(self):
        presses = p.mouse.get_pressed()
        i = 1
        for press in presses:
            if press:
                self.mouse_buttons[str(i)] = True
            else:
                self.mouse_buttons[str(i)] = False
                if str(i) in self.handled_buttons:
                    self.handled_buttons.remove(str(i))
            i += 1

    def change_key_bind(self, action, key):
        self.key_binds[action] = key

    def get_key_down(self, key):
        if key in self.handled_keys:
            return False
        elif key in self.raw_keys.keys():
            if self.raw_keys[key]:
                self.handled_keys.append(key)
                return True
        return False

    def get_key(self, key):
        if key in self.raw_keys:
            return self.raw_keys[key]

    def get_action_down(self, action):
        act = self.actions[action]
        self.actions[action] = False
        return act

    def get_action(self, action):
        return self.actions[action]

    def get_button_down(self, button):
        if button in self.handled_buttons:
            return False
        elif button in self.mouse_buttons.keys():
            if self.mouse_buttons[button]:
                self.handled_buttons.append(button)
                return True
        return False

    def get_button(self, button):
        return self.mouse_buttons[button]

    #def get_mouse_scroll(self, scroll):
    #    non_scroll = self.get_mouse_pos()
    #    return non_scroll[0] + scroll[0], non_scroll[1] + scroll[1]

