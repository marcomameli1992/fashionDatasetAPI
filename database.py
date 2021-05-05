from pymongo import MongoClient
import glob

client = MongoClient(port=27017)
db = client.dati_da_analizzare
collection = db.files

tutti_i_file0 = glob.glob("Image/BAULETTO/*.txt")
tutti_i_file1 = glob.glob("Image\BRAND\FAY\*.txt")
tutti_i_file2 = glob.glob("Image\BRAND\HOGAN\BAULETTO\*.txt")
tutti_i_file3 = glob.glob("Image\BRAND\HOGAN\CLUTCH\*.txt")
tutti_i_file4 = glob.glob("Image\BRAND\HOGAN\HOBO\*.txt")
tutti_i_file5 = glob.glob("Image\BRAND\HOGAN\SECCHIELLO\*.txt")
tutti_i_file6 = glob.glob("Image\BRAND\ROGERVIVIER\BAULETTO\*.txt")
tutti_i_file7 = glob.glob("Image\BRAND\ROGERVIVIER\CLUTCH\*.txt")
tutti_i_file8 = glob.glob("Image\BRAND\ROGERVIVIER\HOBO\*.txt")
tutti_i_file9 = glob.glob("Image\BRAND\ROGERVIVIER\MARSUPIO\*.txt")
tutti_i_file10 = glob.glob("Image\BRAND\ROGERVIVIER\SACCA\*.txt")
tutti_i_file11 = glob.glob("Image\BRAND\ROGERVIVIER\SECCHIELLO\*.txt")
tutti_i_file12 = glob.glob("Image\BRAND\ROGERVIVIER\SHOPPING\*.txt")
tutti_i_file13 = glob.glob("Image\BRAND\TODS\BAULETTO\*.txt")
tutti_i_file14 = glob.glob("Image\BRAND\TODS\CLUTCH\*.txt")
tutti_i_file15 = glob.glob("Image\BRAND\TODS\HOBO\*.txt")
tutti_i_file16 = glob.glob("Image\BRAND\TODS\MARSUPIO\*.txt")
tutti_i_file17 = glob.glob("Image\BRAND\TODS\SACCA\*.txt")
tutti_i_file18 = glob.glob("Image\BRAND\TODS\SECCHIELLO\*.txt")
tutti_i_file19 = glob.glob("Image\BRAND\TODS\SHOPPING\*.txt")
tutti_i_file20 = glob.glob("Image\BRAND\TODS\TRACOLLA\*.txt")
tutti_i_file21 = glob.glob("Image\CLUTCH\*.txt")
tutti_i_file22 = glob.glob("Image\HOBO\*.txt")
tutti_i_file23 = glob.glob("Image\Hogan\*.txt")
tutti_i_file24 = glob.glob("Image\hoganbag\*.txt")
tutti_i_file25 = glob.glob("Image\MARSUPIO\*.txt")
tutti_i_file26 = glob.glob("Image\SECCHIELLO\*.txt")
tutti_i_file27 = glob.glob("Image\CLUTCH\\rogervivierbags\*.txt")
tutti_i_file28 = glob.glob("Image\hoganbag\\rogervivierbag\*.txt")
tutti_i_file29 = glob.glob("Image\\rogervivier\*.txt")
tutti_i_file30 = glob.glob("Image\\rogervivierbag\*.txt")
tutti_i_file31 = glob.glob("Image\\rogervivierbags\*.txt")
#tutti i file delle cartelle TOD_s
tutti_i_file32 = glob.glob("Image\\tods\ADVERTISING\ADV_ISTITUZIONALE\FW19-20\Adv_worldwide\Foto_Social\*.txt")
tutti_i_file33 = glob.glob("Image\\tods\ADVERTISING\ADV_ISTITUZIONALE\FW19-20\Adv_worldwide\Immagini_adv\*.txt")
tutti_i_file34 = glob.glob("Image\\tods\ADVERTISING\ADV_ISTITUZIONALE\FW19-20\Adv-Japan-Maggie_Jiang\Immagini\*.txt")
tutti_i_file35 = glob.glob("Image\\tods\ADVERTISING\ADV_ISTITUZIONALE\FW19-20\Box_NYT_2x7\*.txt")
tutti_i_file36 = glob.glob("Image\\tods\ADVERTISING\ADV_ISTITUZIONALE\FW20-21\Adv_Cina\Foto_Social\*.txt")
tutti_i_file37 = glob.glob("Image\\tods\ADVERTISING\ADV_ISTITUZIONALE\FW20-21\Adv_Cina\Immagini_adv\*.txt")
tutti_i_file38 = glob.glob("Image\\tods\ADVERTISING\ADV_ISTITUZIONALE\FW20-21\Adv_Worldwide\Foto_Social\*.txt")
tutti_i_file39 = glob.glob("Image\\tods\ADVERTISING\ADV_ISTITUZIONALE\FW20-21\Adv_Worldwide\Immagini_adv\*.txt")
tutti_i_file40 = glob.glob("Image\\tods\ADVERTISING\ADV_ISTITUZIONALE\Pre_FW20-21\Immagini_adv\*.txt")
tutti_i_file41 = glob.glob("Image\\tods\ADVERTISING\ADV_ISTITUZIONALE\Pre_SS21\Foto_Social\*.txt")
tutti_i_file42 = glob.glob("Image\\tods\ADVERTISING\ADV_ISTITUZIONALE\Pre_SS21\Immagini_adv\*.txt")
tutti_i_file43 = glob.glob("Image\\tods\ADVERTISING\ADV_ISTITUZIONALE\SS20\Foto_Social\*.txt")
tutti_i_file44 = glob.glob("Image\\tods\ADVERTISING\ADV_ISTITUZIONALE\SS20\Immagini_adv\*.txt")
tutti_i_file45 = glob.glob("Image\\tods\ADVERTISING\ADV_ISTITUZIONALE\SS20_RESORT\Foto_Social\*.txt")
tutti_i_file46 = glob.glob("Image\\tods\ADVERTISING\ADV_ISTITUZIONALE\SS20_RESORT\Immagini_adv\*.txt")
tutti_i_file47 = glob.glob("Image\\tods\ADVERTISING\ADV_ISTITUZIONALE\SS21\Foto_Social\*.txt")
tutti_i_file48 = glob.glob("Image\\tods\ADVERTISING\ADV_ISTITUZIONALE\SS21\Immagini_adv\*.txt")
tutti_i_file49 = glob.glob("Image\\tods\CATALOGHI\\1_AI_19_20\*.txt")
tutti_i_file50 = glob.glob("Image\\tods\CATALOGHI\\2_SS_20\*.txt")
tutti_i_file51 = glob.glob("Image\\tods\CATALOGHI\\3_AI_20_21\*.txt")
tutti_i_file52 = glob.glob("Image\\tods\CATALOGHI\\4_SS_21\*.txt")
tutti_i_file53 = glob.glob("Image\\tods\DIGITAL_PROJECTS\FW19-20\ALBER_ELBAZ_HAPPY_MOMENTS\*.txt")
tutti_i_file54 = glob.glob("Image\\tods\DIGITAL_PROJECTS\FW20-21\A_PAWFECT_HOLIDAY_DogsProject\*.txt")
tutti_i_file55 = glob.glob("Image\\tods\DIGITAL_PROJECTS\FW20-21\HOLLY_BAG\BTS_Images\*.txt")
tutti_i_file56 = glob.glob("Image\\tods\DIGITAL_PROJECTS\FW20-21\HOLLY_BAG\STILLS_FROM_VIDEO\*.txt")
tutti_i_file57 = glob.glob("Image\\tods\DIGITAL_PROJECTS\PE20\FULL_SUMMER_DREAM\*.txt")
tutti_i_file58 = glob.glob("Image\\tods\DIGITAL_PROJECTS\PE20\MAME\*.txt")
tutti_i_file59 = glob.glob("Image\\tods\DIGITAL_PROJECTS\PE20\MY_TODS_CLOSET\*.txt")
tutti_i_file60 = glob.glob("Image\\tods\DIGITAL_PROJECTS\PE20\TIMELESS\*.txt")
tutti_i_file61 = glob.glob("Image\\tods\DIGITAL_PROJECTS\PE21\SHIRT_BAG\*.txt")


class Valore:
    def __init__(self, tipo, val1, val2, val3, val4):
        self.tipo=tipo,
        self.val1=val1,
        self.val2=val2,
        self.val3=val3,
        self.val4=val4


def carica_file(file_to_open):
    f = open(file_to_open)
    text = f.read()
    content=list()
    appoggio=list()
    n_righe=text.count('\n')
    riga=text.split('\n')

    for n in range(n_righe):
        dato=riga[n].split(" ")
        appoggio.append(dato)

    for k in range(n_righe):
        text_valore = {"classe_oggetto":appoggio[k][0], "val_1":appoggio[k][1], "val_2":appoggio[k][2], "val_3":appoggio[k][3], "val_4":appoggio[k][4]}
        content.append(text_valore)

    text_file = {"nome_file": file_to_open, "numero_oggetti":n_righe, "contenuto": content}
    collection.insert(text_file)


for element in tutti_i_file0:
    if not(element.__contains__("classes")):
        carica_file(element)


for element in tutti_i_file1:
    if not(element.__contains__("classes")):
        carica_file(element)


for element in tutti_i_file2:
    if not(element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file3:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file4:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file5:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file6:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file7:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file8:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file9:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file10:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file11:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file12:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file13:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file14:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file15:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file16:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file17:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file18:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file19:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file20:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file21:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file22:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file23:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file24:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file25:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file26:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file27:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file28:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file29:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file30:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file31:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file32:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file33:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file34:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file35:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file36:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file37:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file38:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file39:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file40:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file41:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file42:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file43:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file44:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file45:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file46:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file47:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file48:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file49:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file50:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file51:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file52:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file53:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file54:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file55:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file56:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file57:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file58:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file59:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file60:
    if not (element.__contains__("classes")):
        carica_file(element)

for element in tutti_i_file61:
    if not (element.__contains__("classes")):
        carica_file(element)


cursor = collection.find({})
for document in cursor:
    print(document)

print("--------------------------------------")
print("Il database contiene: " + str(db.files.count()) + " elementi.")
print(db.files.count())
