class Info:
    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {
            "name": self.name,
        }



class Classic(Info):
    def __init__(self, name, genre):
        super().__init__(name)
        self.genre = genre

    def to_dict(self): 
        Classic.to_dict = super().to_dict()
        Classic.to_dict.update({"genre": self.genre})
        return Classic.to_dict


class Rock(Info):
    def __init__(self, name, genre):
        super().__init__(name)
        self.genre = genre

    def to_dict(self):
        Rock.to_dict = super().to_dict()
        Rock.to_dict.update({"genre": self.genre})
        return Rock.to_dict

    

class Pop(Info):
    def __init__(self, name, genre, long):
        super().__init__(name)
        self.genre = genre
        self.long = long

    def to_dict(self):
        Pop.to_dict = super().to_dict()
        Pop.to_dict.update({"genre": self.genre})
        Pop.to_dict.update({"long": self.long})
        return Pop.to_dict

    

class Rap(Info):
    def __init__(self, name, genre, long, pip):
        super().__init__(name)
        self.genre = genre
        self.long = long
        self.pip = pip

    def to_dict(self):
        Rap.to_dict = super().to_dict()
        Rap.to_dict.update({"genre": self.genre})
        Rap.to_dict.update({"long": self.long})
        Rap.to_dict.update({"pip": self.pip})
        return Rap.to_dict

    