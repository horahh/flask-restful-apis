# importing the requests library
import requests
  
# defining the api-endpoint 
API_ENDPOINT = "http://localhost:5000/incomes"
  
# your API key here
API_KEY = "XXXXXXXXXXXXXXXXX"
  
# data to be sent to api
data = { "amount": 100.0, "description": "example income" }
  
# sending post request and saving response as response object
requests.post(url = API_ENDPOINT, json = data)
  
# extracting response text 
pastebin_url = r.text
print("Post sent")
