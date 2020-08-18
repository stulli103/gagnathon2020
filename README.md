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

There are a lot of available settings available in the files located int the folder **files_to_run/**  
1.  **###Path**  
    This setting declares where inside the **csv_files** the file the specific settings that follows is to be found  
    This setting is required in each file  
    Example of usage
    ```
    ###Path -- Required
        orkustofnun/os_vatnsafl.csv
    ###Path
    ```

2.  **###Delimeter**  
    This setting declares what delimeter the .csv file the path settings uses to split the dataset  
    This setting is required in each file 
    Example of usage
    ```
    ###Delimeter -- Required
        ,
    ###Delimeter
    ```

3.  **###ChooseColumns**  
    This setting stores all of the columns the user wants to retrieve from the .csv file and put in his own  
    This setting has other settings for each and every column  
    Every file must have this setting, otherwise there is no point in having the .txt file  
    -   ###Column  
        This setting stores what Column the user wants from the .csv file  
        The name of the column must be the same as an existing column in the .csv file
        The user can add as many Column settings as he likes to the ChooseColumns setting  
        Every ChooseColumns setting must have at least one Column setting  
        -   ###Name  
            Declares the name of the Column in the .csv file that the user wants to extract
        -   ###NewName  
            The user can rename the column for the new generated file if he likes  
            By default the setting is the name of the column  
    Example of usage
    ```
    ###ChooseColumns -- Required
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
    ```

4.  **###WhereClause**  
    This setting allows the user to choose only the data from the .csv file in the path settings that fulfills specific requirements  
    As of now, the only available clause is the equivalence to the **'Where'** command in sql query language but the plan is to have more options in the future    
    This is an optional setting and is therefore not required  
    Just like the ###ChooseColumns setting, this setting stores a list of all of the clauses the user wants to add to the dataset in the .csv file  which have their own settings  
    -   ###Clause  
        This setting, just like the Column setting above, can be added as often as the user wants to the WhereClause setting  
        This setting stores info about each clause and has it´s own settings  
        -   ###Column  
            Declares the column the WhereClause should work on  
        -   ###Equal  
            Declares the value that the Column should equal to  
    Example of usage
    ```
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
    The equivalent sql query would be 
    ```
        select * from ---someTableName--- where Ar = 2014 and Orkustofnun = 'Fallorka'
    ```
        

Here is an example of how one of those files could look like with all of the settings above  
```
###Path -- Required
    orkustofnun/os_vatnsafl.csv
###Path
###Delimeter -- Required
    ,
###Delimeter
###ChooseColumns -- Required
    ###Column -- Required
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