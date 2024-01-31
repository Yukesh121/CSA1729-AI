class VacuumCleaner:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.position = (0, 0)  # Starting position
        self.direction = 'right'  # Starting direction

    def place_dirt(self, row, col):
        self.grid[row][col] = 'D'

    def move(self):
        row, col = self.position

        # Clean dirt if present
        if self.grid[row][col] == 'D':
            self.grid[row][col] = ' '
            print(f"Cleaned dirt at ({row}, {col})")

        # Move according to direction
        if self.direction == 'right':
            if col < self.cols - 1:
                col += 1
            else:
                self.direction = 'down'
                row += 1
        elif self.direction == 'down':
            if row < self.rows - 1:
                row += 1
            else:
                self.direction = 'left'
                col -= 1
        elif self.direction == 'left':
            if col > 0:
                col -= 1
            else:
                self.direction = 'up'
                row -= 1
        elif self.direction == 'up':
            if row > 0:
                row -= 1
            else:
                self.direction = 'right'
                col += 1

        self.position = (row, col)

    def clean_room(self):
        for _ in range(self.rows * self.cols):
            self.move()
        print("Room cleaned.")


# Example usage
if __name__ == "__main__":
    vacuum = VacuumCleaner(rows=5, cols=5)
    vacuum.place_dirt(1, 1)
    vacuum.place_dirt(2, 3)
    vacuum.clean_room()
