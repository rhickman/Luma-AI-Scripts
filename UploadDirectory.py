import os
import requests

directory = input("Enter the directory path (default is current directory): ") or "."
prefix = input("Enter the prefix for capture title (optional): ")

auth_headers = {'Authorization': f'luma-api-key={os.environ["LUMA_API_KEY"]}'}

file_counter = 0
for filename in os.listdir(directory):
    file_counter += 1
    if filename.endswith(".zip") or filename.endswith(".mp4"):
        capture_title = f"{prefix} {filename}" if prefix else filename
        
        print(f"Processing file {file_counter}: {filename}")
        response = requests.post("https://webapp.engineeringlumalabs.com/api/v2/capture",
                                 headers=auth_headers,
                                 data={'title': capture_title})
        capture_data = response.json()
        upload_url = capture_data['signedUrls']['source']
        slug = capture_data['capture']['slug']
        print("Capture data:", capture_data)
        
        print("Starting upload for file:", filename)
        with open(os.path.join(directory, filename), "rb") as f:
            payload = f.read()
        response = requests.put(upload_url, headers={'Content-Type': 'text/plain'}, data=payload)
        print("Upload completed for file:", filename)
        
        print("Triggering processing of slug:", slug)
        response = requests.post(f"https://webapp.engineeringlumalabs.com/api/v2/capture/{slug}",
                                 headers=auth_headers)
        print("Processing response:", response.text)
        print(f"{file_counter} of {len(os.listdir(directory))} files processed.")
    else:
        print(f"Skipping file {file_counter}: {filename}")
        print("File must be a .zip or .mp4 file.")
