from pymongo import MongoClient
import glob

client = MongoClient(port=27017)
db = client.dati_da_analizzare
collection = db.files
tutti_i_file0 = glob.glob("D:\dati_progetto_moda\Instagram\BAULETTO\*.txt")
tutti_i_file1 = glob.glob("D:\dati_progetto_moda\Instagram\BRAND\FAY\*.txt")
tutti_i_file2 = glob.glob("D:\dati_progetto_moda\Instagram\BRAND\HOGAN\BAULETTO\*.txt")
tutti_i_file3 = glob.glob("D:\dati_progetto_moda\Instagram\BRAND\HOGAN\CLUTCH\*.txt")
tutti_i_file4 = glob.glob("D:\dati_progetto_moda\Instagram\BRAND\HOGAN\HOBO\*.txt")
tutti_i_file5 = glob.glob("D:\dati_progetto_moda\Instagram\BRAND\HOGAN\SECCHIELLO\*.txt")
tutti_i_file6 = glob.glob("D:\dati_progetto_moda\Instagram\BRAND\ROGERVIVIER\BAULETTO\*.txt")
tutti_i_file7 = glob.glob("D:\dati_progetto_moda\Instagram\BRAND\ROGERVIVIER\CLUTCH\*.txt")
tutti_i_file8 = glob.glob("D:\dati_progetto_moda\Instagram\BRAND\ROGERVIVIER\HOBO\*.txt")
tutti_i_file9 = glob.glob("D:\dati_progetto_moda\Instagram\BRAND\ROGERVIVIER\MARSUPIO\*.txt")
tutti_i_file10 = glob.glob("D:\dati_progetto_moda\Instagram\BRAND\ROGERVIVIER\SACCA\*.txt")
tutti_i_file11 = glob.glob("D:\dati_progetto_moda\Instagram\BRAND\ROGERVIVIER\SECCHIELLO\*.txt")
tutti_i_file12 = glob.glob("D:\dati_progetto_moda\Instagram\BRAND\ROGERVIVIER\SHOPPING\*.txt")
tutti_i_file13 = glob.glob("D:\dati_progetto_moda\Instagram\BRAND\TODS\BAULETTO\*.txt")
tutti_i_file14 = glob.glob("D:\dati_progetto_moda\Instagram\BRAND\TODS\CLUTCH\*.txt")
tutti_i_file15 = glob.glob("D:\dati_progetto_moda\Instagram\BRAND\TODS\HOBO\*.txt")
tutti_i_file16 = glob.glob("D:\dati_progetto_moda\Instagram\BRAND\TODS\MARSUPIO\*.txt")
tutti_i_file17 = glob.glob("D:\dati_progetto_moda\Instagram\BRAND\TODS\SACCA\*.txt")
tutti_i_file18 = glob.glob("D:\dati_progetto_moda\Instagram\BRAND\TODS\SECCHIELLO\*.txt")
tutti_i_file19 = glob.glob("D:\dati_progetto_moda\Instagram\BRAND\TODS\SHOPPING\*.txt")
tutti_i_file20 = glob.glob("D:\dati_progetto_moda\Instagram\BRAND\TODS\TRACOLLA\*.txt")
tutti_i_file21 = glob.glob("D:\dati_progetto_moda\Instagram\CLUTCH\*.txt")
tutti_i_file22 = glob.glob("D:\dati_progetto_moda\Instagram\HOBO\*.txt")
tutti_i_file23 = glob.glob("D:\dati_progetto_moda\Instagram\Hogan\*.txt")
tutti_i_file24 = glob.glob("D:\dati_progetto_moda\Instagram\hoganbag\*.txt")
tutti_i_file25 = glob.glob("D:\dati_progetto_moda\Instagram\MARSUPIO\*.txt")
tutti_i_file26 = glob.glob("D:\dati_progetto_moda\Instagram\SECCHIELLO\*.txt")



def carica_file(a):
    f = open(a)
    text = f.read()
    text_file = {"nome_file": a, "contenuto": text}
    collection.insert(text_file)

for number in range(27)
    appoggio="tutti_i_file"+str(number)
    for element in appoggio:
        carica_file(element)


cursor = collection.find({})
for document in cursor:
    print(document)

print("--------------------------------------")
print("Il database contiene: "+str(db.files.count())+" elementi.")
print(db.files.count())


