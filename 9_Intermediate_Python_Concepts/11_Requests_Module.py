'''
The Python Requests module is an HTTP library that enables developers to send HTTP requests in Python.
This module enables you to send HTTP requests using Python code and makes it possible to interact with APIs and web services.
'''
# Get Request: Sends a GET request
import requests
response = requests.get("https://www.google.com")
print(response.text)


''' Post Request:  Sends a POST request to a web service and includes a custom header'''
# url = "https://api.example.com/login"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
#     "Content-Type": "application/json"
# }
# data = {
#     "username": "myusername",
#     "password": "mypassword"
# }

# response = requests.post(url, headers=headers, json=data)
# print(response.text)

'''In this example, we send a POST request to a web service to authenticate a user. We include a custom User-Agent header and a JSON payload with the user's credentials.
This POST requests code snippet will give error as the given url does not exist. It's just an example.'''
