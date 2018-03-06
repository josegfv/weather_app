#!/usr/bin/python
"""
Usage: copyNoDuplicate (-s <filename> -c <col> | -h)

Options:
  -h              Help.
  -s <filename>   This is the name of the source CSV file
  -c <col>        Provide the column number where to look for duplicates


Examples:
    copyNoDuplicates -s Myfile.csv -c 3

"""
import csv
try:
    from docopt import docopt
except ImportError:
    print("docopt library missing..\nPlease install by executing the following command:")
    print("pip3 install docopt")


def main():
    singleValues = []
    column = 0
    lc = ""
    # Collects the arguments passed to the script from command line
    arguments = docopt(__doc__, version='0.1')

    # Act upon the arguments passed
    #print(arguments)
    if arguments.get('-s') != None and arguments.get('-c') != None:
        # Uploads file to transfer.sh and if successful adds the file to the DB
        fileName = arguments.get('-s')
        column = int(arguments.get('-c'))
    else:
        print("Something Wrong, we should not be here...")
        exit()

    fdst = open(fileName+'_new', "w", encoding='utf-8', errors='ignore')
    writer = csv.writer(fdst, lineterminator='\n')

    with open(fileName, 'r', encoding='utf-8', errors='replace', newline=None) as fsrc:
        reader = csv.reader(fsrc)
        for row in reader:
            #Check if the row exists or is not empty
            if row:
                #Assigns the value in the specified column position to a variable
                lc = row[column]
                #print(row)
                if not singleValues.count(lc):
                    singleValues.append(lc)
                    writer.writerow(row)
                    #print("Line added for city: {}".format(lc.encode('utf-8')))

    fsrc.close()
    fdst.close()


if __name__ == '__main__':
    main()
