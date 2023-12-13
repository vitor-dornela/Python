class Point:
    # the constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # custom method
    def dist(self, p2):
        print("O self é: ", self.x, self.y)
        print("O p2 é: ", p2.x, p2.y)
        return ((self.x-p2.x)**2+(self.y-p2.y)**2)**0.5

    def dist2(self, p2):
        return ((p1.x-p2.x)**2+(p1.y-p2.y)**2)**0.5

p1 = Point(1.5, 1)
print(p1.x, p1.y)

p2 = Point(1.5, 2)
print(p2.x, p2.y)


print(p1.dist(p2))  # 1.0      
print(Point.dist2(p1,p2)) # 1.0 alternative calling object method