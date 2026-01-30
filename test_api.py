
import urllib.request
import json

try:
    url = "http://127.0.0.1:8000/api/products/"
    print(f"Fetching {url}...")
    with urllib.request.urlopen(url) as response:
        data = response.read()
        json_data = json.loads(data)
        print(f"Status: {response.status}")
        print(f"Type: {type(json_data)}")
        if isinstance(json_data, list):
            print(f"Count: {len(json_data)}")
            if len(json_data) > 0:
                print("First item sample:", json_data[0])
        else:
            print("Response is not a list.")
            print(json_data)
except Exception as e:
    print(f"Error: {e}")
