print('')

########################################################################
print(f'Strings -->> '.ljust(80 ,'#'))

texto = 'Exemplo de string com aspas simples'
print(texto)

print('')
texto2 = r'\\' #exemplo de texto bruto com a função 'r'
print(f'Exemplo da aplicação da função r para textos brutos: {texto2})')

print('')
print(f'Exemplo de textos em múltiplsa linhas:')
multilinestring='''
           linha um 
           linha dois
           linha três '''
print(multilinestring)

########################################################################
print(f'Exceções -->> '.ljust(80 ,'#'))

lista = range(0,10,2)

for i in lista:
    print(i)
    try:
        print(i/0)
    except:
        print('Error by division!!')


