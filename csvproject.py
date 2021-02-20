import csv
import operator


def csvsort(input, output, columnchoice):
    readable = open(input, 'r')
    writeable = open(output, 'w')
    csv_readable = csv.reader(readable, delimiter=',')
    readable_sorted = \
        sorted(csv_readable, key=operator.itemgetter(int(columnchoice)))
    csv_writeable = csv.writer(writeable, delimiter=',')
    for line in readable_sorted:
        csv_writeable.writerow(line)
