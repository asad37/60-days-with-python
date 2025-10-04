# #this section include the file handling in which txt csv and json file 
# f=open("asad.txt","w")
# f.write("My name is Asad waqas and i am mobile application developer")
# print("file written successfully")
# f.close()
# f=open("asad.txt","r")
# for line in f:
#     print(line.strip())
# f.close()

# f=open("asad.txt","a")
# f.write("\n i am also worpress developer")
# f=open("asad.txt","r")
# for line in f:
#     print(line.strip())
# f.close()


##############################
# with open("practice.txt","w")as f:
#     data=f.write("Asad is a good boy")
# with open("practice.txt","r") as f:
#     data=f.read()
#     print(data)
    
# with open ("practice.txt","a")as f:
#     f.write("Aasncbduybb c j   erwchj h rh v 4")
# with open("practice.txt","r") as f:
#     data=f.read()
#     print(data)
    
##################################################

import csv
with open("students.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["Name","Age","Marks"])
    writer.writerow(["Asad Waqas",23,453])
    
with open ("students.csv","r") as f:
    reader=csv.reader(f)
    for i in reader:
        print(i)
############################################
import json 
student={
    "name":"Asad Waqas",
    "age":23,
    "marks":93
}

with open("student.json","w")as file:
    json.dump(student,file)
with open("student.json","r")as file:
    data=json.load(file)
    print(data["age"])