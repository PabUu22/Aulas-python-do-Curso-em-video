# Aula de Condições
# if carro.esquerda():
    #Bloco True
#else:
    #Bloco False
nome = str(input('Qual seu nome? ')).strip()
if nome[:5] == 'Pablo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))