import json
import os

#NOTE - use this method to format the Json from ParseHub
def formatJson(jsonFile):
    with open(jsonFile, 'r') as file:
        data = json.load(file)
        print(data)

    for match in data["Matches"]:
        del match["name"]
        del match["selection2"]

    with open('file.json', 'w') as file:
        json.dump(data, file)
    
    os.remove(jsonFile)
    print('JSON formatted as "file.json"')

#NOTE - use this method to get matchs ids
def getIds(jsonFileFormatted):
    ids = []
    with open(jsonFileFormatted, 'r') as file:
        data = json.load(file)
    for match in data["Matches"]:
        rs = match['url']
        rs = str(rs)
        ids.append(rs[31:])
    return ids
