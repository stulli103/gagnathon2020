import implementation_files.combined as combined
import implementation_files.implementation as implementation

def implement():
    fileList = implementation.getFileList()
    for file in fileList:
        dataSet = implementation.returnDataSet(file)