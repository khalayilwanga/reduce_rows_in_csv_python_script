import csv


def reduce_rows():
    with open('CHRIS_metadata.csv', 'r') as inp, open('CHRIS_edited.csv', 'w', newline="") as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            x = row[0]
            if x[-1] == '1':
                writer.writerow(row)


if __name__ == "__main__":
    reduce_rows()
