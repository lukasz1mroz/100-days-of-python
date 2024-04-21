MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

while True:
    action = input("What would you like (espresso/latte/cappuccino)? ")

    if action in MENU:
        for ingredient in MENU[action]['ingredients']:
            if resources[ingredient] < resources[ingredient]:
                print(f"Sorry, not enough {ingredient}")
                continue

        print("Please insert coins")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        coinSum = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)
        price = MENU[action]['cost']

        if coinSum < price:
            print("Not enough money, returned")
        else:
            for ingredient in MENU[action]['ingredients']:
                resources[ingredient] -= MENU[action]['ingredients'][ingredient]
            if coinSum > price:
                print(f'Here is ${coinSum} in change')
            print("Here is your coffee, enjoy!")
    elif action == 'off':
        break
    elif action == 'report':
        for resource in resources:
            print(f"{resource.capitalize()}: {resources[resource]}")