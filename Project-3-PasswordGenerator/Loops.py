

#
#
# # Learning loops
#
#
# mobile = ['iPhone', 'Samsung', 'Nokia', 'Motorola', 'MI']
#
# for models in mobile:
#     print(models)
# print("For Loops ended here")



bolt_runs = [11.53, 10.8, 9.43, 9.53, 10.05, 8.06, 9.89]



min = bolt_runs[0]
for i in bolt_runs:
    if i < min:
        min = i

print(f"Minimum Number is = {min}")


max = bolt_runs[0]
for i in bolt_runs:
    if i > max:
        max = i
print(f"Maximum Number is = {max}")

sum = sum(bolt_runs)
print(f"sum = {sum}")


# len = len(bolt_runs)
# print(len)
average = sum / len(bolt_runs)
print(f"Average is = {average}")










