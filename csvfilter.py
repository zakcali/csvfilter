# csv filter by Zafer Akçalı, selects specified fields/columns from a csv file
# my purpose was to create a database file from wos2q utility for my institution's publication library
import csv, os

csvRows = []
EXTENSION = '.csv'
ENCODING = 'utf-8-sig'
SEPERATOR = '\t'
FIELDS = ['Q', 'scie', 'ssci', 'ahci', 'esci', 'istp', 'isshp', 'bsci', 'bhci', 'Method', 'Wos number', 'Doc type',
          'Cited', 'Auth.#', 'p.Year', 'ea.Year', 'Year', 'Journal', 'Journ', 'Book', 'issn', 'eissn', 'isbn', 'Title',
          'Doi', 'Vol.', 'Issue', 'Page.S', 'Page.E', 'Artic.Nr', 'Ref.style', 'PMID', 'Pub type', 'Publisher',
          'Book doi', 'Authors', 'gAuthors', 'Book auth', 'Book ed', 'Abstr', 'M.Abstr']

for csvFilename in os.listdir('.'):
    if not csvFilename.endswith(EXTENSION):
        continue  # skip non-csv files
    print('Writing filtered-' + csvFilename + '...')
    inputFile = open(csvFilename, newline='', encoding=ENCODING)
    outputFile = open('filtered-'+csvFilename, 'w', newline='', encoding='utf-8')

    readerObj = csv.DictReader(inputFile, delimiter=SEPERATOR)
    writerObj = csv.DictWriter(outputFile, FIELDS, delimiter=SEPERATOR)
    writerObj.writeheader()
    for row in readerObj:  # Read rows
        rowDict = {}
        for field in FIELDS:
            rowDict[field] = row[field]
        writerObj.writerow(rowDict)
    inputFile.close()
    outputFile.close()
    break   # filter only first file
