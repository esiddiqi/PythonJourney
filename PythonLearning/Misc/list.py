def main():


    aws_services = ["S3", "Lambda", "RDS", "EC2", "VPC"]
    print(f"AWS Services list: {aws_services}")
    first_item = aws_services[0]
    print(f"First Item in the list : {first_item}")
    last_item = aws_services[-1]
    print(f"Last Item in the list: {last_item}")



    # # Modify the last Service
    # aws_services[-1] = "VPC"
    # print(aws_services)

    # # Remove Second value from the list
    # aws_services.pop(1)
    # print (aws_services)


    # del aws_services[1]
    # print(aws_services)


    #print Services form 1 to 3
    print(f"{aws_services[1:3]}")


    # find lenght of the list
    print(f"Length of the list: {len(aws_services)}")











if __name__ == "__main__":
    main()