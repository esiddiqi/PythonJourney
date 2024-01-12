# Print the line "Emaad You are Awesome, Your Age is 30" using diffrent print syntax

name = "Emaad"
age = 30
quality = "Awesome"

print(name + " You are " + quality + ", Your Age is " + str(age))   #The basic way
print(f"{name} You are {quality}, Your Age is {age}")               #The cool Way
print("{} You are {}, Your Age is {}".format(name,quality,age))     #The logical Way
print(name, "You are", quality,", Your Age is", age)                #The hot way



#
# Output :
#
# Emaad You are Awesome, Your Age is 30
# Emaad You are Awesome, Your Age is 30
# Emaad You are Awesome, Your Age is 30
# Emaad You are Awesome , Your Age is 30





