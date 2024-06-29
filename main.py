import numpy as np
from state import State


class Puzzle:
    def __init__(self, x: int = 3, y: int = 3):
        self.x = x
        self.y = y

    def generateInitialState(self) -> np.ndarray:
        availableNumbers = np.arange(1, self.x * self.y)
        array = np.array(
            [
                [
                    State(np.random.choice(availableNumbers), (i, j))
                    for i in range(self.x)
                ]
                for j in range(self.y)
            ]
        )
        array

    def generateGoalState(self) -> np.ndarray:
        print("")


if __name__ == "__main__":
    puzzle = Puzzle()
    print(puzzle.generateInitialState().shape)
