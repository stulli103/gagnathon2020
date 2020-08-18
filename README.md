# gagnathon2020

This is a python program that can generate custom made database tables and csv files from multiple csv files.

The real magic happens in the setting files of the program.
The program reads all the settings and how it should implement the return result from these files

One of those is the file implementation.txt where the user of the program chooses whether he wishes the program to return a csv file or a database table (good explanation text is to find in the file itself)

Another is the file db_settings.txt and should be used with the Database setting of the first file mentioned above.
The available settings the user can set in db_settings.txt are: 
1.  **###TableName**  
    It gives the user the control of deciding what the table name should be  
    If this setting is not set the set default table name in the program will be used (Table_23)  
    Example of usage  
    ```
    ###TableName
        LosunIslands
    ###TableName
    ```

2.  **###ColumnTypes**  
    This setting says the program that inside of this setting are multiple Column declarations where the user can set the type value of each column  
    Each Column declaration has its own setting called **###Column**  
    By default each column that is not represented in the ColumnTypes setting is given the value varchar(max)  
    Example of usage  
    ```
    ###ColumnTypes
        ###Column -> First column setting
            ###Name -> The name of the column
                Urgangur2018
            ###Name
            ###Type -> Declares the Column Type
                Float
            ###Type
        ###Column
        ###Column -> Second column setting
            ###Name
                Urgangur2017
            ###Name
            ###Type
                Float
            ###Type
        ###Column
    ###ColumnTypes
    ```


The magic of the program happens inside of the folder **files_to_run/**  
Inside of that folder the user can insert all of the setting text files for the .csv files he wants the program to run on  
In the folder **file_examples/** there comes a list of already made setting files for various .csv files that are stored in the folder **csv_files/**  
The name of the setting files in the **files_to_run/** do not matter as the program only reads the declared settings that are written in the files themselves  
All of the csv files the program can run on should be located in the folder **csv_files/**    

Here is an example of how one of those files work
```
###Path -- Required
    orkustofnun/os_vatnsafl.csv
###Path
###Delimeter -- Required
    ,
###Delimeter
###ChooseColumns -- Required
    ###Column -- Required ()
        ###Name -- Required (Must be the same as an existing column in the dataset)
            Virkjun
        ###Name
    ###Column
    ###Column -- Required
        ###Name -- Required (Must be the same as an existing column in the dataset)
            Tala1
        ###Name
        ###NewName
            MikilvaegTala
        ###NewName
    ###Column
    ###Column -- Required
        ###Name -- Required (Must be the same as an existing column in the dataset)
            Tala2
        ###Name
    ###Column
###ChooseColumns
###WhereClause
    ###Clause
        ###Column
            Ar
        ###Column
        ###Equal
            2014
        ###Equal
    ###Clause
    ###Clause
        ###Column
            Orkustofnun
        ###Column
        ###Equal
            Fallorka
        ###Equal
    ###Clause
###WhereClause
```