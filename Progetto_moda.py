import json
import string

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
"""# Fashion Dataset API

Creazione di API per analizzare un Fashion dataset e provare a predire i futuri trend nel campo della moda. Queste API lavorano con file di testo in formato .txt o con immagini.E restituiscono i risultati in formato JSON.

----
----
#### **API N°1:** CONTEGGIO DI NUMERO DI IMMAGINI PER CLASSE

###### /img_per_classe

Questa API restituisce un JSON contenente il numero di immagini per ogni classe. Il risultato è il seguente:

```
[
  {
    "Le_foto_con_oggetti_della_classe_0_sono'": 0,
    "Le_foto_con_oggetti_della_classe_1_sono'": 0,
    "Le_foto_con_oggetti_della_classe_2_sono'": 0,
    "Le_foto_con_oggetti_della_classe_3_sono'": 0,
    "Le_foto_con_oggetti_della_classe_4_sono'": 0,
    "Le_foto_con_oggetti_della_classe_5_sono'": 0,
    "Le_foto_con_oggetti_della_classe_6_sono'": 0,
    "Le_foto_con_oggetti_della_classe_7_sono'": 0,
	"Le_foto_con_oggetti_della_classe_8_sono'": 0
  }
]
```
----
* **Parametri:** _nomi_ -> non va valorizzato _**FACOLTATIVO**_

Se specificato questo parametro il numero delle classi viene convertito nel nome della classe che rappresenta in questo modo l'API restituisce un JSON, più leggibile contenente il numero di immagini che hanno più di un oggetto della stessa classe al loro interno. Il risultato è il seguente:

```
[
  {
    "Le_foto_con_oggetti_della_classe_BAULETTO_sono'": 0,
    "Le_foto_con_oggetti_della_classe_CLUTCH_sono'": 0,
    "Le_foto_con_oggetti_della_classe_HOBO_sono'": 0,
    "Le_foto_con_oggetti_della_classe_MARSUPIO_sono'": 0,
    "Le_foto_con_oggetti_della_classe_SACCA_sono'": 0,
    "Le_foto_con_oggetti_della_classe_SECCHIELLO_sono'": 0,
    "Le_foto_con_oggetti_della_classe_SHOPPING_sono'": 0,
    "Le_foto_con_oggetti_della_classe_TRACOLLA_sono'": 0,
	"Le_foto_con_oggetti_della_classe_ZAINO_sono'": 0
  }
]
```
----
----
"""
classi_ammesse=['bauletto','clutch', 'hobo', 'marsupio', 'sacca', 'secchiello','shopping','tracolla','zaino']

# API n.1: conteggio di numero di immagini per classe
@app.route('/img_per_classe', methods=['GET'])
def im_per_classe():
    appoggio = list()
    for classe in range(9):
        classe = str(classe)
        immagini_per_classe = collection.find({"contenuto.classe_oggetto": classe}).count()
        text_valore = {f'Le_foto_con_oggetti_della_classe_{classe}_sono': immagini_per_classe}
        if 'nomi' in request.args:
            text_valore = {f'Le_foto_con_oggetti_della_classe_{nomeClasse(classe)}_sono': immagini_per_classe}
        appoggio.append(text_valore)
    return jsonify(appoggio), 200


"""#### **API N°2:** CONTEGGIO DI IMMAGINI CON PIU' DI UN OGGETTO DENTRO

###### /molti_oggetti/all

Questa API restituisce un JSON contenente il numero di immagini che hanno più di un oggetto al loro interno. Il risultato è il seguente:

```
{
  "Le_foto_con_piu_oggetti_presenti_sono": 0
}
```
----
----
"""


# API n.2: conteggio di immagini con più di un oggetto dentro
@app.route('/molti_oggetti/all', methods=['GET'])
def piu_di_uno():
    piuoggettipresenti = collection.find({'numero_oggetti': {"$gt": 1}}).count()
    text_valore = {"Le_foto_con_piu_oggetti_presenti_sono:": piuoggettipresenti}
    return text_valore, 200


"""#### **API N°2.1:** CONTEGGIO DI IMMAGINI CON PIU' DI UN OGGETTO DELLA STESSA CLASSE DENTRO

###### /molti_oggetti

* **Parametri:** 
* * _classe_ -> una **stringa** che corrisponde al numero della classe, o al suo nome(case insensitive), di cui si vuole eseguire il conteggio
* *  _nomi_ -> non va valorizzato _**FACOLTATIVO**_

Questa API restituisce un JSON contenente il numero di immagini che hanno più di un oggetto della stessa classe al loro interno. Il risultato è il seguente:

```
{
  "Le_foto_con_piu_di_un_oggetto_della_classe_{classe}_sono": 0
}
```
----
Se viene specificato il parametro **_nomi_** il numero delle classi viene convertito nel nome della classe che rappresenta in questo modo l'API restituisce un JSON, più leggibile contenente il numero di immagini che hanno più di un oggetto della stessa classe al loro interno.
Se non viene passato il parametro _classe_ il risultato è il seguente:
```
{
  "Errore": Non hai specificato la classe. Riprova specificando la classe."
}
```
Se viene passata al parametro _classe_ una classe che non esiste il risultato è il seguente:
```
{
  "Errore": "la classe non esiste"
}
```

----
----
"""


# API n.2-1: conteggio di immagini con più di un oggetto della stessa classe dentro
@app.route('/molti_oggetti', methods=['GET'])
def piu_stessa_classe():
    if 'classe' in request.args:
        classe = request.args['classe']
        if (classe.isnumeric()):
            nome=nomeClasse(int(classe))
            classe=classe
            if (int(classe) > 8):
                text_error = {"Errore": "la classe non esiste"}
                return text_error, 404
        elif isinstance(classe,str):
            nome=classe.lower()
            if not(nome in classi_ammesse):
                text_error = {"Errore": "la classe non esiste"}
                return text_error, 404
            else: classe=classeNome(nome)
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
        if 'nomi' in request.args:
            text_valore={f'Le_foto_con_piu_di_un_oggetto_della_classe_{nome.upper()}_sono': result}
        return text_valore, 200
    else:
        text_error = {'Errore': 'Non hai specificato la classe. Riprova specificando la classe.'}
        return text_error, 400




"""#### **API N°2.2:** CONTEGGIO DI IMMAGINI CON PIU' DI UN OGGETTO DI CLASSI DIVERSE DENTRO

###### /molti_oggetti/molte_classi

Questa API restituisce un JSON contenente il numero di immagini che hanno più di un oggetto di classi diverse al loro interno. Il risultato è il seguente:

```
{
  "Le_foto_con piu_di_un_oggetto_di_classi_diverse_sono": 0
}
```
----
----
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


"""#### **API N°3:** VALUTAZIONE DEL COLORE DOMINANTE DI UNA DETERMINATA IMMAGINE

###### /dominante

* **Parametri:** _img_ -> una **stringa** che contiene il Path dell'immagine della quale si vuole estrarre il colore dominante

Questa API restituisce un JSON contenente i colori dominanti di ciascun'immagine, in formato esadecimale. Il risultato è il seguente:

```
{
  "I_colori_dominanti_per_l_immagine_{img}_sono": [
    "string"
  ]
}
```
Se non viene passato il parametro _img_ il risultato è il seguente:
```
{
  "Errore": Non hai specificato l'immagine. Riprova specificando l'immagine"
}
```

----
----
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


"""#### **API N°4:** RICONOSCIMENTO OGGETTI PERSENTI IN UN'IMMAGINE CON MODELLO YOLOv5

###### /YOLOv5

* **Parametri:** _img_ -> una **stringa** che contiene il Path dell'immagine della quale si vuole, mediante il modello YOLOv5, vedere quali oggetti vi siano presenti

Questa API restituisce un JSON. Il risultato è il seguente:

```
"string"
```
Se non viene passato il parametro _img_ il risultato è il seguente:
```
{
  "Errore": Non hai specificato un immagine. Riprova specificando un'immagine corretta."
}
```

----
----
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


"""#### **API N°5:** RICONOSCIMENTO OGGETTI PERSENTI IN UN'IMMAGINE CON MODELLO VGG

###### /predvgg

* **Parametri:** _img_ -> una **stringa** che contiene il Path dell'immagine della quale si vuole, mediante il modello vgg, vedere quali oggetti vi siano presenti

Questa API restituisce un JSON. Il risultato è il seguente:

```
{
  "Le_predizioni_per_l_immagine_{img}_sono": [array],
  "classe_id": "string",
  "nome_classe": "string"
}
```
Se non viene passato il parametro _img_ il risultato è il seguente:
```
{
  "Errore": Non hai specificato un immagine. Riprova specificando un'immagine corretta."
}
```

----
----
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
        _, y_hat = predictions.max(1)
        predicted_idx = str(y_hat.item())
        imagenet_class_index = json.load(open('Image/imagenet_class_index.json'))
        class_id, class_name=imagenet_class_index[predicted_idx]
        list = predictions.tolist()

        return {f'Le_predizioni_per_l_immagine_{jpg}_sono': list, 'classe_id':class_id,'nome_classe':class_name}, 200
    else:
        text_error = {"Errore": "Non hai specificato un immagine. Riprova specificando un'immagine corretta."}
        return text_error, 400

def nomeClasse(classes):
    classe=int(classes)
    if classe == 0:
        nome = "BAULETTO"
    elif classe == 1:
        nome = "CLUTCH"
    elif classe == 2:
        nome = "HOBO"
    elif classe == 3:
        nome = "MARSUPIO"
    elif classe == 4:
        nome = "SACCA"
    elif classe == 5:
        nome = "SECCHIELLO"
    elif classe == 6:
        nome = "SHOPPING"
    elif classe == 7:
        nome = "TRACOLLA"
    elif classe == 8:
        nome = "ZAINO"
    else: nome = "CLASSE_INESISTENTE"
    return nome

def classeNome(nomes):
    nome=str(nomes).lower()
    if nome=="bauletto":
        classe='0'
    elif nome == "clutch":
        classe = '1'
    elif nome == "hobo":
        classe = '2'
    elif nome == "marsupio":
        classe = '3'
    elif nome == "sacca":
        classe = '4'
    elif nome == "secchiello":
        classe = '5'
    elif nome == "shopping":
        classe = '6'
    elif nome == "tracolla":
        classe = '7'
    elif nome == "zaino":
        classe = '8'
    else: classe = 'Inesistente'
    return classe
app.run()
