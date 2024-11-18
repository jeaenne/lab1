class Info:
    def __init__(self, name):
        self.name = name

    def Name(self):
        return {
            "name": self.name,
        }

    def __m2__(self):
        return f"Название: {self.name}\n"


class Classic(Info):
    def __init__(self, name, genre):
        super().__init__(name)
        self.genre = genre

    def name(self): 
        Classic.Name = super().Name()
        Classic.Name.update({"genre": self.genre})
        return Classic.Name

    def __m2__(self):
        return f"Название: {self.name}\n Жанр: {self.genre}\n"


class Rock(Info):
    def __init__(self, name, genre):
        super().__init__(name)
        self.genre = genre

    def Name(self):
        Rock.Name = super().Name()
        Rock.Name.update({"genre": self.genre})
        return Rock.Name

    def __m2__(self):
        return f"Название: {self.name}\n Жанр: {self.genre}\n"


class Pop(Info):
    def __init__(self, name, genre, long):
        super().__init__(name)
        self.genre = genre
        self.long = long

    def Name(self):
        Pop.Name = super().Name()
        Pop.Name.update({"genre": self.genre})
        Pop.Name.update({"long": self.long})
        return Pop.Name

    def __m2__(self):
        return f"Название: {self.name}\n Жанр: {self.genre}\n Длительность: {self.long} сек\n"


class Rap(Info):
    def __init__(self, name, genre, long, pip):
        super().__init__(name)
        self.genre = genre
        self.long = long
        self.pip = pip

    def Name(self):
        Rep.Name = super().Name()
        Rep.Name.update({"genre": self.genre})
        Rep.Name.update({"long": self.long})
        Rep.Name.update({"pip": self.pip})
        return Rep.Name

    def __m2__(self):
        return f"Название: {self.name}\n Жанр: {self.genre}\n Длительность: {self.long} сек\n Исполнитель:{self.pip}"