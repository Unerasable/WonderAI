import json

with open('./data/responses.json') as f:
    data = json.load(f)

while True:
    q = input()

    for i in data:
        if q in data[i]:
            print(data[i][q])
        else:
            print("Sorry, I don't know that.")