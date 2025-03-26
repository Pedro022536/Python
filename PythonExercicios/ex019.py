import random
n1 = input('Digite o nome do Primeiro aluno: ')
n2 = input('Digite o nome do Segundo aluno: ')
n3 = input('Digite o nome do Terceiro aluno: ')
lista = [n1,n2,n3]
escolhido = random.choice(lista)
print(f'O nome sorteado escolhido foi: {escolhido}')