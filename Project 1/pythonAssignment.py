#Import necessary modules
import time
import math
import random

#Declare variables
gems = 0
boxes = 0
boxes_opened = 0
total_spent = 0
cost = 100
items = []

#Open box function
def open_box(num_items):
    print("\nOpening loot box:")
    rarities = []
    #Random item generator
    for i in range(num_items):
        #Generate a random number between 1 and 100
        n = random.randint(1, 100)
        time.sleep(1)
        #if 'n' is less then or equal to 5, execute resposne. Repeated for each condition if true
        if n <= 5:
            #Display item number and total, aswell as item raritiy obtained. Repeated for each condition if true 
            print("Item", i + 1, "of", num_items, "... Legendary item!")
            #Add 'Legendary' to the rarities list. Repeated for each condition if true
            rarities.append('Legendary')
        elif n <= 15:
            print("Item", i + 1, "of", num_items, "... Epic item!")
            rarities.append('Epic')
        elif n <= 50:
            print("Item", i + 1, "of", num_items, "... Rare Item!")
            rarities.append('Rare')
        else:
            print("Item", i + 1, "of", num_items, "... Common Item!")
            rarities.append('Common')
    return rarities

#Display a welcone message
print("Welcome to the Lootbox Simulator!")

while True:
    #Display current amount of 'gems', 'boxes' and cost.
    #
    print("You currently have", gems, "gems and", boxes, "loot boxes!\nPlease Choose from one of the options below:")
    print("1. Buy Gems (550 gems for $19.95)\n2. Buy loot box (for only", cost, "gems)\n3. Open loot box\n4. View Record\n5. Exit Simulator")

    #Prompt user input, equal to 'choice'
    choice = input("Choose your option: ")
    #Buy Gems
    if choice == '1':
        gems += 550
        total_spent += 19.95
        print("\nYou have purchased 550 gems!\nThank you for your purchase")
        time.sleep(0.8)
    #Buy Boxes
    elif choice == '2':
        if gems >= cost:
            gems = gems - cost
            boxes += 1
            print("\nYou have purchased 1 loot box!")
            time.sleep(0.8)

        else:
            print("\nInsufficent Funds, purchase more gems")
            time.sleep(0.8)
    #Run loot box simulator function
    elif choice == '3':
        if boxes >= 1:
            time.sleep(0.8)
            rarities = open_box(num_items = 4)
            items.extend(rarities)
            boxes_opened += 1
            boxes -= 1
        else:
            print("\nThere are no loot boxes!")
            time.sleep(0.8)
    #Display stats/record
    elif choice == '4':
        print("\nTotal spendings: $", format(total_spent, ',.2f'))
        print("Loot boxes opened: ", boxes_opened)
        print("Total Items:     ", len(items))
        print("Common items:    ", items.count('Common'), "(", round(items.count('Common') / (len(items)) * 100 if len(items) > 0 else 0, 2), "%)")
        print("Rare items:      ", items.count('Rare'), "(", round(items.count('Rare') / (len(items)) * 100 if len(items) > 0 else 0, 2), "%)")
        print("Epic items:      ", items.count('Epic'), "(", round(items.count('Epic') / (len(items)) * 100 if len(items) > 0 else 0, 2), "%)")
        print("Legendary items: ", items.count('Legendary'), "(", round(items.count('Legendary') / (len(items)) * 100 if len(items) > 0 else 0, 2), "%)")
        time.sleep(0.8)
    #Close/end simulator
    elif choice == '5':
        print("Closing Simulator")
        time.sleep(3)
        break

    #Otherwise, display error message
    else:
        print("\nInvalid Choice")
        time.sleep(0.8)

    print("")
