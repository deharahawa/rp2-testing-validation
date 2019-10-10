import csv
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

test = open('./tested-repo.txt')
tested = csv.DictReader(test)
issues= open('./results.txt')

def cria_tupla(name,x,y,z):
	tupla={"Repositorio": name,"issue": int(x), "star": int(y), "fork": int(z)}	
	return tupla


def organiza_lista(lista,tipo):
	if tipo == 'star':
		return sorted(lista,key = lambda k: k['star'])
	if tipo == 'fork':
		return sorted(lista,key = lambda k: k['fork'])


def plota_graphico(axisx,axisy,tested_axisx2,tested_axisy2,name,color):
	fig,(ax1,ax2) = plt.subplots(1,2,sharex = True)
	fig.suptitle(name)
	

	if color == 'red':
		color = 'ro'
	if color == 'blue':
		color = 'bo'
	#plt.plot(axisx,axisy,'bo',label = name)
	#plt.plot(tested_axisx2,tested_axisy2,'bo',label = name)


	ax1.plot(axisx,axisy,'ro')
	ax2.plot(tested_axisx2,tested_axisy2,'bo')
	#plt.plot(star_axis,issue_axis1,'ro-',label = 'Stars')
	#plt.plot(fork_axis,issue_axis2, 'go-',label = 'Forks')
	plt.ylim(-1,650)
	plt.xlim(-1,4300)
	plt.show()


arqcsv = csv.DictReader(issues)
general_list = [] #lista com todos os repo
tested_list = [] #lista com repositorios com testes
semteste=[] #lista com repositorios sem testes
listaTestada=[]

star_axis=[]
issue_axis1=[]

tested_star_axis=[]
tested_issue_axis=[]

issue_axis2=[]
fork_axis=[]

for repo in tested:
	listaTestada.append(repo)


for nome in arqcsv:
	
	general_list.append(cria_tupla(nome['Repositorio'],nome['open_issues'],nome['stars'],nome['forks']))


for tupla in general_list:	
	testado = 0
	a = object
	for x in listaTestada:
		a=x		
		if x['Repositorio'] == tupla['Repositorio']:
			testado = 1		
			tested_list.append(tupla)
	if testado==0:
		semteste.append(tupla)
	
		
general_list_star = organiza_lista(general_list,'star')
general_list_fork = organiza_lista(general_list,'fork')

tested_list_star = organiza_lista(tested_list,'star')
tested_list_fork = organiza_lista(tested_list,'fork')

for par in tested_list_star:
	issue_axis1.append(par["issue"])
	star_axis.append(par["star"])


for par in semteste:
	print(par)
	tested_issue_axis.append(par["issue"])
	tested_star_axis.append(par["star"])

for par in tested_list_fork:
	issue_axis2.append(par["issue"])
	fork_axis.append(par["fork"])

plota_graphico(star_axis,issue_axis1,tested_star_axis,tested_issue_axis,'stars','red')
#plota_graphico(fork_axis,issue_axis2,'forks','blue')
