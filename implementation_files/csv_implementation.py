import implementation_files.combined as combined
import implementation_files.implementation as implementation
import csv

PATH = 'result/csv/csv_result.csv'

def setupFieldNamesList(dataSet):
    returnList = []
    for point in dataSet:
        returnList.append(point['columnName'])

    return returnList

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
    highestNumber = combined.findLongestDataset(dataSet)
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
    dataSet = combined.createSingleDataSet()
    writeFile(dataSet)

    
