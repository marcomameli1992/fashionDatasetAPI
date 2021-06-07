import flask
import torch
from flask import request, jsonify
from matplotlib import pyplot as plt, patches

from database import collection
from sklearn.cluster import KMeans
import cv2
import torchvision.models as models
from PIL import Image

app = flask.Flask(__name__)
app.config["DEBUG"] = True



class FashionResponseSchema(Schema):
    message = fields.Str(default='Successo')


class FashionRequestSchema(Schema):
    api_type = fields.String(required=True, description="API tipo delle Fashion Dataset API")

class FashionAPI(MethodResource, Resource):
    @doc(description='API per il conteggio del numero di immagini per classe.', tags=['Immagini'])
    @marshal_with(FashionResponseSchema)  # marshalling
    # API n.1: conteggio di numero di immagini per classe
    @app.route('/imm_per_classe', methods=['GET'])
    def im_per_classe(self):
        appoggio = list()
        for classe in range(8):
            classe = str(classe)
            immagini_per_classe = collection.find({"contenuto.classe_oggetto": classe}).count()
            text_valore = {f'Le foto con oggetti della classe {classe} sono': immagini_per_classe}
            appoggio.append(text_valore)
        return jsonify(appoggio)
=======
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
>>>>>>> parent of 5a1dca8 (Update Progetto_moda.py)

    @doc(description='API per il conteggio del numero di immagini per classe.', tags=['Immagini'])
    @use_kwargs(FashionRequestSchema, location=('json'))
    @marshal_with(FashionResponseSchema)  # marshalling
    def get(self):
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
    text_valore = {f'Le foto con piu\' di un oggetto di classi diverse sono': str(contatore)}
    return text_valore


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
        text_valore = {f'I colori dominanti per l\'immagine {jpg} sono': str(esadecimali)}
        return text_valore

        #return "I colori dominanti per l'immagine " + jpg + " sono " + str(esadecimali)
    else:
        return "Errore: Non hai specificato l'immagine. Riprova specificando l'immagine'."


@app.route('/ssd')
def ssd():
    if 'img' in request.args:
        jpg = str(request.args['img'])
        import cv2
        import torch
        from PIL import Image

        # Model
        model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

        img1 = Image.open(jpg)  # PIL image
        img2 = cv2.imread(jpg)[:, :, ::-1]  # OpenCV image (BGR to RGB)
        imgs = [img1, img2]  # batch of images

        # Inference
        results = model(imgs, size=640)  # includes NMS

        # Results
        results.print()
        results.save()  # or .show()

        predictions = results.xyxy[0]  # img1 predictions (tensor)
        predictions2 = results.pandas().xyxy[0].to_json(orient="records")  # img1 predictions (pandas)

        return str(predictions) + "\n\n" + predictions2
    else:
        return "Errore: Non hai specificato un'immagine. Riprova specificando un'immagine corretta."

# API 4: Vgg16
@app.route('/predvgg')
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

        # img = cv2.resize(cv2.imread('./255201749_3778225.jpg'),(224,224))
        img_t = transform(img)
        batch_t = torch.unsqueeze(img_t, 0)

        # img = np.expand_dims(img, axis=0)
        model = models.vgg16(pretrained=True)
        # model.to(device)
        model.eval()
        predictions = model(batch_t)
        # text_valore = "Le predizioni per l\'immagine sono':"+str(predictions)
        result = str(predictions)
        #index_i = result.index('[')
        #index_f = result.index(']')
        #risultato_stampa = result[index_i: index_f + 2]
        return {f'Le predizioni per l\'immagine {jpg} sono': result}
    else:
        return "Errore: Non hai specificato un immagine. Riprova specificando un'immagine corretta."


app.run()
