import implementation_files.combined as combined
import implementation_files.implementation as implementation
import implementation_files.constants as constants

DEFAULTCOLUMNSETTING = 'varchar(max)'
CREATETABLEPATH = 'result/db/create_table.txt'
INSERTSTATEMENTSPATH = 'result/db/insert_statements.sql'

def getColumnSettings(lineList):
    returnList = []
    columnTypes = combined.getSingleSetting(lineList, constants.COLUMN_TYPES_SETTING)
    columns = combined.getMultipleSettings(columnTypes, constants.COLUMN_SETTING)

    for col in columns:
        dict = {}
        name = combined.getSingleSettingAsString(col, constants.NAME_SETTING)
        type = combined.getSingleSettingAsString(col, constants.TYPE_SETTING)

        dict['name'] = name
        if type != None and type != '':
            dict['type'] = type
        else:
            dict['type'] = DEFAULTCOLUMNSETTING

        returnList.append(dict)

    return returnList

def getColumnType(colSettings, columnName):
    for col in colSettings:
        if col['name'] == columnName:
            return col['type']

    return DEFAULTCOLUMNSETTING

def getColumnList(dataSet, lineList):
    colSettings = getColumnSettings(lineList)

    returnList = []
    for point in dataSet:
        dict = {}
        dict['columnName'] = point['columnName']
        dict['type'] = getColumnType(colSettings, point['columnName'])

        returnList.append(dict)

    return returnList

def getTableName(lineList):
    tableName = combined.getSingleSettingAsString(lineList, constants.TABLENAME_SETTING)
    if tableName == '' or tableName == None:
        print("Table name was not set in implementation.txt")
        print("Hence default table name is set (Table_23)")
        tableName = 'Table_23'

    return tableName

def createTableStatement(dataSet, tableName, colList):
    createTable = 'Create Table [dbo].[' + tableName + '](\n'
    createTable = createTable + '\tId [int] Identity(1,1) NOT NULL'
    for col in colList:
        createTable = createTable + '\n\t' + col['columnName'] + ' ' + col['type'] + ', '
    
    createTable = createTable[:-1] + '\n'
    createTable = createTable + ');'

    f = open(CREATETABLEPATH, 'w+')
    f.write(createTable)

def addColumnsToDataSet(colList):
    returnString = ''

    for col in colList:
        returnString = returnString + col['columnName'] + ', '

    if returnString != '':
        return returnString[:-2]

    return returnString

def columnsIsOfStringType(columnName, colList):
    for col in colList:
        if columnName == col['columnName']:
            if 'varchar' not in col['type']:
                return False
            break

    return True

def addValuesToDataSet(dataSet, index, colList):
    returnString = ''

    for point in dataSet:
        if len(point['dataset']) > index:
            if columnsIsOfStringType(point['columnName'], colList):
                returnString = returnString + "'" + point['dataset'][index] + "', "
            else:
                returnString = returnString + point['dataset'][index] + ", "
        else:
            returnString = returnString + "Null, "

    if returnString != '':
        return returnString[:-2]

    return returnString

def insertDataset(dataSet, tableName, colList):
    highestNumber = combined.findLongestDataset(dataSet)

    f = open(INSERTSTATEMENTSPATH, 'w+')
    for x in range(0, highestNumber):
        statement = 'Insert into [dbo].[' + tableName + '] (' + addColumnsToDataSet(colList) + ') values (' + addValuesToDataSet(dataSet, x, colList) + ');\n'
        f.write(statement)


def writeFile(dataSet, tableName, colList):
    createTableStatement(dataSet, tableName, colList)
    insertDataset(dataSet, tableName, colList)

def implement():
    lineList = combined.readPath(constants.PATHTODBSETTINGS)

    tableName = getTableName(lineList)
    dataSet = combined.createSingleDataSet()
    colList = getColumnList(dataSet, lineList)
    writeFile(dataSet, tableName, colList)


# CREATE TABLE Persons (
#     PersonID int,
#     LastName varchar(255),
#     FirstName varchar(255),
#     Address varchar(255),
#     City varchar(255)
# );



# CREATE TABLE [dbo].[ApiResource](
# 	[Id] [int] IDENTITY(1,1) NOT NULL,
# 	[Name] [varchar](100) NOT NULL,
# 	[DisplayName] [varchar](100) NOT NULL,
# 	[Description] [varchar](max) NOT NULL,
# 	[Enabled] [varchar](1) NOT NULL