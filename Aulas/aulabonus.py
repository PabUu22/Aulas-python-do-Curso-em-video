# test de cores
print('\33[31;43mOlá, mundo\33[m') # para obter cores sempre ultilize o \33[m e para determinar onde o fundo termina coloque \33[m no locola escolhido
nome = str(input('Digite seu nome: '))
print('Olá, prazer em te conhecer {}{}{}'.format('\33[1;35m', nome, '\33[m'))