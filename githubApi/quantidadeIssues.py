import github
from github import Github #pygithub
import csv




def issues(rep_name,orderID):
    try:
        repo = g.get_repo(rep_name)
        starscount = repo.stargazers_count
        print(orderID," :",rep_name )        
        quantidade_issues = str(repo.open_issues_count)
        quantidade_stars = str(repo.stargazers_count)
        quantidade_forks = str(repo.forks_count)        
        text = rep_name + "," + quantidade_issues + "," + quantidade_stars + "," + quantidade_forks + "\n" 
        file.write(text)     
    except github.GithubException:
    	text = rep_name + ",-1,-1,-1 " + "\n"
    	file.write(text)

        
g = Github("Gustavoyama", "New_horizon1")

arq = open('./list.csv')
linhas = csv.DictReader(arq)
file = open('./results.txt','w')
file.write("Repositorio,open_issues,stars,forks\n")

for linha in linhas:
    issues(linha["repo"],linha["orderId"])
file.close()


