import requests


url =  'http://127.0.0.1:8000/item_based_recommendation' #'.../endpoint'

input_data_for_model = {'itemID': "B00002JV62"}
response = requests.post(url, json=input_data_for_model)



# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Convert the JSON response to a Python list
    recommendation_array = response.json()
    
    # Print the array
    print(recommendation_array)
else:
    print("Error:", response.status_code)