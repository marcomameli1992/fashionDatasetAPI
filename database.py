from pymongo import MongoClient
from pathlib import Path

client = MongoClient(port=27017)
db = client.dati_da_analizzare
collection = db.files



def carica_file(a):
    data_folder = Path("D:\Instagram-20210504T103737Z-001\Instagram\BAULETTO")
    a = a+'.txt'
    file_to_open = data_folder / a
    f = open(file_to_open)
    text = f.read()
    text_file = {"nome_file": a, "contenuto": text}
    collection.insert(text_file)


carica_file("2020-11-14_14-37-01_UTC.xml")
carica_file("2020-11-14_16-46-36_UTC.xml")
carica_file("2020-11-14_16-47-10_UTC.xml")
carica_file()
