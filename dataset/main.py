import CSVs
import JSONs
import time

formattedFile = 'example.json' #NOTE - replace this string with your formatted json

if __name__ == '__main__':
    print('Starting..\n')
    time.sleep(1)
    print('Ids: ' + str(JSONs.getIds(formattedFile))+'\n')
    time.sleep(1)
    print('URLs: ' + str(CSVs.getUrls(JSONs.getIds(formattedFile)))+'\n')
    time.sleep(1)
    print('URLs len: ' + str(len(CSVs.getUrls(JSONs.getIds(formattedFile)))))
    time.sleep(1)
    print('Creating CSVs..\n')
    CSVs.createCSV(CSVs.getUrls(JSONs.getIds(formattedFile)))