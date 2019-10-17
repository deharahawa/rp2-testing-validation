#-*- coding: UTF-8 -*-

import csv
import requests
import re
import json

arquivo = open('/home/fernando/Documentos/USP/Resolução de Problemas 2/rp2-testing-validation/githubApi/list.csv')
coluna_nomes = csv.reader(arquivo)

requisicao = requests.get('http://localhost:3000/api/apps/io.github.hidroh.materialistic/reviews') 
print(type(requisicao))
