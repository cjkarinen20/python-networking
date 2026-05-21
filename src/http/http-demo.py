import http.client
import requests

# response = requests.get('https://www.example.com')
# print(response.status_code)
# print(response.text)

conn = http.client.HTTPSConnection("www.example.com")
conn.request("GET", "/")

response = conn.getresponse()
print(response.status, response.reason)

data = response.read()
print(data)

conn.close()