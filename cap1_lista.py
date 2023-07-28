import networkx as nx
import matplotlib.pyplot as plt

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


