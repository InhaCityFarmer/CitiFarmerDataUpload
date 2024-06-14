import pymongo
from datetime import datetime
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import ConnectionFailure

def inputData():
    mongo_database = "mongoTestDB"
    mongo_user = "3079601d-1300-42aa-89bd-bb9aa121ffec"
    mongo_password = "SmNfWM51tznfjfXc0b7ihU40"
    mongo_host = "apps-mongodb-single-b45997e1-1ef6-44f9-bd45-ff5c8218ccf7-pub.education.wise-paas.com"
    mongo_port = 27017
    mongo_uri = f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/{mongo_database}"
    now = datetime.now()
    formate_now = now.strftime("%Y-%m-%d-%H-%M-%S")
    with open('input.txt','r') as file:
    	line =  file.readline()
    	words = line.split()
    	M = words[1]
    	D = words[3]
    	T = words[5]
    	H = words[7]   
    try:
        client = MongoClient(mongo_uri)
        db = client.get_database(mongo_database)
        crop_coll = db["crop"]
        Date = formate_now

       
         # 데이터 정의
        data = {
            "name": "tomato",
            "d": D,
            "t": T,
            "h" : H,
            "m": M,
            "date": Date        }

        # 각 날짜별로 개별 문서 생성 및 삽입

       
        crop_coll.insert_one(data)
       
        client.close()
       
        return data
   
    except ConnectionFailure as e:
        print(f"Unable to connect to MongoDB instance: {str(e)}")
        return {"error": f"Unable to connect to MongoDB instance: {str(e)}"}
    except Exception as e:
        print(f"An error occurred while connecting to MongoDB: {str(e)}")
        return {"error": f"An error occurred while connecting to MongoDB: {str(e)}"}

# Send a ping to confirm a successful connection

inputData()

