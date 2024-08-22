
# in this program, Emaad is Showcasing the use of loops in Python 

def main():
    


    aws_services = ["S3", "Lambda", "RDS", "EC2", "VPC"]                           # Define List of AWS Service
    aws_feature = ["storage", "servlerless", "atabase", "Compute", "Network"]      # Define use of the Correspoding Services 
    # print(f"AWS Services list: {aws_services}")
   


    # for myservice in aws_services:                                    # How to use FOR Loop for print aws_service in Sequence
    #   print(f"AWS Service is: {myservice}")


    # index = len(aws_services) -1                                      # How to use WHILE loop for printing list suing condition, let say' reverse the List
    # while index >= 0 :
    #   print(aws_services[index])
    #   index -= 1


 
   
    for index, service in enumerate(aws_services):                     # How to use enumerate for performint advance options , its used for print the list with index
        feature_index = aws_services.index(service)
        print(f"Use of {service}: {aws_feature[feature_index]}")



 


if __name__ == "__main__":
    main()