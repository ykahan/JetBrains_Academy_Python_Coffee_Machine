class Turtle:
    def __init__(self, x, y):
        # the initial coordinates of the turtle
        self.x = x
        self.y = y

    def move_up(self, n):
        self.y += n

    def move_down(self, n):
        self.y = 0 if n > self.y else self.y - n

    def move_right(self, n):
        self.x += n

    def move_left(self, n):
        self.x = 0 if n > self.x else self.x - n

leo = Turtle(1, 1)
leo.move_up(7)
leo.move_left(5)
leo.move_down(4)
leo.move_right(6)
print(leo.x)
print(leo.y)

cents = 157
print(cents // 100)