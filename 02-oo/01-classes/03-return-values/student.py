#!/usr/bin/python3

class Wall:
    armor = 10
    height = 5

    def get_cost(self) -> int:
        return self.armor * self.height

    def fortify(self):
        self.armor *= 2