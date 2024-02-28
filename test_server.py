import requests


# To test the code run this in the terminal with uvicorn running
print(requests.get("http://127.0.0.1:8000/").json())

print(requests.get("http://127.0.0.1:8000/items/2").json())

#print(requests.get("http://127.0.0.1:8000/items/10").json())

print(requests.get("http://127.0.0.1:8000/items?name=Nails").json())