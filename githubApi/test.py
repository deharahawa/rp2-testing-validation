import csv
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

test = open('./tested-repo.txt')
issues= open('./results.txt')


x = open('./results1.txt', 'w')

for a in issues:
	print (a.split(',')[0])
	for b in test:
		if a.split(',')[0] == b.split('\n')[0]:
			x.write(a)
	