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
    duck = Duck()
    print(duck.can_quack())

    snake = Snake()
    print(snake.can_quack())

    platypus = Platypus()
    print(platypus.can_quack())
