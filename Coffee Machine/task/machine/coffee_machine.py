water_available = 0
milk_available = 0
coffee_beans_available = 0
cups_available = 0
money_available = 0

def get_num_drinks():
    # return int(input("Write how many cups of coffee you will need"))
    return int(input())


def get_ml_water_needed_per_drink():
    return 200


def get_ml_milk_needed_per_drink():
    return 50


def get_grams_beans_drink_per_drink():
    return 15


def get_ml_water_available():
    return int(input("Write how many ml of water the coffee machine has:"))


def get_ml_milk_available():
    return int(input("Write how many ml of milk the coffee machine has:"))


def get_grams_beans_available():
    return int(input("Write how many grams of coffee beans the coffee machine has:"))


def get_num_drinks_possible(water_available, milk_available, beans_available):
    water_factor = water_available / get_ml_water_needed_per_drink()
    milk_factor = milk_available / get_ml_milk_needed_per_drink()
    beans_factor = beans_available / get_grams_beans_drink_per_drink()

    least = min(water_factor, milk_factor)
    least = min(beans_factor, least)

    return least


def response(num_drinks_wanted, num_drinks_possible):
    if num_drinks_possible >= num_drinks_wanted:
        extra_drinks = num_drinks_possible - num_drinks_wanted
        extra_drinks = max(0, extra_drinks)
        extra_text = f" and even {extra_drinks} more than that"
        basic_text = "Yes, I can make that amount of coffee"
        if extra_drinks:
            print(basic_text + extra_text)
        else:
            print(basic_text)
    else:
        print(
            f"No, I can only make {num_drinks_possible} cups of coffee")


def activate_coffee_machine():
    water_available = get_ml_water_available()
    milk_available = get_ml_milk_available()
    beans_available = get_grams_beans_available()
    cups_available = get_cups_available()
    money_available = get_money_available()
    num_drinks_wanted = get_num_drinks()

    num_drinks_possible = int(get_num_drinks_possible(water_available,
                                                      milk_available,
                                                      beans_available))
    response(num_drinks_wanted, num_drinks_possible)


activate_coffee_machine()
