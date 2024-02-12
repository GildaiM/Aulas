import random
n1 = int(input('Entre 1 e 10 digite um número e tente adivinhar o número escolhido pela Máquina. \n'))
numero = (random.randint(1,10))
if numero == n1:
    print('Párabens, Você acertou o número sorteado!')
else:
    print(f'Não foi dessa vez, o número sorteado foi {numero}')
