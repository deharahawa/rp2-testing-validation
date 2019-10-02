#-*- coding: UTF-8 -*-

import csv
import requests
import re

arquivo = open('/home/fernando/Documentos/USP/Resolução de Problemas 2/rp2-testing-validation/githubApi/list.csv')
coluna_nomes = csv.reader(arquivo)

#for identificador in coluna_nomes:
    #nome_app = identificador[1]
requisicao = requests.get('http://localhost:3000/api/apps/io.github.hidroh.materialistic/reviews') 
comentarios = re.search(r'\btext\b', requisicao.text)
print(comentarios)
