import requests
import json

with open("standart.json", "r") as test_standarts:
    data = json.load(test_standarts)

url = "https://jsonplaceholder.typicode.com/posts"
responce = requests.get(url)
json_response = json.loads(responce.text)


def api_test():
    for json_data in json_response:
        for key in data.keys():
            if key in json_data.keys():
                if data[key][2] == "int":
                    if not data[key][0] <= json_data[key] <= data[key][1]:
                        print("Failed ,because the range did not meet the standard we set for the user ")
                        return
                if data[key][2] == "string":
                    if not data[key][0] <= len(json_data[key]) < data[key][1]:
                        print("lens no match")
                        return
    print("All cases are okay")


api_test()
