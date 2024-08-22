

marks = {
    "Emaad": [98,45,12],
    "Zainab": [32,54,87],
    "Mariyam": [34,65,98]
}

total_marks = []
for key,value in marks.items():
#    print(value)
    addition = sum(value)
    print(addition)
    total_marks.append(addition)


print(total_marks)

largest_score = max(total_marks)
print(f"Top Performer is {largest_score}")








# marks = input("Enter the Details for student 1 for English, Hindi, Urdu")
#
# for key in student1_marks:



