import time
import math
import sys
import random

gems = 0
boxes = 0
boxes_opened = 0
total_spent = 0
cost = 150
items = ["Common", "Rare", "Epic", "Legendary"]

def open_box():
    print("Opening loot box:")
    if boxes > 0:
        for i in range(4):
            n = random.randint(1, 100)
            time.sleep(1)
            if n >= 1 and n <= 5:
                print("Item", i, "of 4 ... ", items[3])
            elif n >= 6 and n <= 15:
                print("Item", i, "of 4 ... ", items[2])
            elif n >= 16 and n <= 50:
                print("Item", i, "of 4 ... ", items[1])
            else:
                print("Item", i, "of 4 ... ", items[0])
    else:
        print("There are no boxes")


print("Welcome to the Lootbox Simulator!")

while True:

    print("You currently have", gems, "gems and", boxes, "loot boxes!\nPlease Choose from one of the options below:")
    print("1. Buy Gems (500 gems for $14.95)\n2. Buy loot box\n3. Open loot box\n4. View Record\n5. Exit Simulator")

    choice = input("Choose your option: ")

    if choice == '1':
        gems += 500
        total_spent += 14.95
        print("You have purchased 500 gems!")

    elif choice == '2':
        if gems >= cost:
            gems = gems - cost
            boxes += 1
            print("You have prucahsed 1 loot box\nYou currently have", boxes, "loot boxes")

        else:
            print("Insufficent Funds, purchase more gems")

    elif choice == '3':
        if boxes >= 1:
            boxes_opened += 1
            boxes -= 1
            open_box()
        else:
            print("\nThere are no loot boxes!")
            time.sleep(2)

    elif choice == '4':
         print("Total spendings: ", total_spent, "\nLoot boxes opened: ",
               boxes_opened, "\nLegendary Items: ", items.count('Common'),
               "(", print(((items.count('Common') / (boxes_opened * 4))*100), "%)"))

    elif choice == '5':
        print("Closing Simulator")
        print(items.count(items[3]))
        time.sleep(3)
        exit()

    else:
        print("Invalid Choice")

    print("")
    print("")
