def request_action():
    return input("Write action (buy, fill, take, remaining, exit):")


def pick_type_of_coffee():
    message = \
        "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"
    return input(message)


def add_water():
    return int(input("Write how many ml of water do you want to add:"))


def add_milk():
    return int(input("Write how many ml of milk do you want to add:"))


def add_beans():
    return int(input("Write how many grams of coffee beans do you want to add:"))


def add_cups():
    return int(input("Write how many disposable cups of coffee do you want to add:"))


class CoffeeMachine:
    def __init__(self):
        self.water_avail = 400
        self.milk_avail = 540
        self.beans_avail = 120
        self.cups_avail = 9
        self.money_avail = 550
        self.activity = "choosing action"

    def display_status(self):
        print("The coffee machine has:")
        if self.water_avail > 0:
            print(f"{self.water_avail} of water")
        if self.milk_avail > 0:
            print(f"{self.milk_avail} of milk")
        if self.beans_avail > 0:
            print(f"{self.beans_avail} of coffee beans")
        if self.cups_avail > 0:
            print(f"{self.cups_avail} of disposable cups")
        print(f"{self.money_avail} of money")

    def enough_milk(self, type_coffee):
        if type_coffee == 2 and self.milk_avail < 75:
            return False
        elif type_coffee == 3 and self.milk_avail < 100:
            return False
        return True

    def enough_water(self, type_coffee):
        if type_coffee == "1" and self.water_avail < 250:
            return False
        elif type_coffee == "2" and self.water_avail < 350:
            return False
        elif type_coffee == "3" and self.water_avail < 200:
            return False
        return True

    def enough_beans(self, type_coffee):
        if type_coffee == 1 and self.beans_avail < 16:
            return False
        elif type_coffee == 2 and self.beans_avail < 20:
            return False
        elif type_coffee == 3 and self.beans_avail < 12:
            return False
        return True

    def check_resources(self, type_coffee):
        return self.enough_water(type_coffee) and \
               self.enough_milk(type_coffee) and \
               self.enough_beans(type_coffee) and \
               self.cups_avail >= 1

    def sorry_message(self, type_coffee):
        message = "Sorry, not enough "
        if not self.enough_water(type_coffee):
            print(message + "water!")
        elif not self.enough_milk(type_coffee):
            print(message + "milk!")
        elif not self.enough_beans(type_coffee):
            print(message + "coffee beans!")
        else:
            print(message + "disposable cups!")

    def buy_coffee(self):
        type_of_coffee = pick_type_of_coffee()
        if type_of_coffee == "back":
            return
        enough = self.check_resources(type_of_coffee)
        if enough:
            print("I have enough resources, making you a coffee!")
            if type_of_coffee == "1":
                self.water_avail -= 250
                self.beans_avail -= 16
                self.money_avail += 4
            elif type_of_coffee == "2":
                self.water_avail -= 350
                self.milk_avail -= 75
                self.beans_avail -= 20
                self.money_avail += 7
            else:
                self.water_avail -= 200
                self.milk_avail -= 100
                self.beans_avail -= 12
                self.money_avail += 6
            self.cups_avail -= 1
        else:
            self.sorry_message(type_of_coffee)

    def fill_machine(self):
        self.water_avail += add_water()
        self.milk_avail += add_milk()
        self.beans_avail += add_beans()
        self.cups_avail += add_cups()

    def release_money(self):
        print(f"I gave you ${self.money_avail}")
        self.money_avail = 0

    def operate_machine(self, user_request):
        if user_request == "buy":
            self.buy_coffee()
        elif user_request == "fill":
            self.fill_machine()
        elif user_request == "remaining":
            self.display_status()
        elif user_request == "take":
            self.release_money()


cm = CoffeeMachine()

operating_machine = True
while operating_machine:
    request = request_action()
    if request == "exit":
        operating_machine = False
    else:
        cm.operate_machine(request)
