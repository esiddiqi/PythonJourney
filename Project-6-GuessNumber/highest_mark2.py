

marks = {
    "Emaad": [98,45,12],
    "Superman": [32,54,87],
    "Deadpool": [34,65,98]
}

topper = ""
largest_score = -1
total_marks = []
for key,value in marks.items():
    addition = sum(value)
    print(key, addition)
    if addition > largest_score:
        largest_score = addition
        topper = key



print(f"\n {topper} is the Topper !!! With highest Score of {largest_score} !!!")








#    total_marks.append(addition)



# print(total_marks)
# largest_score = max(total_marks)
# print(f"Largest Score is: {largest_score}")



#print(total_marks)
#
#
# topper["top1"] = largest_score
# print(topper)



# print(f"Top Performer is {largest_score}")










# marks = input("Enter the Details for student 1 for English, Hindi, Urdu")
#
# for key in student1_marks:



