class Circle:
    def __init__(self, radius):
        self.radius = float(radius)
        

    def area(self):
        result = (3.14 * (self.radius*self.radius))
        return result

    def circumference(self):
        ans = 2* 3.14 * self.radius
        return ans


radius=float(input())

circle = Circle(radius)

print(circle.area())
print(circle.circumference())
