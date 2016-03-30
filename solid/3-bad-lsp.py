class Animal(object):
    pass


class Duck(Animal):
    pass


class Snake(Animal):
    pass


class Platypus(Animal):
    pass


def can_quack(animal):
    if isinstance(animal, Duck):
        return True
    elif isinstance(animal, Snake):
        return False
    else:
        raise RuntimeError('Unknown animal!')


if __name__ == '__main__':
    print(can_quack(Duck()))
    print(can_quack(Snake()))
    print(can_quack(Platypus()))
