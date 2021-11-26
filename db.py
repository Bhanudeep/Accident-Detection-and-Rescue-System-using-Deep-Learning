import pymongo
import json
camerano="camera_01"
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydb"]
mycol = mydb["camdetails"]
cam=str(camerano)
i=0
res=""
for x in mycol.find({"camerano":cam},{ "_id": 0,"camerano": 1, "location": 1 }):
    result=json.dumps(x)
    res = json.loads(result)
    print(res["location"])

#0bf3c198b91003