import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydb"]
mycol = mydb["camdetails"]
print("please enter details to be stored into database")
while True:
    print("Enter Camera number")
    number=input()
    print("Enter location of {} ".format(number))
    name=input()
    details={"camerano":number,"location":name}
    mycol.insert_one(details)
    a=input("Press Enter to continue adding \n Press ctrl+z to exit")