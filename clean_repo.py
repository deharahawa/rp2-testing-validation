import re

with open('results.txt', 'r') as reader:
	for row in reader:
		clean = re.sub(r'https://github.com/', '', row)
		clean = re.sub(r' true', '', clean)
		with open('results_clean.txt', 'a') as results_writer:
			results_writer.write(clean)