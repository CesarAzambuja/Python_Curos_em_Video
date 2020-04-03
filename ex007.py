#007 Desenvolva um programa que leia as duas notas do um aluno, e calculo e mostre sua média

nome = input('Digite o nome do aluno: ')
n1 = float(input('Digita a nota da primeira prova: '))
n2 = float(input('Digite a nota da segunda prova: '))
m = (n1+n2)/2
print ('A media do aluno {} é: {}'.format (nome, m))