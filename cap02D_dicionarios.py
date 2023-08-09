print('')

########################################################################
print(f' Dicionários - criação e busca de chaves '.center(80 ,'#'))
print('')

empty_dict = {}
empty_dict2 = dict()
grades={
    'Joel':80,
    'Tim':95
}

print(f'empty_dict: {empty_dict}')
print(f'empty_dict2: {empty_dict2}')
print(f'grades: {grades}')

joels_grade=grades['Joel']
print(f'joel\'s grade: {joels_grade}')

try:
    grades['Kate']
except KeyError:
    print('no grades for Kate')

print('')

########################################################################
print(f' Método in '.center(80 ,'#'))
print('')
joels_grade_in = 'Joel' in grades
print(f'Joel in grades: {joels_grade_in}')

kates_grade_in = 'kate' in grades
print(f'Kate in grades: {kates_grade_in}')

print('')

########################################################################
print(f' Método get '.center(80 ,'#'))
print('')

print('Método get')
joels_grade_get = grades.get('Joel','No grades')
print(f'Joel in grades: {joels_grade_get}')

kates_grade_get = grades.get('Kate','No grades')
print(f'Kate in grades: {kates_grade_get}')

print('')

########################################################################
print(f' Atribuições '.center(80 ,'#'))
print('')

grades['Tim'] = 99
grades['Kate'] = 100
num_alunos = len(grades)
print(f'num_alunos: {num_alunos}')
print(grades)

print('')

########################################################################
print(f' Representação de dados estruturados '.center(80 ,'#'))
print('')

tweet = {
    'user':'joelgrus',
    'text':'Data Science is awesome',
    'retweet_count': 100,
    'hashtags':['#data','#science','#datascience','#awesome','#yolo']
}

print('Dicionário tweet')
print(tweet)

tweet_keys=tweet.keys()
tweet_values=tweet.values()
tweet_items=tweet.items()

print(tweet_keys)
print(tweet_values)
print(tweet_items)

print('')

########################################################################
print(f' Buscas em dicionário '.center(80 ,'#'))
print('')

print('user' in tweet_keys)
print('user' in tweet) #mais rápido que o anterior pois este usa dic in
print('joelgus' in tweet_values)

print('')

########################################################################
print(f' Contar palavras utilizando dicionários '.center(80 ,'#'))
print('')

documento = '''Coordenar equipes em Engenharia de Dados, Business Intelligence e Analytics foi uma experiência gratificante. Nesse papel, desempenhei um papel crucial na gestão de projetos e na promoção de um ambiente colaborativo. Minha expertise abrange as plataformas Qlik, Power BI e GCP, além de habilidades avançadas em Python, R e SQL. Essas habilidades foram essenciais em minha jornada profissional, permitindo contribuições significativas em todos os projetos que assumi.'''

documento = documento.split(' ')
print(documento)

word_counts={}
for word in documento:
    if word in word_counts:
        word_counts[word] +=1
    else:
        word_counts[word] = 1

print(word_counts)

print('')

########################################################################
print(f' Contar palavras - perdão é melhor do que permissão '.center(80 ,'#'))
print('')

documento = '''Coordenar equipes em Engenharia de Dados, Business Intelligence e Analytics foi uma experiência gratificante. Nesse papel, desempenhei um papel crucial na gestão de projetos e na promoção de um ambiente colaborativo. Minha expertise abrange as plataformas Qlik, Power BI e GCP, além de habilidades avançadas em Python, R e SQL. Essas habilidades foram essenciais em minha jornada profissional, permitindo contribuições significativas em todos os projetos que assumi.'''
documento = documento.split(' ')

word_counts_2={}
for word in documento:
    try:
        word_counts_2[word] +=1
    except:
        word_counts_2[word] = 1

print(word_counts_2)
print('')

########################################################################
print(f' Contar palavras - usando get '.center(80 ,'#'))
print('')

documento = '''Coordenar equipes em Engenharia de Dados, Business Intelligence e Analytics foi uma experiência gratificante. Nesse papel, desempenhei um papel crucial na gestão de projetos e na promoção de um ambiente colaborativo. Minha expertise abrange as plataformas Qlik, Power BI e GCP, além de habilidades avançadas em Python, R e SQL. Essas habilidades foram essenciais em minha jornada profissional, permitindo contribuições significativas em todos os projetos que assumi.'''
documento = documento.split(' ')

word_counts_3 = {}
for word in documento:
    previous_count = word_counts_3.get(word,0)
    word_counts_3[word] = previous_count + 1

print(word_counts_3)
print('')

########################################################################
print(f' Contar palavras - defaultdict '.center(80 ,'#'))
print('')

from collections import defaultdict

documento = '''Coordenar equipes em Engenharia de Dados, Business Intelligence e Analytics foi uma experiência gratificante. Nesse papel, desempenhei um papel crucial na gestão de projetos e na promoção de um ambiente colaborativo. Minha expertise abrange as plataformas Qlik, Power BI e GCP, além de habilidades avançadas em Python, R e SQL. Essas habilidades foram essenciais em minha jornada profissional, permitindo contribuições significativas em todos os projetos que assumi.'''
documento = documento.split(' ')

word_counts_4 = defaultdict(int)
for word in documento:
    word_counts_4[word] += 1

print(word_counts_4)

print('')

########################################################################
print(f' Contar palavras - defaultdict '.center(80 ,'#'))
print('')

dd_list = defaultdict(list)
dd_list[2].append(1)
print(dd_list)

dd_dict = defaultdict(dict)
dd_dict['joel']['City'] = 'Seatle'
print(dd_dict)


dd_pair = defaultdict(lambda : [0,0])
dd_pair[2,1] = 1
print(dd_pair)

print('')








