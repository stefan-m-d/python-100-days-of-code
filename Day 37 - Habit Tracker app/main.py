import requests
from datetime import datetime

today = datetime.today()
formatted_date = today.strftime("%Y %m %d").replace(" ", "")

#step 1 - set up user

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "" #username you've chosen
TOKEN = "" #token you've created

user_params = {
    "token": "", #this is made up by you, the user
    "username": "", #this, like the above is made up by you, the user
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
#  above 2 lines should be run when creating a new user only. You still need the user_params dictionary

# step 2 - create graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# use the above 2 lines when creating the graph only, you don't need them afterwards

# step 3 is to get the graph via URL - https://pixe.la/v1/users/<username>/graphs/<graphID>.html

# step 4 - post to the graph

post_to_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"



pixel_config = {
    "date": formatted_date,
    "quantity": "5.25" #you make this stuff up or if you're following a habit graph, you put in however many kms you've cycled
}

# response = requests.post(url=post_to_graph_endpoint, json=pixel_config, headers=headers)
# print (response.text)
# run the above 2 lines to make a new post to the graph


#step 5 - update pixel, this requires at least 2 pixels, so if you don't have 2, change the formatted_date variable to something like 20240423 or another sample yyyymmdd format and run the request to post something

date_to_update = "20240423" #change this to any date you wanna update, the format is yyyymmdd

post_to_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{date_to_update}"

pixel_config = {
    "quantity": "40.15"
}

# response = requests.put(url=post_to_graph_endpoint, json=pixel_config, headers=headers)
# print (response.text)
# same as above for these 2 lines - run them if you want to update a pixel


# step 6, final step, delete a pixel

response = requests.delete(url=post_to_graph_endpoint, headers=headers)
print (response.text)