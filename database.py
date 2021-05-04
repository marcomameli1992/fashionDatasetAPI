from pymongo import MongoClient
client = MongoClient(port=27017)
db=client.dati_da_analizzare

foto={
    'modello':'',
    'valori':[]
}
db.dati_da_analizzare.insert_one(foto)