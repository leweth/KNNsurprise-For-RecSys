import pickle
import json
from fastapi import FastAPI
from pydantic import BaseModel




# Création d'un instance de la clase FastAPI
app = FastAPI()




#Spécification des données d'entrées
class model_input(BaseModel):

    itemID      : str



#Le chargement du modèle
knn_model = pickle.load(open('KNNBaseline_itemBaseRec.pkl', 'rb'))

#Le chargement des données d'entrainnement
trainset = pickle.load(open('trainset.pkl', 'rb'))





@app.post('/item_based_recommendation')
def item_pred(input_parameters : model_input):


    input_data = input_parameters.json()
    input_dictionnary = json.loads(input_data)
    
    rawID = input_dictionnary['itemID']


    k = 15  # Number of similar items to retrieve
    similar_items = knn_model.get_neighbors(trainset.to_inner_iid(rawID), k)

    similar_items_rawIIDs = [trainset.to_raw_iid(inner_iid) for inner_iid in similar_items]
    
    return similar_items_rawIIDs 