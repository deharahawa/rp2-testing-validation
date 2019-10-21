#-*- coding: UTF-8 -*-

import csv
import requests
import re
import json
from collections import Counter

#LER ARQUIVO DE REPOSITÓRIO, LISTA DE PALAVRAS POSITIVAS E NEGATIVAS
arquivo = open('/home/fernando/Documentos/USP/Resolução de Problemas 2/rp2-testing-validation/githubApi/list.csv')
repositorio_nomes = csv.reader(arquivo)

lista_palavras_positivas = open('/home/fernando/Documentos/USP/Resolução de Problemas 2/rp2-testing-validation/googleplay_analyser/lista_positvas.csv')
repositorio_positivo = csv.reader(lista_palavras_positivas)

lista_palavras_negativas = open('/home/fernando/Documentos/USP/Resolução de Problemas 2/rp2-testing-validation/googleplay_analyser/lista_negativas.csv')
repositorio_negativo = csv.reader(lista_palavras_negativas)

lista_positivas = []
lista_negativas = []
lista_contagem = [] 

size_lista = len(lista_positivas)
for linha in repositorio_positivo:
    lista_positivas.append(linha[0])
for linha in repositorio_negativo:
    lista_negativas.append(linha[0])

def encontrar_palavras(palavra_da_vez, size, data2):
    for x in range(size):
        comentario = data2[x].get('text')  
        comentario_convertido = str(comentario)
        result = comentario_convertido.find(palavra_da_vez)
        if result != -1:
            lista_contagem.append(palavra_da_vez)

def contagem(lista_contagem):
    print(len(lista_contagem))

def identificar():
    for identificador in repositorio_nomes:
        nome_app = identificador[1]
        #REQUISIÇÃO USANDO API GOOGLE PLAY PARA RETORNAR INFORMAÇÕES SOBRE O APLICATIVO
        requisicao = requests.get('http://localhost:3000/api/apps/'+str(nome_app)+'/reviews') or requests.get('http://localhost:3000/api/apps/?q='+nome_app+'/reviews')
        data = requisicao.json()
        data2 = data.get('results')
        size = len(data2)
        for i in lista_positivas:
            encontrar_palavras(i, size, data2)
        contagem(lista_contagem)
        del lista_contagem[:]

if __name__ == "__main__":
    identificar()

    


