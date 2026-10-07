""" 
Api Key: free_user_3KHEdMDXaZEc9dAS44DLETWulNE

Endpoint: https://reqres.in/api/collections/products/records
"x-api-key": "pro_e48c2563adfb3b444d4f9a253cad62774a6e0c84e197d4d0"
"""

import requests

endPoint = "https://reqres.in/api/collections/products/records"
api_key = "pro_e48c2563adfb3b444d4f9a253cad62774a6e0c84e197d4d0"

headers = {
    "x-api-key":api_key
}

res = requests.get(
    endPoint,
    headers=headers
)

print(res)