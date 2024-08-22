# Simple Interest calculator
# This will take user input as Principle, Rate of interest, Time in Years


principle = int(input("Enter Principle Amount: "))
roi = int(input("Enter Rate of Interest: "))
time = int(input("Enter time in Years:"))

totalintrest = float((principle * roi * time) / 100)
totalamount = float(totalintrest + principle)
print("Total Interest: " + str(totalintrest))

print("Total amount to pay: " + str(totalamount))