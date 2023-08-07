print('')

########################################################################
print(f' Listas -->> '.center(80 ,'#'))
print('')
########################################################################
print(f'Listas -->> '.ljust(80 ,'#'))
print('')

integer_list = [1,2,3]
heterogeneous_list = ['string', 0.1, True]
list_of_list = [integer_list, heterogeneous_list, []]

list_length_integer_list = len(integer_list)
list_sum_integer_list = sum(integer_list)

print('Exemplos:')
print(f'integer_list: {integer_list}')
print(f'heterogeneous_list: {heterogeneous_list}')
print(f'list_of_list: {list_of_list}')
print(f'list_length_integer_list: {list_length_integer_list}')
print(f'list_sum_integer_list: {list_length_integer_list}')
print('')

x = []
for i in range(10):
    x.append(i)
print(f'x: {x}')
print('')

'-----------------------------------------------------------------------'
print('Slices')
first_three = x[:3]
three_to_end = x[3:]
one_to_four = x[1:5] # a indexação não considera o último valor
last_three = x[-3:]
without_first_and_last = x[1:-1]

print(f'first_three: {first_three}')
print(f'three_to_end: {three_to_end}')
print(f'one_to_four: {one_to_four}')
print(f'last_three: {last_three}')
print(f'without_first_and_last: {without_first_and_last}')
print('')

'-----------------------------------------------------------------------'
print('Verificar se está contido - operador in')
print(f'1 in [1,2,3]: {1 in [1,2,3]}')
print(f'0 in [1,2,3]: {0 in [1,2,3]}')
print('')

'-----------------------------------------------------------------------'
print('Concatenar listas')
x=[1,2,3]
print(f'lista x: {x}')
x.extend([4,5,6])
print(f'lista x extendida: {x}')
print('')

y=x+[0,8,9]
print(f'lista y : x extendida por [0,8,9]: {y}')

print('Append de elementos no final da lista ')
x=[1,2,3]
print(f'x: {x}')
x.append(0)
print(f'x: {x}')
print('')

'-----------------------------------------------------------------------'
print('Extração de elementos de uma lista')
x=[1,2,3]
print(f'x: {x}')
x,y,z=x
print(f'x:{x} y:{y} z:{z}')
print('')

'-----------------------------------------------------------------------'
print('Extração de elementos com underscore')
x=[1,2,3]
print(f'x: {x}')
x,_,z=x
y=0
print(f'x:{x} y:{y} z:{z}')

print('')
'-----------------------------------------------------------------------'
print('Listas e tuplas')

my_list = [1,2]
my_tuple = (1,2)
other_tuple = 3,4
my_list[1] = 3

print(f'my_tuple: {my_tuple}')
try:
    my_tuple[1]=3
except TypeError:
    print('cannot modify a tuple')

print('')
'-----------------------------------------------------------------------'

def sum_and_product(x,y):
    return (x+y),(x*y)

sp=sum_and_product(2,3)
s,p=sum_and_product(5,10)

print(f'sp:{sp}')
print(f's:{s}')
print(f'p:{p}')

print('')
print('Inversão de valores:')
x,y=1,2
print(x,y)

x,y=y,x
print(x,y)
