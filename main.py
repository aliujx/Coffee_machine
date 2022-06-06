from menu import drinks, resources

resources['money'] = 0


def resources_left():
    global water
    global milk
    global coffee
    global cost
    resources['water'] -= drinks[user_choice]['ingredients']['water']
    if user_choice != 'espresso':
        resources['milk'] -= drinks[user_choice]['ingredients']['milk']
    resources['coffee'] -= drinks[user_choice]['ingredients']['coffee']
    resources['money'] += drinks[user_choice]['cost']
    return resources


def report():
    global water
    global milk
    global coffee
    global cost
    if resources['money'] == 0:
        for key, value in resources.items():
            if value == 'money':
                print(f"{key.title()}: ${value}")
            elif value == 'coffee':
                print(f"{key.title()}: {value}gr")
            elif value == 'water' or value == 'milk':
                print(f"{key.title()}: {value}ml")
    else:
        resources_left()



def check_resources():
    global water
    global milk
    global coffee
    for ingredient in drinks[user_choice]['ingredients']:
        if drinks[user_choice]['ingredients'][ingredient] > resources[ingredient]:
            return f"Sorry, that's not enough {ingredient}"
            break


quarter = 0.25
dime = 0.1
nickle = 0.05
penny = 0.01

should_work = True

while should_work:
    user_choice = input("  What would you like? (espresso/latte /cappuccino): ").lower()
    if user_choice == "off":
        should_work = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gr")
        print(f"Money: ${resources['money']}")
    else:
        check_resources()
        if check_resources():
            print(check_resources())

        else:
            price = drinks[user_choice]['cost']
            print(f"{user_choice} costs ${price}")

            print("Please insert coins.")
            insert_quarter = int(input("how many quarters?: "))
            insert_dime = int(input("how many dimes?: "))
            insert_nickle = int(input("how many nickles?: "))
            insert_penny = int(input("how many pennies?: "))
            user_paid = round(insert_quarter * quarter + insert_dime * dime + insert_nickle * nickle + insert_penny * penny,
                                  2)

            #print(user_paid)

            if user_paid < price:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                change = round(user_paid - price, 2)
                print(f"Here's ${change} in change.")
                print(f"Here's your {user_choice}. ☕ Enjoy!")
                resources_left()

