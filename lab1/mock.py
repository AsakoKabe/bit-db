import random

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["customers"]
collection = db["collection"]

num_records_to_insert = 1000000
data = []
for i in range(num_records_to_insert):
    data.append({
      "_id": i + 300,
      "genre": "Male",
      "age": random.randint(10, 60),
      "annual_income": random.randint(10, 600),
      "spending_score": random.randint(10, 600),
  })

collection.insert_many(data)

client.close()
