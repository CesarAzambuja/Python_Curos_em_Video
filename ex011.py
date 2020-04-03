#011 Faça um programa que leia a altura e largura de uma parede em metros e calculo a sua area e a quantidade de tenta necessaria para pinta~la, sabendo que cada litro de tinta pinta uma area de 2m²
l = float(input('Digita a largura da parede: '))
a = float(input('Digite a altura da parede: '))
area = l*a
qnt = area/2
print('Sua parede tem uma area total de {}m² e serão necessarios {} Litros de tinta para pintala'.format(area, qnt))