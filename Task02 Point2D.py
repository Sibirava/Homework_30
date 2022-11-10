class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set(self, x, y, num):
        if isinstance(num,(int,float)):
            self.x += num
            self.y += num
        return self

    def calculate_distance(self):
        return (self.x**2 + self.y**2)**0.5

point1 = Point2D(3, 4)

print(point1.x, point1.y)
print(point1.calculate_distance())

point2 = Point2D()

print(point2.set(5, 5, 2))


