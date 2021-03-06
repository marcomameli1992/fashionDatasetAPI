# Fashion Dataset API

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
#### **API N°2:** CONTEGGIO DI IMMAGINI CON PIU' DI UN OGGETTO DENTRO

###### /molti_oggetti/all

Questa API restituisce un JSON contenente il numero di immagini che hanno più di un oggetto al loro interno. Il risultato è il seguente:

```
{
  "Le_foto_con_piu_oggetti_presenti_sono": 0
}
```
----
----
#### **API N°2.1:** CONTEGGIO DI IMMAGINI CON PIU' DI UN OGGETTO DELLA STESSA CLASSE DENTRO

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
#### **API N°2.2:** CONTEGGIO DI IMMAGINI CON PIU' DI UN OGGETTO DI CLASSI DIVERSE DENTRO

###### /molti_oggetti/molte_classi

Questa API restituisce un JSON contenente il numero di immagini che hanno più di un oggetto di classi diverse al loro interno. Il risultato è il seguente:

```
{
  "Le_foto_con piu_di_un_oggetto_di_classi_diverse_sono": 0
}
```
----
----
#### **API N°3:** VALUTAZIONE DEL COLORE DOMINANTE DI UNA DETERMINATA IMMAGINE

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
#### **API N°4:** RICONOSCIMENTO OGGETTI PERSENTI IN UN'IMMAGINE CON MODELLO YOLOv5

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
#### **API N°5:** RICONOSCIMENTO OGGETTI PERSENTI IN UN'IMMAGINE CON MODELLO VGG

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