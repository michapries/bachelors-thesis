import csv

country_prefixes = ['england', 'germany', 'italy', 'spain']

years = range(10, 19)           # years in which the seasons began (10 to 18); no 19/20 because it has an extra column

header_set = False

# clear any previous content in results.csv
with open('results.csv', 'w', newline='') as results:
    results.write('')

for country in country_prefixes:
    for year in years:
        file_name = country + '_' + str(year) + '_' + str(year + 1) + '.csv'

        with open(file_name, newline='') as csvfile:
            csvdata = csv.reader(csvfile, delimiter=',')

            header = next(csvdata, None)            # remove header

            with open('results.csv', 'a', newline='') as results:
                writer = csv.writer(results)

                # set header exactly once
                if header_set == False:
                    if 'england' in file_name:
                        writer.writerow(header[:10] + header[11:23])
                    else:
                        writer.writerow(header[:22])
                    header_set = True

                # write rows to csv
                for row in csvdata:
                    if 'england' in file_name:
                        writer.writerow(row[:10] + row[11:23])
                    else:
                        writer.writerow(row[:22])
