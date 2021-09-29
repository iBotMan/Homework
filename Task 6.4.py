# Task 6.4
# Create hierarchy out of birds.
# Implement 4 classes:
# * class `Bird` with an attribute `name` and methods `fly` and `walk`.
# * class `FlyingBird` with attributes `name`, `ration`, and with the same methods. `ration` must have default value.
# Implement the method `eat` which will describe its typical ration.
# * class `NonFlyingBird` with same characteristics but which obviously without attribute `fly`.
# Add same "eat" method but with other implementation regarding the swimming bird tastes.
# * class `SuperBird` which can do all of it: walk, fly, swim and eat.
# But be careful which "eat" method you inherit.

#Implement str() function call for each class.

# Example:
# b = Bird("Any")
# b.walk()
# "Any bird can walk"

# p = NonFlyingBird("Penguin", "fish")
# p.swim()
# "Penguin bird can swim"
# p.fly()
# AttributeError: 'Penguin' object has no attribute 'fly'
# p.eat()
# "It eats mostly fish"

# c = FlyingBird("Canary")
# str(c)
# "Canary can walk and fly"
# c.eat()
# "It eats mostly grains"

# s = SuperBird("Gull")
# str(s)
# "Gull bird can walk, swim and fly"
# s.eat()
# "It eats fish"


class Bird:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"I AM: {self.__class__} name: {self.name}"

    def fly(self):
        print(f"{self.name}: I'm flying")

    def walk(self):
        print(f"{self.name}: I'm walking")


class FlyingBird(Bird):
    def __init__(self, name, ration="grains"):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        print(f"{self.name}: just eat {self.ration}, mute-mute")


class NonFlyingBird(FlyingBird, Bird):
    def __init__(self, name, ration="fish"):
        super().__init__(name, ration)

    def swim(self):
        print(f"{self.name} bird can swim")

    def fly(self):
        try:
            raise AttributeError(f"{self.name} object has no attribute 'fly'")
        except Exception as exc:
            print(exc)


class SuperBird(NonFlyingBird, FlyingBird):
    def __init__(self, name, ration="any food"):
        super().__init__(name, ration)


def main():
    b = Bird("Any")
    b.walk()
    # "Any bird can walk"

    p = NonFlyingBird("Penguin", "fish")
    p.swim()
    # "Penguin bird can swim"
    p.fly()
    #AttributeError: 'Penguin' object has no attribute 'fly'
    p.eat()
    # "It eats mostly fish"

    c = FlyingBird("Canary")
    str(c)
    # "Canary can walk and fly"
    c.eat()
    # "It eats mostly grains"

    s = SuperBird("Gull")
    str(s)
    # "Gull bird can walk, swim and fly"
    s.eat()
    # "It eats fish"


if __name__ == '__main__':
    main()

