import flask
import torch
from flask import request, jsonify
from matplotlib import pyplot as plt, patches

import cv2
import torch
from PIL import Image

from database import collection
from sklearn.cluster import KMeans
import cv2
import torchvision.models as models
from PIL import Image

app = flask.Flask(__name__)
app.config["DEBUG"] = True
""" # Fashion Dataset API"""
""" Creazione di API per analizzare un Fashion dataset e provare a predire i futuri trend nel campo della moda. Queste API lavorano con file di testo in formato .txt o con immagini.
E restituiscono i risultati in formato JSON"""
"""#### **API N°1:** CONTEGGIO DI NUMERO DI IMMAGINI PER CLASSE"""
"""###### /img_per_classe"""
"""Questa API restituisce un JSON contenente il numero di immagini per ogni classe. Il risultato è il seguente:
'''
[
  {
    "Le_foto_con_oggetti_della_classe_0_sono'": 0,
    "Le_foto_con_oggetti_della_classe_1_sono'": 0,
    "Le_foto_con_oggetti_della_classe_2_sono'": 0,
    "Le_foto_con_oggetti_della_classe_3_sono'": 0,
    "Le_foto_con_oggetti_della_classe_4_sono'": 0,
    "Le_foto_con_oggetti_della_classe_5_sono'": 0,
    "Le_foto_con_oggetti_della_classe_6_sono'": 0,
    "Le_foto_con_oggetti_della_classe_7_sono'": 0
  }
]
'''
"""


# API n.1: conteggio di numero di immagini per classe
@app.route('/img_per_classe', methods=['GET'])
def im_per_classe():
    appoggio = list()
    for classe in range(8):
        classe = str(classe)
        immagini_per_classe = collection.find({"contenuto.classe_oggetto": classe}).count()
        text_valore = {f'Le_foto_con_oggetti_della_classe_{classe}_sono': immagini_per_classe}
        appoggio.append(text_valore)
    return jsonify(appoggio), 200


"""####**API N°2:** CONTEGGIO DI IMMAGINI CON PIU' DI UN OGGETTO DENTRO"""
"""######/molti_oggetti/all"""
"""Questa API restituisce un JSON contenente il numero di immagini che hanno più di un oggetto al loro interno. Il risultato è il seguente:
'''
{
  "Le_foto_con_piu_oggetti_presenti_sono": 0
}
'''
"""


# API n.2: conteggio di immagini con più di un oggetto dentro
@app.route('/molti_oggetti/all', methods=['GET'])
def piu_di_uno():
    piuoggettipresenti = collection.find({'numero_oggetti': {"$gt": 1}}).count()
    text_valore = {"Le_foto_con_piu_oggetti_presenti_sono:": piuoggettipresenti}
    return text_valore, 200


"""####**API N°2.1:** CONTEGGIO DI IMMAGINI CON PIU' DI UN OGGETTO DELLA STESSA CLASSE DENTRO"""
"""######/molti_oggetti"""
""" 
- **Parametri:** *classe* -> una **stringa** che corrisponde al numero della classe di cui si vuole eseguire il conteggio
"""
"""Questa API restituisce un JSON contenente il numero di immagini che hanno più di un oggetto della stessa classe al loro interno. Il risultato è il seguente:
'''
{
  "Le_foto_con_piu_di_un_oggetto_della_classe_{classe}_sono": 0
}
'''
"""


# API n.2-1: conteggio di immagini con più di un oggetto della stessa classe dentro
@app.route('/molti_oggetti', methods=['GET'])
def piu_stessa_classe():
    if 'classe' in request.args:
        classe = str(request.args['classe'])
        if (int(classe) > 8):
            text_error = {"Errore": "la classe non esiste"}
            return text_error, 404
        result=0
        st_classe = collection.find(
            {"$and": [{"contenuto.classe_oggetto": classe}, {'numero_oggetti': {"$gt": 1}}]})
        for doc in st_classe:
            array = doc['contenuto']
            valut=0
            for j in array:
                val = j['classe_oggetto']
                if val == classe:
                    valut +=1
                    if valut>1:
                        result += 1
                        break
        text_valore = {f'Le_foto_con_piu_di_un_oggetto_della_classe_{classe}_sono': result}
        print(st_classe.count())
        return text_valore, 200
    else:
        text_error = {'Errore': 'Non hai specificato la classe. Riprova specificando la classe.'}
        return text_error, 400




"""####**API N°2.2:** CONTEGGIO DI IMMAGINI CON PIU' DI UN OGGETTO DI CLASSI DIVERSE DENTRO"""
"""######/molti_oggetti/molte_classi"""
"""Questa API restituisce un JSON contenente il numero di immagini che hanno più di un oggetto di classi diverse al loro interno. Il risultato è il seguente:
'''
{
  "Le_foto_con piu_di_un_oggetto_di_classi_diverse_sono": 0
}
'''
"""


# API n.2-2: conteggio di immagini con più di un oggetto di classi dentro
@app.route('/molti_oggetti/molte_classi', methods=['GET'])
def piu_uno_piu_classi():
    piu_classi = collection.find({'numero_oggetti': {"$gt": 1}})
    contatore = 0
    for i in piu_classi:
        array = i['contenuto']
        confronto = array[0]['classe_oggetto']
        for j in array:
            classe = j['classe_oggetto']
            if classe != confronto:
                contatore += 1
                break
    text_valore = {f'Le_foto_con_piu_di_un_oggetto_di_classi_diverse_sono': str(contatore)}
    return text_valore, 200


"""####**API N°3:** VALUTAZIONE DEL COLORE DOMINANTE DI UNA DETERMINATA IMMAGINE"""
"""######/dominante"""
""" 
- **Parametri:** *img* -> una **stringa** che contiene il Path dell'immagine della quale si vuole estrarre il colore dominante
"""
"""Questa API restituisce un JSON contenente i colori dominanti di ciascun'immagine, in formato esadecimale. Il risultato è il seguente:
'''
{
  "I_colori_dominanti_per_l_immagine_{img}_sono": [
    "string"
  ]
}
'''
"""


# API n.3: per una determinata classe quale è il colore predominante
@app.route('/dominante')
def colore_dominante():
    if 'img' in request.args:
        jpg = str(request.args['img'])
        img = cv2.imread(jpg)
        immagine = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        immagine = immagine.reshape((immagine.shape[0] * immagine.shape[1], 3))
        kmeans = KMeans(2)
        kmeans.fit(immagine)
        colori_dominanti = kmeans.cluster_centers_
        colori_dominanti.astype(int)

        esadecimali = []
        for i in colori_dominanti:
            j = str(i).strip("][")
            splittato = j.split()
            colori = '%02x%02x%02x' % (int(float(splittato[0])), int(float(splittato[1])), int(float(splittato[2])))
            esadecimali.append(colori)
        text_valore = {f'I_colori_dominanti_per_l_immagine_{jpg}_sono': str(esadecimali)}
        return text_valore, 200

        # return "I colori dominanti per l'immagine " + jpg + " sono " + str(esadecimali)
    else:
        text_error = {"Errore": "Non hai specificato l'immagine. Riprova specificando l'immagine"}
        return text_error, 400


"""####**API N°4:** RICONOSCIMENTO OGGETTI PERSENTI IN UN'IMMAGINE CON MODELLO YOLOv5 """
"""######/YOLOv5"""
""" 
- **Parametri:** *img* -> una **stringa** che contiene il Path dell'immagine della quale si vuole estrarre il colore dominante
"""
"""Questa API restituisce un JSON. Il risultato è il seguente:
'''
"string"
'''
"""


@app.route('/YOLOv5')
def pred_yolo():
    if 'img' in request.args:
        jpg = str(request.args['img'])


        model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

        #img1 = Image.open(jpg) metodo alternativo per aprire l'immagine, non serve
        img2 = cv2.imread(jpg)[:, :, ::-1]
        #imgs = [img1, img2]

        #risultati
        results = model(img2, size=640)

        results.print() #permette di controllare su terminale i risultati ottenuti
        results.save()  #salva l'immagine con gli oggetti evidenziati

        predictions2 = results.pandas().xyxy[0].to_json(orient="records")

        return predictions2
    else:
        text_error = {"Errore": "Non hai specificato un immagine. Riprova specificando un'immagine corretta."}
        return text_error, 400


"""####**API N°5:** RICONOSCIMENTO OGGETTI PERSENTI IN UN'IMMAGINE CON MODELLO VGG"""
"""######/predvgg"""
""" 
- **Parametri:** *img* -> una **stringa** che contiene il Path dell'immagine della quale si vuole estrarre il colore dominante
"""
"""Questa API restituisce un JSON. Il risultato è il seguente:
'''
{
  "Le_predizioni_per_l_immagine_{img}_sono": "string"
}
'''
"""


# API 5: Vgg16
@app.route('/predvgg', methods=['GET'])
def pred_vgg():
    if 'img' in request.args:
        jpg = str(request.args['img'])
        img = Image.open(jpg)
        from torchvision import transforms
        transform = transforms.Compose([  # [1]
            transforms.Resize(256),  # [2]
            transforms.CenterCrop(224),  # [3]
            transforms.ToTensor(),  # [4]
            transforms.Normalize(  # [5]
                mean=[0.485, 0.456, 0.406],  # [6]
                std=[0.229, 0.224, 0.225]  # [7]
            )])

        img_t = transform(img)
        batch_t = torch.unsqueeze(img_t, 0)

        model = models.vgg16(pretrained=True)

        model.eval()
        predictions = model(batch_t)

        list = predictions.tolist()

        return {f'Le_predizioni_per_l_immagine_{jpg}_sono': list}, 200
    else:
        text_error = {"Errore": "Non hai specificato un immagine. Riprova specificando un'immagine corretta."}
        return text_error, 400


app.run()
