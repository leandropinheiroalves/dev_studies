"""Faça um programa que leia e valide as seguintes informações:
    * Nome: maior que 3 caracteres;
    * Idade: entre 0 e 150;
    * Salário: maior que zero;
    * Sexo: 'f' ou 'm';
    * Estado Civil: 's', 'c', 'v', 'd';
"""

nome = str(input('Digite seu nome: ')).upper()
while len(nome) < 3:
    print('ERRO! O nome informado precisa ter mais do que 3 caracteres.')
    nome = str(input('Digite o nome novamente: ')).upper()

idade = int(input('Digite sua idade: '))
while idade < 0 or idade > 150:
    print('ERRO! A idade informado precisa estar entre 0 e 150 anos.')
    idade = int(input('Digite a idade novamente: '))

salario = int(input('Digite seu salario: '))
while salario < 0:
    print('ERRO! O salário informado precisa ser maior que 0.')
    salario = int(input('Digite o salario novamente: '))

sexo = str(input('Digite seu sexo: ')).upper()
while sexo[0] not in 'MF':
    print('ERRO! O sexo informado precisa ser M-Masculino ou F-Feminino.')
    sexo = str(input('Digite o sexo novamente: ')).upper()

estado_civil = str(input('Digite seu estado civil: ')).upper()
while estado_civil[0] not in 'SCVD':
    print('ERRO! O estado civil informado precisa ser S-Solteiro(a), C-Casado(a), V-Viúvo(a) ou D-Divorciado(a)')
    estado_civil = str(input('Digite o estado civil novamente: ')).upper()

if sexo == 'M':
    sexo = 'Masculino'
else:
    sexo = 'Feminino'

if estado_civil == 'S':
    estado_civil = 'Solteiro'
elif estado_civil == 'C':
    estado_civil = 'Casado'
elif estado_civil == 'V':
    estado_civil = 'Viúvo'
else:
    estado_civil = 'Divorciado'

print()
print(f'''Nome: {nome}
Idade: {idade} anos
Salario: R$ {salario} 
Sexo: {sexo}
Estado Civil: {estado_civil}
''')
