import random
n1 = input('Digite um nome: ')
n2 = input('Digite outro nome: ')
n3 = input('Digite mais um: ')
lista = [n1,n2,n3]
random.shuffle(lista)
print('A ordem da lista é:')
print(lista)