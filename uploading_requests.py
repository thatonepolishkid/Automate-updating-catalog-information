# Importing necessary modules.
import requests, os

folder = (r'Insert absolute path here.')
os.chdir(folder)

#Url needs to be replaced with the external IP address from the lab.
url = 'http://local-host-IP/fruits/'

# Instantiating the necessary lists and dictionaries.
list_of_dicts_to_push = []
name = {}
weight = {}
description = {}
image_name = {}

# Iterates through the specified directory and appends the lines to the list_of_dicts_to_push variable 
# **Maybe should put this into a function?
for file in os.listdir(folder):
    # Important to not forget this dictionary inside the loop or it will give the incorrect information.
    information = []
    with open(file, 'r') as text:
        for line in text:
            line = line.strip('\n')
            information.append(line)
    # Holder Dictionary for each loop.
    format_dict = {}
    name['name'] = information[0]
    weight['weight'] = information[1]
    description['description'] = information[2]
    image_name['image_name'] = information[3]
    format_dict |= name
    format_dict |= weight
    format_dict |= description
    format_dict |= image_name
    list_of_dicts_to_push.append(format_dict)


for dictionary in list_of_dicts_to_push:
    # Replace 'http://<corpweb-external-IP>/feedback' with the website you are trying to push to.
    response = requests.post(url, json=dictionary)
    if response.ok:
        print("Response has been received")
    if not response.ok:
        raise Exception(f"Get failed with status code {response.status_code}")