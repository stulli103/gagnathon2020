import csv

def readCsvFile(path, dm):
    returnDict = {
        'columnList': [],
        'columns': {}
    }

    with open(path, encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=dm)
        fetchColumns = True
        for row in csv_reader:
            if fetchColumns == True:
                returnDict['columnList'] = row
                for item in row:
                    returnDict['columns'][item] = []
                fetchColumns = False
            else:
                for x in range(0, len(row)):
                    returnDict['columns'][returnDict['columnList'][x]].append(row[x])

    return returnDict
                
def readPath(path):
    lineList = []

    for line in open(path, 'r', encoding="utf8"):
        lineList.append(line)

    return lineList

def getSingleSetting(listOfLines, setting):
    lineList = []
    startAdding = False

    for line in listOfLines:
        if startAdding == True:
            lineList.append(line)

        if setting in line:
            startAdding = not startAdding

    return lineList[:-1]

def getSingleSettingAsString(listOfLines, setting):
    returnString = ''

    startAdding = False

    for line in listOfLines:
        if startAdding == True:
            if setting not in line:
                returnString = returnString + line

        if setting in line:
            startAdding = not startAdding

    return returnString.strip()

def getMultipleSettings(listOfLines, setting):
    returnList = []
    
    lineList = []
    startAdding = False

    for line in listOfLines:
        if startAdding == True:
            lineList.append(line)

        if setting in line:
            if startAdding == True:
                returnList.append(lineList[:-1])
                lineList = []
            startAdding = not startAdding

    return returnList