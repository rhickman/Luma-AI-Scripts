import os
import requests
import json

auth_headers = {'Authorization': f'luma-api-key={os.environ["LUMA_API_KEY"]}'}

skip = 0
take = input("Enter the number of items to take (optional): ")
if take:
    take = int(take)
else:
    take = 3
url = f"https://webapp.engineeringlumalabs.com/api/v2/capture?skip={skip}&take={take}&order=DESC"

payload = {}

response = requests.request("GET", url, headers=auth_headers, data=payload)

captures = response.json()['captures']
for capture in captures:
    print('Title:', capture['title'])
    print('Status:', capture['status'])
    print('Date:', capture['date'])
    print('Slug:', capture['slug'])
    print('--------------------------')