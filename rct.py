class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perameter(self):
        return 2 * (self.width + self.height)

def total_area(rectangles):
    total = 0
    for rect in rectangles:
        total += rect.area()
    return total


r1 = rectangle(4, 5)
r2 = rectangle(10, 15)

my_rectangles = [r1, r2]
print(total_area(my_rectangles))