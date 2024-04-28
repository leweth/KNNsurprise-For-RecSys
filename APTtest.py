import requests
import json 

url =  'the htttp stuff/item_based_recommendation' #'.../endpoint'


input_data_for_model = {'userID'    : "A3DHAPM8LB4JYY"}



input_json = json.dumps(input_data_for_model)

response = requests.post(url, input_json)

if response.status_code == 200:
    # Parse the JSON response into a Python list
    recommended_products = response.json()
    
    # Print the recommended products
    print("Recommended products:", recommended_products)
else:
    print("Error:", response.status_code)