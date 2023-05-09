#NOTE - from the json formatted, use this file to download all the csv
import requests
import time
import pandas as pd
import os

#NOTE - use this method to get csv download url for every match
def getUrls(ids):
    urls = []
    for id in ids:
        url = 'https://ballchasing.com/dl/stats/players/'+id+'/'+id+'-players.csv'
        urls.append(url)
    return urls 

#NOTE - use this method to merge all the csv files
def mergeCSVs(files):
    print('Merging files..\n')
    dataFrame = pd.DataFrame()
    for file in files:
        print('CSV name: '+str(file))
        data = pd.read_csv(file)
        dataFrame = pd.concat([dataFrame, data], axis=0)
    dataFrame.to_csv('allMatches.csv', index=False)
    print('Merge done\n')

#NOTE - use this method to download all the csv files
def createCSV(urls):
    i = 0
    files = []
    toBeDeleted = []
    for url in urls:
        print('Numero: '+str(i)+': '+str(url))
        rs = requests.get(url)
        name = 'match'+str(i)+'.csv'
        open(name, 'wb').write(rs.content)
        print('File '+name+' creato')
        toBeDeleted.append(str(name))
        print('Controllo file..')
        with open(str(name)) as file:
            if(file.readline(5)) == 'color':
                print('File idoneo')
                files.append(str(name))
            else:
                print('File corrotto')
        i += 1
        time.sleep(5)
    mergeCSVs(files)
    print('Removing old files..\n')
    for badFile in toBeDeleted:
        os.remove(badFile)