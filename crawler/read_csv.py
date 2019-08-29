import csv

class Read_csv:
    def repo_github():
        csv_path = 'githubdata-MA663.csv'
        paths = []
        with open(csv_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                    if (row[2] == 'repo'):
                        continue
                    paths.append(row[2])
        return paths

    if __name__ == '__main__':
        repo_github()