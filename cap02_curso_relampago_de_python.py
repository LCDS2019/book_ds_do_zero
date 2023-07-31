print('')

########################################################################
print(f'Aritmética -->> '.ljust(50 ,'#'))

ans_real=5/2
ans_inteiro = 5//2

print(f'Divisão no conjunto dos números reais: {ans_real}')
print(f'Divisão no conjunto dos números inteiros: {ans_inteiro}')
print('')

########################################################################
print(f'Funções -->> '.ljust(50 ,'#'))
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