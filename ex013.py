#013 Faça um algoritimo que leia o salario de um funcionario e mostre seu novo salarío com 15% de aumento.
s = float(input('Qual o salario atual do colaborador: '))
a = int (input('De quantos procento era o reajuste: '))
ns = s+s*(a/100)
print('O nova salario do colaborador após o reajuste será: R$: {:.2f}'.format(ns))