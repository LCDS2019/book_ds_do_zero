print('')

########################################################################
print(f'Aritmética -->> '.ljust(80 ,'#'))

ans_real=5/2
ans_inteiro = 5//2

print(f'Divisão no conjunto dos números reais: {ans_real}')
print(f'Divisão no conjunto dos números inteiros: {ans_inteiro}')
print('')

########################################################################
print(f'Funções -->> '.ljust(80 ,'#'))
def teste_de_multiplicar(multiplicador,lista):
    '''
    :param multiplicador: número real utilizado como multiplicador dos valores da lista.
    :param lista: lista de entrada com os valores a serem multiplicados
    :return: lista com valores multiplicados.
    '''
    lista_out=[]
    for i in lista:
        ans=multiplicador*i
        lista_out.append(ans)

    print(f'lista da entrada: {lista}')
    print(f'lista de saída com multiplicador {multiplicador}: {lista_out} \n')
    return lista_out

lista = [1,2,3,4,5,6]
teste_de_multiplicar(5,lista)
teste_de_multiplicar(2.5,lista)

########################################################################
print(f'Funções com valores padrão -->> '.ljust(80 ,'#'))

def padrao(a=1,b=10):
    ans=a+b
    return ans

ans_padrao=padrao()
print(f'Resultado da função com valores padrao: {ans_padrao} \n')

ans_padrao=padrao(5,2)
print(f'Resultado da função com valores padrao: {ans_padrao} \n')

########################################################################
print(f'Funções lambda (funções anônimas) -->> '.ljust(80 ,'#'))
# podemos utilizar lambda como uma função composta

teste_lambda = lambda x : x+4
print(f' {teste_lambda(20)} \n')

precos = [100,120,150,200]
taxa = lambda x:x*0.2

print(f'Exemplo de função lambda como função composta:')
print(f'Lista de preços: {precos}')
print(f'Lista de taxas sobre preços: {list(map(taxa,precos))} \n')

########################################################################
print(f'Função extra - map -->> '.ljust(80 ,'#'))
# função não apresentada no livro
# a função map() fornece uma maneira de aplicar uma função a todos os itens de um iterável

print('Função map + lambda')
numbers = [10, 15, 21, 33, 42, 55]
result = list(map(lambda x: x-5, numbers))

print(f'numbers: {numbers}')
print(f'result: {result}')
print('')

'----------------------------------------------------'

print('Função map + definida')
def func_map(x):
    return x-5

ans = map(func_map,numbers)

ans = list(ans)

print(f'numbers: {numbers}')
print(f'result: {ans}')
print('')

'----------------------------------------------------'
print('Função map + várias listas')

base_numbers = [2, 4, 6, 8, 10, 12, 14, 16]
powers = [1, 2, 3, 4, 5]

numbers_powers = list(map(pow, base_numbers, powers))

print(numbers_powers)
print('')

########################################################################
print(f'Função extra - filter -->> '.ljust(80 ,'#'))
# função não representable no livro

lista =[0,1,2,3,4,5,6,7,8,9,10]

ans=list(filter(lambda x: x>=5,lista))
print(f'Resultado de filtro: {ans}')

print('')
########################################################################
print(f'Função extra - reduce -->> '.ljust(80 ,'#'))
# função não representable no livro

from functools import reduce

def soma_acumuladora(x, y):
    return x + y

numeros = [1, 2, 3, 4, 5]

resultado = reduce(soma_acumuladora, numeros)
print(resultado)

print('')