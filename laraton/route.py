from dataclasses import dataclass
from typing import Type


class Route:

    def __init__(self, pattern, controller, method, *args, **kwargs):
        self.pattern = pattern
        self.controller = controller
        self.method = method

    def name(self, name):
        self.name = name
