import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

############################################################################

print('')
users = [
    {'id': 0,'name': 'Hero'},
    {'id': 1,'name': 'Dunn'},
    {'id': 2,'name': 'Sue'},
    {'id': 3,'name': 'Chi'},
    {'id': 4,'name': 'Thor'},
    {'id': 5,'name': 'Clive'},
    {'id': 6,'name': 'Hicks'},
    {'id': 7,'name': 'Devin'},
    {'id': 8,'name': 'Kate'},
    {'id': 9,'name': 'Klein'}
]

friendships=[
    (0,1),(0,2),(1,2),(1,3),(2,3),(3,4),
    (4,5),(5,6),(5,7),(6,8),(7,8),(8,9)
]

############################################################################

for i in users:
    i['friend']=[]

for i,j in friendships:
    users[i]['friend'].append(j)
    users[j]['friend'].append(i)

for i in users:
    print(i)

############################################################################

def number_of_friends(user):
    ans=len(user['friend'])
    #print(ans)
    return ans

total_connections = sum(number_of_friends(user) for user in users)
num_users = len(users)

avg_connections = total_connections / num_users

print('')
print(f'total_connections = {total_connections}')
print(f'num_users = {num_users}')
print(f'avg_connections = {avg_connections}')
print('')

num_friends_by_id = [(user['id'], number_of_friends(user)) for user in users]

num_friends_by_id = sorted(num_friends_by_id, key=lambda item: item[1], reverse=True)
print(num_friends_by_id)

############################################################################
print('')
print('Criando o sistema de recomendação')
print('')

def foaf(x):
    print(users[x]['name'],f' / id: '+str(users[x]['id']))
    print(20 * '-')
    #print(users[x])
    #print(users[x]['friend'])
    for i in users[x]['friend']:
        print(users[i]['name'],f' / id: '+str(users[i]['id']))
        print(users[i]['friend'])
        print(10 * '-')
        ans = users[i]['friend']
    print('')
    return ans

def not_friends(x):
    lista=[]
    for i in users[x]['friend']:
        for j in users[i]['friend'] :
            if j != x and j not in users[x]['friend']:
                #print(j)
                lista.append(j)
    return lista

def contar_elementos(lista):
    contagem_elementos={}
    for i in lista:
        if i in contagem_elementos:
            contagem_elementos[i]+=1
        else:
            contagem_elementos[i]=1

    contagem_elementos = dict(sorted(contagem_elementos.items(), key=lambda x: x[1], reverse=True))
    print(f'Sugestão de amigos: {contagem_elementos}')
    for i in contagem_elementos:
        print(users[i]['name'])
    print()


for i in range(10):
    print(50 * '#')
    print()
    usuario=i
    foaf(usuario)
    lista= not_friends(usuario)
    contar_elementos(lista)


############################################################################
print('')
print('Criando lista de interesse')
print('')

interests = [
    (0,'Hadoop'),(0,'Big Data'),(0,'HBase'),(0,'Java'),(0,'Spark'),(0,'Storm'),(0,'Cassandra'),(1,'NoSQL'),
    (1,'MongoDB'),(1,'Cassandra'),(1,'HBase'),(1,'Postgre'),(2,'Python'),(2,'scikit-learn'),(2,'scipy'),(2,'Numpy'),
    (2,'statsmodels'),(2,'Pandas'),(3,'R'),(3,'Python'),(3,'statistics'),(3,'regression'),(3,'probability'),
    (4,'machine learning'),(4,'regression'),(4,'decision trees'),(4,'libsvm'),(5,'python'),(5,'R'),(5,'C++'),
    (5,'Haskell'),(5,'programming language'),(6,'statistics'),(6,'probability'),(6,'mathematics'),(6,'theory'),
    (7,'machine learning'),(7,'scikit-learn'),(7,'Mahout'),(7,'neural networks'),(8,'deep learning'),(8,'Big Data'),
    (8,'Artificial Intelligence'),(9,'Hadoop'),(9,'Java'),(9,'Mapreduce'),(9,'Big Data')
]

for i in interests:
    print(i)

def data_scientists_who_like(interest):
    ans = [user_id for user_id, user_interests in interests if user_interests == interest]
    print(interest)
    return ans

print('')
print('Usuários com o mesmo interesse:')
usuarios = data_scientists_who_like('machine learning')
for i in usuarios:
    print(users[i]['name'])

############################################################################

dic_users_interest=defaultdict(list)
for user_id, interest in interests:
    dic_users_interest[interest].append(user_id)
dic_users_interest= dict(sorted(dic_users_interest.items(), key=lambda item: len(item[1]),reverse=True))


dic_interest_users=defaultdict(list)
for user_id, interest in interests:
    dic_interest_users[user_id].append(interest)

print('')
print(40*'#')
print('dic_users_interest:')
for chave, valor in dic_users_interest.items():
    print(f'{chave}: {valor}')

print('')
print(40*'#')
print('dic_interest_users:')
for chave, valor in dic_interest_users.items():
    print(f'{chave}: {valor}')

############################################################################
print('')
print(40*'#')
print('salaries_and_tenure:')

salaries_and_tenures=[
    (83000,8.7),(88000,8.1),
    (48000,0.7),(76000,6.0),
    (69000,6.5),(76000,7.5),
    (60000,2.5),(83000,10),
    (48000,1.9),(63000,4.2)
]

salary_by_tenure=defaultdict(list)
for salary,tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

#for chave, valor in salary_by_tenure.items():
 #   print(f'{valor}: {chave}')

average_salary_by_tenure = {
    tenure: sum(salaries)/len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}

for chave, valor in average_salary_by_tenure.items():
    print(f'{valor}: {chave}')

def tenure_bucket(tenure):
    if tenure < 2:
        return 'Less than two'
    elif tenure < 5:
        return 'Between two and five'
    else:
        return 'More than five'

salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

average_salary_by_bucket = {
    tenure_bucket: sum(salaries)/len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}

############################################################################
print('')
print(40*'#')
print('salaries_by_bucket:')
for chave, valor in average_salary_by_bucket.items():
    print(f'{chave}: {valor}')

############################################################################
print('')
print(40*'#')
print('levantamento de tópicos:')
def contar_palavras(lista):
    contagem={}
    for i in lista:
        if i in contagem:
            contagem[i]+=1
        else:
            contagem[i]=1
    return contagem

lista_de_palavras=[]
for i,j in interests:
    lista_de_palavras.append(j.lower())

#print(lista_de_palavras)
contar_palavras=contar_palavras(lista_de_palavras)
#print(contar_palavras)

palavras = dict(sorted(contar_palavras.items(), key=lambda item: item[1],reverse=True))
for chave, valor in palavras.items():
    print(f'{chave}: {valor}')