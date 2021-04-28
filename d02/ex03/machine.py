import random
import beverages


class CoffeeMachine(object):

    def __init__(self):
        self.beverage_counter = 0

    class EmptyCup(beverages.HotBeverage):

        name = 'empty cup'
        price = 0.90

        def description(self):
            return 'An empty cup?! Gimme my money back!'

    class BrokenMachineException(Exception):

        def __init__(self):
            self.message = 'This coffee machine has to be repaired'

        def __str__(self):
            return self.message

    def repair(self):
        self.beverage_counter = 0

    def serve(self, beverage: beverages.HotBeverage):

        if self.beverage_counter < 9:
            prepared_beverage = (beverage
                if random.randint(0, 1) == 0
                else self.EmptyCup())
            self.beverage_counter += 1
        else:
            raise self.BrokenMachineException()
        return prepared_beverage


if __name__ == '__main__':
    coffee_machine = CoffeeMachine()
    for i in range(10):
        try:
            print(coffee_machine.serve(beverages.Coffee()))
            print(coffee_machine.serve(beverages.Tea()))
            print(coffee_machine.serve(beverages.Chocolate()))
            print(coffee_machine.serve(beverages.Cappuccino()))
        except coffee_machine.BrokenMachineException as e:
            print(e)
            coffee_machine.repair()
            print('Coffee machine is repaired sucessfully!')





