def can_quack(animal):
    return animal.can_quack()


class Animal(object):
    def can_quack(self):
        pass


class Duck(Animal):
    def can_quack(self):
        return True


class Snake(Animal):
    def can_quack(self):
        return False


class Platypus(Animal):
    def can_quack(self):
        return True


if __name__ == '__main__':
    print(can_quack(Duck()))
    print(can_quack(Snake()))
    print(can_quack(Platypus()))
