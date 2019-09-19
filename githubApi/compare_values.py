import csv
import os

path_tests = "/home/andre/usp/6_semestre/RP2/results_clean.txt"
path_repos = "/home/andre/usp/6_semestre/RP2/githubApi/list.csv"

repos = open(path_repos)
reader_repos = csv.reader(repos, delimiter=',')

for row_repos in reader_repos:
	for column_repos in row_repos:
		with open(path_tests, 'r') as reader:
			line = reader.readline()
			while line != '':
				if line == column_repos+'\n':
					print(line)
					with open('results_com_testes.csv', 'a', newline='') as myfile:
					     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
					     wr.writerow(row_repos)
				line = reader.readline()
			# if column_repos == 
			