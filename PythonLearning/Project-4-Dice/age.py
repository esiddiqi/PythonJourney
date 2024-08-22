

def check_age(name='Mr. Unknown', age='0'):  #--> Keyword arguments
    if age < 18:
        print(f"hey {name}, You can't have the bear, Grow UP Fastt !!")
    else:
        print(f"Hey {name}, You are Welcome, Which beer you Want?")



n = input("Enter your name: ")
a = int(input("Please Enter you Age: "))


check_age(name=n, age=a)

