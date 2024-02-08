# IMC
nome = str(input('Qual é o seu nome?'))
altura = float(input('Qual é a sua altura?'))
peso = float(input('Qual é o seu peso?'))
imc = peso / altura**2
print(f'{nome}, tem {altura} de altura, pesa {peso} Quilos e seu imc(indice de massa corpórea) é de {imc:.2f}.')

