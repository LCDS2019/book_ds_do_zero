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

########################################################################
print(f' Buscas em dicionário '.center(80 ,'#'))
print('')

print('user' in tweet_keys)
print('user' in tweet) #mais rápido que o anterior pois este usa dic in
print('joelgus' in tweet_values)
