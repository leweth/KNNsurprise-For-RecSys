import pickle
import json
from fastapi import FastAPI
from pydantic import BaseModel

import pandas as pd
from surprise import KNNWithMeans
from surprise import Dataset
from surprise import Reader





 
df = pd.read_csv('ratings_Electronics.csv')
reader = Reader(rating_scale=(1, 5))
surprise_data = Dataset.load_from_df(df,reader)




app = FastAPI()


class model_input(BaseModel):

    userID      : str



KNNsurpriseModel = pickle.load(open('KNNsurprise.sva', 'rb'))



@app.post('/item_based_recommendation')
def item_pred(input_parameters : model_input):

    input_data = input_parameters.json()
    input_dictionnary = json.loads(input_data)
    
    user_id = input_dictionnary['userid']



    # Get all unique item IDs in the dataset that are not rated by the specified user
    all_item_ids = set(iid for uid, iid, _ in surprise_data.raw_ratings if uid != user_id)

    # Make predictions for all items for the specified user
    predictions = [KNNsurpriseModel.predict(user_id, item_id) for item_id in all_item_ids]

    # I added this to get only the top 50 products
    sorted_predictions = sorted(predictions, key=lambda x: x.est, reverse=True)[:50]

    # Print predictions
    for prediction in sorted_predictions:
        print(f"Predicted rating for user {user_id} on item {prediction.iid}: {prediction.est}")

    


    # We can later store the products id we want then transfer them to website for them to be shown
    recommended_products = [product.est for product in sorted_predictions]


    return recommended_products