
altura = float(input('Digite a sua altura: '))
peso   = float(input('Digite o seu peso: '))
imc = peso / (altura ** 2)
if imc < 16:
    print('Seu IMC é de {:.1f}\nConsiderado Magreza grave'.format(imc))
elif imc >= 16 and imc <= 16.9:
    print('Seu IMC é de {:.1f}\nConsiderado Magreza moderada'.format(imc))
elif imc > 16.9 and imc <= 18.5:
    print('Seu IMC é de {:.1f}\nConsiderado Magreza leve'.format(imc))
elif imc > 18.5 and imc <= 24.9:
    print('Seu IMC é de {:.1f\nConsiderado Peso ideal'.format(imc))
elif imc > 24.9 and imc <= 29.9:
    print('Seu IMC é de {:.1f}\nConsiderado Sobrepeso'.format(imc))
elif imc > 29.9 and imc <= 34.9:
    print('Seu IMC é de {:.1f}\nConsiderado Obesidade grau I'.format(imc))
elif imc > 34.9 and imc <= 39.9:
    print('Seu IMC é de {:.1f}\nConsiderado Obesidade grau II (Severa)'.format(imc))
else:
    print('Seu IMC é de {:.1f}\nConsiderado Obesidade grau III (Mórbido)'.format(imc))