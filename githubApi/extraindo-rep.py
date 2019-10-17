# -*- coding: UTF-8 -*
import csv
import requests
import json

arquivo = open('list.csv')
linhas  = csv.reader(arquivo)


for linha in linhas:
	nome_repo = str((linha[1]))
	print(nome_repo)
	url = 'http://localhost:3000/api/apps/?q='+nome_repo+'/reviews/'
	arquivo_json = requests.get(url).json()
	print(str(arquivo_json))
