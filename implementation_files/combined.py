import csv

def readCsvFile(path, dm = ';'):
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

    print(returnDict['columns'].keys())
    print(returnDict['columns']['Desember'])

    return returnDict
                