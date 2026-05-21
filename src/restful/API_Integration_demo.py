import requests

api_endpoint = "https://jsonplaceholder.typicode.com/posts/1"

update_data = {
    'id': 1,
    'title': 'Updated Title',
    'body': 'updated BODY',
    'userID': 1
}

response = requests.delete(api_endpoint)

if response.status_code == 200:
    print("Data deleted successfully")
    print(response.json())
else:
    print("Failed to retrieve data")