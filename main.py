import numpy as np
import random
from state import State


class Puzzle:
    def __init__(self, x: int = 3, y: int = 3):
        self.x = x
        self.y = y

    def selectRandom(self, availableNumbers: list) -> int:
        if not availableNumbers:
            return None
        element = random.choice(availableNumbers)
        availableNumbers.remove(element)
        return element

    def generateInitialState(self) -> np.ndarray:
        rng = np.random.default_rng()
        availableNumbers = list(range(1, self.x * self.y))
        array = np.array(
            [
                [self.selectRandom(availableNumbers) for i in range(self.x)]
                for j in range(self.y)
            ]
        )
        return array

    def generateGoalState(self) -> np.ndarray:
        print("")


if __name__ == "__main__":
    puzzle = Puzzle()
    print(puzzle.generateInitialState())
