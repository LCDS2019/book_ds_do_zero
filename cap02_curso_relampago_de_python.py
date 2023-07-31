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