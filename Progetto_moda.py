import flask
from flask import request, jsonify
from database import collection
from sklearn.cluster import KMeans
import cv2

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# API n.1: conteggio di numero di immagini per classe
@app.route('/imm_per_classe', methods=['GET'])
def im_per_classe():
    appoggio = list()
    for classe in range(8):
        classe = str(classe)
        immagini_per_classe = collection.find({"contenuto.classe_oggetto": classe}).count()
        text_valore = {f'Le foto con oggetti della classe {classe} sono': immagini_per_classe}
        appoggio.append(text_valore)
    return jsonify(appoggio)


# API n.2: conteggio di immagini con più di un oggetto dentro
@app.route('/molti_oggetti/all', methods=['GET'])
def piu_di_uno():
    piuoggettipresenti = collection.find({'numero_oggetti': {"$gt": 1}}).count()
    text_valore = {"Le foto con piu' oggetti presenti sono:": piuoggettipresenti}
    return text_valore


# API n.2-1: conteggio di immagini con più di un oggetto della stessa classe dentro
@app.route('/molti_oggetti', methods=['GET'])
def piu_stessa_classe():
    if 'classe' in request.args:
        classe = str(request.args['classe'])
        st_classe = collection.find(
            {"$and": [{"contenuto.classe_oggetto": classe}, {'numero_oggetti': {"$gt": 1}}]}).count()
        text_valore = {f'Le foto con piu\' di un oggetto della classe {classe} sono': st_classe}
        return text_valore
    else:
        return "Errore: Non hai specificato la classe. Riprova specificando la classe."


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

    return "Le foto con piu\' di un oggetto di classi diverse sono " + str(contatore)


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
        return "I colori dominanti per l'immagine " + jpg + " sono " + str(esadecimali)
    else:
        return "Errore: Non hai specificato l'immagine. Riprova specificando l'immagine'."


app.run()
