"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMG e mostre seu status, de acordo com a tabela abaixo:
    * Abaixo de 18.5: Abaixo do Peso
    * Entre 18.5 e 25: Peso ideal
    * 25 até 30: Sobrepeso
    * 30 até 40: Obesidade
    * Acima de 40: Obesidade mórbida
"""
peso = float(input('Digite o peso em Kg: '))
altura = float(input('Digite a altura em metros: '))
imc = (peso / (altura * altura))
if imc < 18.5:
    print(f'Seu IMC é de {imc:.1f} e você está ABAIXO DO PESO.')
elif 18.5 <= imc < 25:
    print(f'Seu IMC é de {imc:.1f} e você está no PESO IDEAL.')
elif 25 <= imc < 30:
    print(f'Seu IMC é de {imc:.1f} e você está com SOBREPESO.')
elif 30 <= imc < 40:
    print(f'Seu IMC é de {imc:.1f} e você está com OBESIDADE.')
else:
    print(f'Seu IMC é de {imc:.1f} e você está com OBESIDADE MÓRBIDA.')
