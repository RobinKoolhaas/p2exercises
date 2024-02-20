#!/usr/bin/python3

class Wall:
    def __init__(self, depth: int, height: int, width: int) -> None:
        self.depth = depth
        self.height = height
        self.width = width
        self.volume = self.width * self.height * self.depth
