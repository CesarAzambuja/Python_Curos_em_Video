#008 Escreva um programa que leia um valor em metros e o exiba em centimetros e milimetros

n1 = float(input('Digite o Valor em Metros:'))
n2 = n1*100
n3 = n1*1000
print('O Valor em Centrimetros é: {}cm\n O valor em Milimetros é: {}mm'.format(n2, n3))