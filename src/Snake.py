from variables import INITIAL_SIZE, INITIAL_POSITION


class Snake:
    size: int
    head_position: list

    def __init__(self):
        self.size = INITIAL_SIZE
        self.head_position = INITIAL_POSITION  # Need to find a way to allow the removal of tail and addition at head
