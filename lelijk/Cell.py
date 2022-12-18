class Cell:
    def __init__(self):
        self.revealed = False
        self.flagged = False
        self.has_bomb = False
        self.is_exploding_bomb = False
        self.num_adjacent_bombs = 0

    def get_revealed(self):
        return self.revealed

    def get_flagged(self):
        return self.flagged

    def get_bomb(self):
        return self.has_bomb

    def get_adjacent_bombs(self):
        return self.num_adjacent_bombs

    def get_exploding_bomb(self):
        return self.is_exploding_bomb

    def add_adjacent_bomb(self):
        self.num_adjacent_bombs += 1

    def is_hidden(self):
        return not self.revealed

    def set_exploding_bomb(self):
        self.is_exploding_bomb = True

    def put_bomb(self):
        self.has_bomb = True

    def remove_flag(self):
        self.flagged = False

    def reveal(self):
        self.revealed = True

    def flag(self):
        self.flagged = True
