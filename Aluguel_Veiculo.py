
#Considerando que o valor da diária seja R$100, e o valor do KM percorrido seja R$0.50 por KM

dias = int(input('Escreva a quantidade de dias em que ficou com o veículo: '))
km = float(input('Escreva a quantidade de km em que o veículo percorreu: '))
valor = (100 * dias + km * 0.50)
print('O Veículo foi alugado por {} dias e percorreu {}km\nO Valor a pagar: R${:.2f}'.format(dias, km, valor))