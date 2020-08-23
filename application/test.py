
# import re

# regex = r"[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?"

# test_str = "       1452 1520  53.2   1521    1636"

# matches = re.finditer(regex, test_str)

# for matchNum, match in enumerate(matches, start=1):
    

    
#     print(match.group())



import json 
  
  
# function to add to JSON 
def write_json(data, filename='boOom.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 
      
      
with open('boOom.json') as json_file: 
    data = json.load(json_file) 
      
    temp = data['emp_details'] 
  
    # python object to be appended 
    y = {"emp_name":'Nikhil', 
         "email": "nikhil@geeksforgeeks.org", 
         "job_profile": "Full Time"
        } 
  
  
    # appending data to emp_details  
    temp.append(y) 
      
write_json(data) 