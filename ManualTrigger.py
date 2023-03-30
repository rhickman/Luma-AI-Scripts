import os
import requests

auth_headers = {'Authorization': f'luma-api-key={os.environ["LUMA_API_KEY"]}'}

slug = input("Enter the slug: ")
url = f"https://webapp.engineeringlumalabs.com/api/v2/capture/{slug}"

payload = {}

response = requests.request("POST", url, headers=auth_headers, data=payload)

print(response.text)
