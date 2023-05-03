import CSVs
import rlAI
import time

if __name__ == '__main__':
    print('Starting..\n')
    time.sleep(1)
    print('Ids: ' + str(rlAI.getIds())+'\n')
    time.sleep(1)
    print('URLs: ' + str(CSVs.getUrls(rlAI.getIds()))+'\n')
    time.sleep(1)
    print('URLs len: ' + str(len(CSVs.getUrls(rlAI.getIds()))))
    time.sleep(1)
    print('Creating CSVs..\n')
    CSVs.createCSV(CSVs.getUrls(rlAI.getIds()))