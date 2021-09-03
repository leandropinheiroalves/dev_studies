# EXERCÍCIO 43
"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMG e mostre seu status, de acordo com a tabela abaixo:
    → Abaixo de 18.5: Abaixo do Peso
    → Entre 18.5 e 25: Peso ideal
    → 25 até 30: Sobrepeso
    → 30 até 40: Obesidade
    → Acima de 40: Obesidade mórbida
"""

# PROGRAMA PRINCIPAL
peso = float(input('Digite o peso em Kg: '))  # Recebe o peso
altura = float(input('Digite a altura em metros: '))  # Recebe a altura
imc = (peso / (altura * altura))  # Calcula o imc
if imc < 18.5:  # SE o imc for menor que 18.5
    print(f'Seu IMC é de {imc:.1f} e você está ABAIXO DO PESO.')  # Imprime abaixo do peso
elif 18.5 <= imc < 25:  # MAIS SE o imc for maior ou igual 18.5 E menor que 25
    print(f'Seu IMC é de {imc:.1f} e você está no PESO IDEAL.')  # Imprime peso ideal
elif 25 <= imc < 30:  # MAIS SE o imc for maior ou igual 25 E menor que 30
    print(f'Seu IMC é de {imc:.1f} e você está com SOBREPESO.')  # Imprime sobrepeso
elif 30 <= imc < 40:  # MAIS SE o imc for maior ou igual 30 E menor que 40
    print(f'Seu IMC é de {imc:.1f} e você está com OBESIDADE.')  # Imprime obesidade
else:  # SENÃO
    print(f'Seu IMC é de {imc:.1f} e você está com OBESIDADE MÓRBIDA.')  # Imprime obesidade mórbida
