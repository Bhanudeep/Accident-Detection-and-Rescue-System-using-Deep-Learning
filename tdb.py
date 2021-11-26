import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydb"]
mycol = mydb["details"]
print("please enter details to be stored into database")
while True:
    print("Enter Vehicle Number(registration number)")
    number=input()
    print("Enter name of {} vehicle's Owner ".format(number))
    name=input()
    print("Provide email id of {}'s Trustee ".format(name))
    email=input()
    details={"regno":number,"name":name,"email":email}
    mycol.insert_one(details)
    a=input("Press Enter to continue adding \n Press ctrl+z to exit")