"""Sort CSV files"""

import csv
import argparse


def readfile(inputfile: str) -> list:
    """Read a given file and return a list of column values"""
    inputlist = []
    with open(inputfile, "r", newline="") as readable:
        csv_read = csv.reader(readable, delimiter=",")
        for line in csv_read:
            inputlist.append(line)
    return inputlist


def sortdata(inputdata: list, columnchoice: str) -> list:
    """Sort data by column choice and return it"""
    if len(inputdata) == 0:
        raise ValueError("This list is empty")
    return [inputdata[0]] + sorted(
        inputdata[1:], key=lambda a: a[inputdata[0].index(columnchoice)]
    )


def writefile(data: list, outputfile: str) -> None:
    """Write data to a file"""
    with open(outputfile, "w", newline="") as writeable:
        csv_write = csv.writer(writeable, delimiter=",")
        for row in data:
            csv_write.writerow(row)


def csvsort(inputfile: str, outputfile: str, columnchoice: str) -> None:
    """Read input file, sort by column choice, save to a new file"""
    fileread = readfile(inputfile)
    sorteddata = sortdata(fileread, columnchoice)
    writefile(sorteddata, outputfile)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Sort a csv file and write it to a new file"
    )
    parser.add_argument("--inputfile", type=str, help="The input file")
    parser.add_argument("--outputfile", type=str, help="The output file")
    parser.add_argument(
        "--columnchoice", type=str, help="The column to be sorted by"
    )
    args = parser.parse_args()

    csvsort(args.inputfile, args.outputfile, args.columnchoice)
