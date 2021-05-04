from pymongo import MongoClient
from pathlib import Path
import glob

client = MongoClient(port=27017)
db = client.dati_da_analizzare
collection = db.files
tutti_i_file = glob.glob("D:\dati_progetto_moda\*.txt")


def carica_file(a):
    f = open(a)
    text = f.read()
    text_file = {"nome_file": a, "contenuto": text}
    collection.insert(text_file)

for element in tutti_i_file:
    carica_file(element)


