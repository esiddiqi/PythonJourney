import random

#Generating Password by taking inputs from user


letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbol = ['!','@','$','%','^','~']
digits = [0,1,2,3,4,5,6,7,8,9]


choice_letter = int(input("Enter number of letters you want to use for your password"))
choice_symbol = int(input("Enter Number of Symbols you want to use for your password"))
choice_digit = int(input("Enter how many digits you want to use for your password"))

print(type(choice_symbol))

password_list = []


for i in range(0, choice_symbol):
    password_list.append(random.choice(symbol))

for i in range(0, choice_letter):
    password_list.append(random.choice(letter))

for i in range(0, choice_digit):
    password_list.append(random.choice(digits))


random.shuffle(password_list)
print(password_list)


