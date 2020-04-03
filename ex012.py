#012 Faça um algoritimo que leia um preço de um produto e monstre seu novo valor com 5% de desconto.
p = float(input(' Digite o preço do produto: '))
d = p*0.05
v = p-d
print('O valor do desconto é R$: {:.2f}\nValor a pagar: R$: {:.2f}'.format(d, v))