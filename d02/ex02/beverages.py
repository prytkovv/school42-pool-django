class HotBeverage(object):

    name = 'hot beverage'
    price = 0.30

    def description(self):
        return 'Just some water in a cup'

    def __str__(self) -> str:
        return "name: %s\nprice price: %.2f\ndescription: %s" % (
            self.name, self.price, self.description())


class Coffee(HotBeverage):

    name = 'coffee'
    price = 0.40

    def description(self):
        return 'A coffee, to stay awake.'


class Tea(HotBeverage):

    name = "tea"


class Chocolate(HotBeverage):

    name = 'chocolate'
    price = 0.50

    def description(self):
        return 'Chocolate, sweet chocolate'


class Cappuccino(HotBeverage):

    name = 'cappuccino'
    price = 0.45

    def description(self):
        return 'Un po’ di Italia nella sua tazza!'


hotBeverage = HotBeverage()
coffee = Coffee()
tea = Tea()
chocolate = Chocolate()
cappuccino = Cappuccino()
print(hotBeverage, coffee, tea, chocolate, cappuccino, sep='\n')
