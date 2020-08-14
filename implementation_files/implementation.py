import implementation_files.combined as combined
import implementation_files.constants as constants

def getFileList():
    lineList = combined.readPath(constants.PATHTOFILE)

    filesSetting = combined.getSingleSetting(lineList, constants.FILES_SETTING)
    fileList = combined.getMultipleSettings(filesSetting, constants.FILE_SETTING)

    return fileList

def getColumnList(lines):
    columnsSetting = combined.getSingleSetting(lines, constants.CHOOSE_COLUMNS_SETTING)
    columnList = combined.getMultipleSettings(columnsSetting, constants.COLUMN_SETTING)
    
    return columnList

def getWhereClauseList(lines):
    returnList = []

    clauseSetting = combined.getSingleSetting(lines, constants.WHERECLAUSE_SETTING)
    clauseList = combined.getMultipleSettings(clauseSetting, constants.CLAUSE_SETTING)

    for clause in clauseList:
        returnList.append({
            'column': combined.getSingleSettingAsString(clause, constants.COLUMN_SETTING),
            'equal': combined.getSingleSettingAsString(clause, constants.EQUAL_SETTING)
        })
    
    return returnList

def getIndexListHelper(dataDict, clause, inputList):
    returnList = []

    for x in range(0, len(dataDict['columns'][clause['column']])):
        if len(inputList) == 0:
            if dataDict['columns'][clause['column']][x] == clause['equal']:
                returnList.append(x)
        else:
            if dataDict['columns'][clause['column']][x] == clause['equal'] and x in inputList:
                returnList.append(x)

    return returnList

def getIndexList(dataDict, clauseList):
    indexList = []
    if len(clauseList) > 0:
        for clause in clauseList:
            if clause['column'] in dataDict['columnList']:
                indexList = getIndexListHelper(dataDict, clause, indexList)

    return indexList
        

def getDataSet(dataDict, name, clauseList):
    indexList = getIndexList(dataDict, clauseList)

    if len(indexList) == 0:
        return dataDict['columns'][name]
    else:
        returnList = []
        for x in range(0, len(dataDict['columns'][name])):
            if x in indexList:
                returnList.append(dataDict['columns'][name][x])

        return returnList


def playWithColumns(columnList, clauseList, dataDict):
    for column in columnList:
        name = combined.getSingleSettingAsString(column, constants.NAME_SETTING)
        newname = combined.getSingleSettingAsString(column, constants.NEWNAME_SETTING)
        
        if name in dataDict['columnList']:
            dataSet = getDataSet(dataDict, name, clauseList)
            print(dataSet)
        else:
            print("The column - " + name + " - could not be found. The settings are wrong in files.txt")
            print("Hence, the program will now quit")
            quit()

def addSeperationForDebugReasons():
    print()
    print()
    print()
    print()
    print()

def returnDataSet(lines):
    path = combined.getSingleSettingAsString(lines, constants.PATH_SETTING)
    delimeter = combined.getSingleSettingAsString(lines, constants.DELIMETER_SETTING)

    dataDict = combined.readCsvFile(constants.FILEFOLDER + '/' + path, delimeter)
    columnList = getColumnList(lines)
    clauseList = getWhereClauseList(lines)

    playWithColumns(columnList, clauseList, dataDict)


    # Comment out later on
    addSeperationForDebugReasons()



    

    

    

