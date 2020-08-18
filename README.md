# gagnathon2020

This is a python program that can generate custom made database tables and csv files from multiple csv files.

The real magic happens in the setting files of the program.
The program reads all the settings and how it should implement the return result from these files

One of those is the file implementation.txt where the user of the program chooses whether he wishes the program to return a csv file or a database table (good explanation text is to find in the file itself)

Another is the file db_settings.txt and should be used with the Database setting.
The available settings to control in this file are: 
1.  ###TableName
    It gives the user the control of deciding what the table name should be. If this setting is not set the default setting will be used (Table_23)
    Example of usage
    ###TableName
        LosunIslands
    ###TableName

2.  ###ColumnTypes
    This setting says the program that inside of this setting are multiple Column declarations where the user can set the type value of each column
    Each Column declaration has its own setting called ###Column
    By default each column that is not represented in the ColumnTypes setting is varchar(max)
    Example of usage
    ###ColumnTypes
        ###Column
            ###Name -> The name of the column
                Urgangur2018
            ###Name
            ###Type -> Declares the Column Type
                Float
            ###Type
        ###Column
        ###Column
            ###Name
                Urgangur2017
            ###Name
            ###Type
                Float
            ###Type
        ###Column
    ###ColumnTypes


