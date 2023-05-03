#NOTE - use this file to format the json from ParseHub, deleting players Name and selection

import json

# Open the JSON file
with open('run_results.json', 'r') as file:
    data = json.load(file)
    print(data)

# Delete the attribute
for match in data["Matches"]:
    del match["name"]
    del match["selection2"]
    
# Write the updated JSON to the file
with open('file.json', 'w') as file:
    json.dump(data, file)
