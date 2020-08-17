import implementation_files.combined as combined
import implementation_files.settings as settings

def main():
    settings.implement()


def test():
    print(combined.readCsvFile('csv_files/orkustofnun/os_borholur.csv', '\t'))

# main()
test()