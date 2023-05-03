import requests
import json

with open('run_results.json', 'r') as file:
    data = json.load(file)

def getIds():
    ids = []
    for match in data["Matches"]:
        rs = match['url']
        rs = str(rs)
        ids.append(rs[31:])
    return ids
    