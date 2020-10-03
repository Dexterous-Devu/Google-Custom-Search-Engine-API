
__author__ : '@rockdevu'

import requests     #pip install requests

# you can get API Key from this URL =   https://developers.google.com/custom-search/v1/introduction
API_key = "AIzaSyCEQ5n68LFSYAHQmzm0j3j0OocsY5DvnqY"

#you can get search engine ID from this URL = https://programmablesearchengine.google.com/cse/all
search_engine_id = "254a427d529329ede"

query = input('Enter Query : ')
page = 1
start = (page-1) * 10 + 1

url = f"https://www.googleapis.com/customsearch/v1?key={API_key}&cx={search_engine_id}&q={query}&start={start}"

data = requests.get(url).json()
search_items = data.get('items')

for i, search_item in enumerate(search_items, start=1):
    
    title = search_item.get("title")
    snippet = search_item.get("snippet")
    html_snippet = search_item.get("htmlSnippet")
    link = search_item.get("link")

    print('='*20, f'Result #{i+start-1}', '='*20)
    print()
    print("Title : ", title)
    print("Description : ", snippet)
    print("URl : ", link, "\n")
