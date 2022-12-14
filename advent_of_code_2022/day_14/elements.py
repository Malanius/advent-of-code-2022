from dataclasses import dataclass

from advent_of_code_2022.day_14.direction import Direction


class Element:
    pass


class SandGenerator(Element):
    def __str__(self) -> str:
        return "+"


class Rock(Element):
    def __str__(self) -> str:
        return "#"


@dataclass
class Air(Element):
    visited: bool = False

    def __str__(self) -> str:
        return "~" if self.visited else "."


@dataclass
class Sand(Element):
    coords: tuple[int, int]
    is_resting: bool = False

    def __str__(self) -> str:
        return "o" if self.is_resting else "*"

    def can_move_to(self, element: Element) -> bool:
        if isinstance(element, Air):
            return True
        if isinstance(element, Sand):
            return not element.is_resting
        return False

    def move(self, direction: Direction):
        x, y = self.coords
        if direction == Direction.DOWN:
            self.coords = (x, y + 1)
        elif direction == Direction.DOWN_LEFT:
            self.coords = (x - 1, y + 1)
        elif direction == Direction.DOWN_RIGHT:
            self.coords = (x + 1, y + 1)