import implementation_files.combined as combined
import implementation_files.csv_implementation as csv_implementation
import implementation_files.db_implementation as db_implementation


IMPLEMENTATIONPATH = './setting_files/implementation.txt'
AVAILABLEOPTIONS = ['CSV', 'DB', 'NOSQL']

def readImplementationFile():
    lineList = combined.readPath(IMPLEMENTATIONPATH)

    for line in lineList:
        if '##' not in line and line.strip() != '':
            return line.strip()
            
    return None

def csv():
    csv_implementation.implement()

def db():
    db_implementation.implement()

def implement():
    implementation = readImplementationFile()

    if implementation == None or implementation not in AVAILABLEOPTIONS:
        print("implementation.txt is not implemented correctly. No implementation type is setup correctly")
    else:
        impFunctions = {
            'CSV': csv,
            'DB': db,
        }
        impFunctions.get(implementation)()