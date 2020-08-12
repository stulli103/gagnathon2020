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

def playWithColumns(columnList, dataDict):
    for column in columnList:
        name = combined.getSingleSettingAsString(column, constants.NAME_SETTING)
        newname = combined.getSingleSettingAsString(column, constants.NEWNAME_SETTING)
        
        ## Todo -> Add where clause to the mix here
        if name in dataDict['columnList']:
            print(dataDict['columns'][name])
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

    playWithColumns(columnList, dataDict)


    # Remove later on
    addSeperationForDebugReasons()



    

    

    

