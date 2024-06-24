# print 9 box
# choose 1 box randomly with treasure (by Computer)
# give user 3 chances to get that box

#FIND THE FIRE

import random
import sys

row1 = ['🙂', '🙂', '🙂']
row2 = ['🙂', '🙂', '🙂']
row3 = ['🙂', '🙂', '🙂']


#take it as nested list
map = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')



auto_choice = random.choice([11,12,13,21,22,23,31,32,33])
#print(auto_choice)





user_input = input("Enter 1st Choice:")
row = int(user_input[0])-1     #since list starts with zero
column = int(user_input[1])-1
if int(user_input) == auto_choice:
    print("YOU WON !!!!!!")
    map[row][column] = '🔥'
    print(f'{row1}\n{row2}\n{row3}')
    sys.exit()

map[row][column] = '😎'       # Updating users 1st choice
print(f'{row1}\n{row2}\n{row3}')




user_input = input("Enter 2nd Choice:")
row = int(user_input[0])-1
column = int(user_input[1])-1

if int(user_input) == auto_choice:
    print("YOU WON !!!!!!")
    map[row][column] = '🔥'
    print(f'{row1}\n{row2}\n{row3}')
    sys.exit()

map[row][column] = '😎'    # Updating users 2nd choice
print(f'{row1}\n{row2}\n{row3}')



user_input = input("Enter 3rd Choice:")
row = int(user_input[0])-1
column = int(user_input[1])-1
if int(user_input) == auto_choice:
    print("YOU WON !!!!!!")
    map[row][column] = '🔥'
    print(f'{row1}\n{row2}\n{row3}')
    sys.exit()

map[row][column] = '😎'    # Updating users 3rd choice
print(f'{row1}\n{row2}\n{row3}')






# print(f"User has choosen Row as {row} and column as {column}")




