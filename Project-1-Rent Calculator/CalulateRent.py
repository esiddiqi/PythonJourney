# This Program will calculate the Rent and contribution for indivisual Person


tot_rent = int(input("Enter Total Rent Amount: "))
tot_units_spent = int(input("Enter Total Electricity Units Spent: "))
elec_charge = int(input("Enter Per Unit Charge: "))
nop = int(input("Enter No. Of Person to Devide the amount: "))


elec_bill = (tot_units_spent * elec_charge)
calc = (tot_rent + elec_bill)
contri = round((calc / nop ), 2)

print("Each Person will pay: " + str(contri))





# Output:
# Enter Total Rent Amount: 14000
# Enter Total Electricity Units Spent: 250
# Enter Per Unit Charge: 11
# Enter No. Of Person to Devide the amount: 7
# Each Person will pay: 2392.86
