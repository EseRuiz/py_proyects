class Queen:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        if self.row < 0:
            raise ValueError("row not positive")
        if self.row > 7:
            raise ValueError("row not on board")
        if self.column < 0:
            raise ValueError("column not positive")
        if self.column > 7:
            raise ValueError("column not on board")

    def can_attack(self, another_queen):
        if (self.row, self.column )== (another_queen.row,another_queen.column):
            raise ValueError("Invalid queen position: both queens in the same square")
        if self.row == another_queen.row:
            return True
        if self.column == another_queen.column:
            return True
        if self.column - self.row ==  another_queen.column - another_queen.row:
            return True
        if self.column + self.row ==  another_queen.column + another_queen.row:
            return True
        return False