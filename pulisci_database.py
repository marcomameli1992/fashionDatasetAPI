from pymongo import MongoClient
import glob

client = MongoClient(port=27017)
db = client.dati_da_analizzare
collection = db.files
tutti_i_file = glob.glob("D:\dati_progetto_moda\Instagram\BAULETTO\*.txt")


db.files.remove()


cursor = collection.find({})
for document in cursor:
    print(document)

print("--------------------------------------")
print("Il database contiene: "+str(db.files.count())+" elementi.")
print(db.files.count())

