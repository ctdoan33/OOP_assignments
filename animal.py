if __name__=="animal":
    class Animal(object):
        def __init__(self, name, health):
            self.name = name
            self.health = health
        def walk(self):
            self.health -= 1
            return self
        def run(self):
            self.health -= 5
            return self
        def display_health(self):
            print self.health
            return self
        def __repr__(self):
            return "<Animal object Name: {} Health: {}>".format(self.name, self.health)
    class Dog(Animal):
        def __init__(self):
            self.health = 150
        def pet(self):
            self.health += 5
            return self
        def __repr__(self):
            return "<Dog object Health: {}>".format(self.health)
    class Dragon(Animal):
        def __init__(self):
            self.health = 170
        def fly(self):
            self.health -= 10
            return self
        def display_health(self):
            super(Dragon, self).display_health()
            print "I am a Dragon"
            return self
        def __repr__(self):
            return "<Dragon object Health: {}>".format(self.health)