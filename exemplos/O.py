from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Exemplo de uso
shapes = [Rectangle(5, 4), Circle(3)]
for shape in shapes:
    print(f"Área da forma: {shape.area()}")]


# Neste exemplo a classe Shape, podee ser extendida de forma variada, e não pode ser alterada, tendo em vista que o seu método é abstrato
