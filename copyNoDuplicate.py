import csv


def main():
    singleValues = []

    fdst = open("./GeoLiteCity-Location-short.csv",
                "w", encoding='utf-8', errors='ignore')
    writer = csv.writer(fdst)

    with open('./GeoLiteCity-Location.csv', 'r', encoding='utf-8', errors='replace') as fsrc:
        reader = csv.reader(fsrc)
        for row in reader:
            lc = row[3]
            if not singleValues.count(lc):
                singleValues.append(lc)
                writer.writerow(row)
                #print("Line added for city: {}".format(lc.encode('utf-8')))

    fsrc.close()
    fdst.close()

if __name__ == '__main__':
    main()
