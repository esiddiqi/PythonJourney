

my_details = {
    "name": "Emaad",
    "YOB": "1994",
    "cities": ["pune", "mumbai"]
}


# print(my_details["YOB"])
# print(my_details["cities"][1])


#
#
# for key in my_details:
#     print(f"{key} : {my_details[key]}")

# test = my_details.items()
# print(test)
#
# for key,value in my_details.items():
#     print(key, value)


# Add Items in dictionary


my_details["occupation"] = 'DevOps Engineer'
print(my_details)


del my_details['YOB']

print("\n After delete")
print(my_details)
