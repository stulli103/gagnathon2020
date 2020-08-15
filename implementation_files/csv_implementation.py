import implementation_files.combined as combined
import implementation_files.implementation as implementation
import csv

PATH = 'result/csv_result.csv'

def createSingleDataSet():
    returnList = []

    fileList = implementation.getFileList()
    for file in fileList:
        dataSet = implementation.returnDataSet(file)
        for point in dataSet:
            returnList.append(point)

    return returnList

def setupFieldNamesList(dataSet):
    returnList = []
    for point in dataSet:
        returnList.append(point['columnName'])

    return returnList

def findLongestDataset(dataSet):
    highestNumber = 0
    for point in dataSet:
        if len(point['dataset']) > highestNumber:
            highestNumber = len(point['dataset'])

    return highestNumber

def setupWriteRowDict(index, dataSet, fieldNames):
    returnDict = {}
    for field in fieldNames:
        for point in dataSet:
            if field == point['columnName']:
                if len(point['dataset']) > index:
                    returnDict[field] = point['dataset'][index]
                else:
                    returnDict[field] = None

    return returnDict

def insertDataPoints(writer, dataSet, fieldNames):
    highestNumber = findLongestDataset(dataSet)
    for x in range(0, highestNumber):
        writer.writerow(
            setupWriteRowDict(x, dataSet, fieldNames)
        )

def writeFile(dataSet):
    with open(PATH, 'w', newline='') as file:
        fieldNames = setupFieldNamesList(dataSet)
        writer = csv.DictWriter(file, fieldnames=fieldNames)
        writer.writeheader()

        insertDataPoints(writer, dataSet, fieldNames)

def implement():
    dataSet = createSingleDataSet()
    writeFile(dataSet)

    
