# def welcome():
#     print("Welcome Brothers")
#     print("Well Done")
#
#
# welcome()


# def sqaure(num):
#     print(num * num)
# sqaure(3)


#Write a program to sum n numbers using a function (Use tuples)

def get_sum(*n):
    sum = 0
    for i in n:
        sum = sum + i
    return sum



sum = get_sum(1,2,3,4,5)
print(sum)








