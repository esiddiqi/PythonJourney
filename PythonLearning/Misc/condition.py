def main():
    user_input = input("Enter Requirement so that i can suggest you the AWS service: ")
    user_requirement = user_input.lower()
    print(user_requirement)




    if user_requirement == 'serverless':
     aws_service = "Labmda"
    elif user_requirement == "storage":
     aws_service = "S3, EBS, EFS"
    elif user_requirement == "database":
       aws_service = "RDS"
    else:
       print("Input Incorrect")
       return


    print(f"You may use {aws_service} for achiving your goal")








if __name__ == "__main__":
    main()
