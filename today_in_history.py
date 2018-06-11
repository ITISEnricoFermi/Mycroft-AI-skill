import requests

url = "https://history.muffinlabs.com/date"

data = requests.get(url).json().get("data")


print(data.keys())
