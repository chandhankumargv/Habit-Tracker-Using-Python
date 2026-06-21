import requests
from datetime import datetime

# ----------------------------
# USER CONFIGURATION
# ----------------------------
USERNAME = "your_username"
TOKEN = "your_secure_token"
GRAPH_ID = "codinggraph"

pixela_endpoint = "https://pixe.la/v1/users"

# ----------------------------
# CREATE USER (RUN ONLY ONCE)
# ----------------------------

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Uncomment below to create user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# ----------------------------
# CREATE GRAPH (RUN ONLY ONCE)
# ----------------------------

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Daily Coding Hours",
    "unit": "hours",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Uncomment below to create graph
# response = requests.post(
#     url=graph_endpoint,
#     json=graph_config,
#     headers=headers
# )
# print(response.text)


# ----------------------------
# ADD TODAY'S DATA
# ----------------------------

today = datetime.now()

pixel_endpoint = (
    f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
)

hours = input("How many hours did you code today? ")

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": hours
}

response = requests.post(
    url=pixel_endpoint,
    json=pixel_data,
    headers=headers
)

print(response.text)
