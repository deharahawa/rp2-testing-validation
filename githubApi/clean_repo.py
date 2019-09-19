import re

with open('results.txt', 'r') as reader:
	for row in reader:
		clean = re.sub(r'https://github.com/', '', row)
		clean = re.sub(r'true', '', clean)
		print(clean)