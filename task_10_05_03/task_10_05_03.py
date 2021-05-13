class PaintingObject:
    """Создает пишущий обьект"""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"OMG! This is {self.name}!"

    def write(self, anything):
        return f"{self.name} write {anything}"


class Pen(PaintingObject):
    """Создает пишущий обьект Pen"""
    def __init__(self):
        super().__init__("Pen")

    def __str__(self):
        return f"this is {self.name}!"


class Pencil(PaintingObject):
    """Создает пишущий обьект Pencil"""
    def __init__(self):
        super().__init__("Pencil")


class TheGelPen(PaintingObject):
    """Создает пишущий обьект TheGelPen"""
    def __init__(self):
        super().__init__("The Gel Pen")

print(TheGelPen().write(" GHbdf"))