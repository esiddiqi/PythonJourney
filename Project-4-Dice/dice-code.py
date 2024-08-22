import dice
import subprocess
import os





while True:

    user_choice = int(input("Enter number of dice: "))
    os.system("clear")
    if user_choice == 0:
        break
    dice.get_dice(user_choice)








