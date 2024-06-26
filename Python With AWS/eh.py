

def main():
  service = 'EKS'
  service_status = get_service_status(service)


  print(f"\n {service} Service Status: '{service_status}'" )


  if service_status == "Operational":
    print(f"Performing operation on '{service}'")
  else:
    print(f"{service} is NOT operational.")

def get_service_status(service_name):
  aws_services_statuses = {
    'EC2': 'Maintenance',
    'S3': 'Operational', 
    'Lambda': 'Issue Detected', 
    'DunamoDB': 'Operational',
    'RDS': 'Operational'
  }
#   return aws_services_statuses[service_name]

  try:
   return aws_services_statuses[service_name]  
  except KeyError as ke:
    print(f"\n Error: {ke}. Staus for AWS service {service_name} is not available in our Recoed")
    return None  





if __name__ == '__main__':
  main()
  