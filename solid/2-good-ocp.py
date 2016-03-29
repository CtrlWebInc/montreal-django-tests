class QuackFlapFactory:
    def create():
        rules = [QuackFlapRule(), FlapRule(), QuackRule(), NormalRule()]
        return QuackFlap(rules)
    create = staticmethod(create)


class QuackFlap:
    def __init__(self, rules):
        self.rules = rules

    def say(self, x):
        for rule in self.rules:
            if rule.is_handled(x):
                return rule.say(x)


class Rule:
    def is_handled(self, x):
        pass

    def say(self, x):
        pass


class NormalRule(Rule):
    def is_handled(self, x):
        return True

    def say(self, x):
        return x


class QuackRule(Rule):
    def is_handled(self, x):
        return x % 3 == 0

    def say(self, x):
        return "Quack!"


class FlapRule(Rule):
    def is_handled(self, x):
        return x % 5 == 0

    def say(self, x):
        return "*Flap*"


class QuackFlapRule(Rule):
    def is_handled(self, x):
        return x % 5 == 0 and x % 3 == 0

    def say(self, x):
        return "Quack! *Flap*"


if __name__ == '__main__':
    quack_flap = QuackFlapFactory.create()
    for i in range(1, 46):
        print(quack_flap.say(i))
