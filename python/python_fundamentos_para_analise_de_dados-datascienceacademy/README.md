# **Python Fundamentos Para Análise de Dados 3.0**

## **[Módulo 01] - Introdução**

### **Por Que Todos Deveriam Aprender a Programa?**
* Programação é o futuro, ele está em tudo, e se não está um dia estará.
* Os programadores são os novos "Rockstars"

### **Por Que Cientistas de Dados Escolhem Python?**
* Ao trabalhar com data science, é necessário uma ferramenta que possa:
   * Coletar os Dados
   * Limpar os Dados
   * Transformar os Dados
   * Fazer Pré Procesamento
   * Criar o Modelo Preditivo
   * Avaliar o Modelo Preditivo 
   * Construir Gráficos e Dashboards

* → Python, pode ser utilizado para todas  essas tarefas!

* Atualmente são utilizadas 4 linguagens amplamente em ciência de dados
   * Python
   * R
   * Scala
   * Java
* Diferencial do Python
    * Muito mais facil de aprender
    * Linguagem de facil utilização
    * Tempo de desenvolvimento mais rapido que as demais
    * Linguagem comum que também é utlizada em outras áreas, sendo mais fácil encontrar alguem que saiba Python na sua empresa
    * Python possui uma grande comunidade que está sempre disposta a ajudar
    * Python possui várias Bibliotecas de Análise de Dados
    * Jupyter Notebook, que permite codar do seu navegador
    * Python tem uma grande facilidade de aprender, pois a linguagem é mais simples e intuítiva
    * Escalabilidade e Portabilidade

### **Programas utilizados durante o curso**
* [Anaconda](https://www.anaconda.com)
* IDE's Python (Ambiente Integrado de Desenvolvimento)
   * Jupyter Notebook (Já vem instalado com o Anaconda)
   * [PyCharm](https://www.jetbrains.com/pycharm/download/)
    * Versão Community - Versão grátis, será usado no curso essa versão
    * Versão Professional - Versão paga, com funcionalidades adicionais 

### **Arquivos usados durante o curso**
*  Todos os arquivos estão disponíveis no [github da Data Science Academy](https://github.com/dsacademybr/PythonFundamentos)

### **Utliziando Jupyter Notebook**
Por padrão o Jupyter Notebook já vem instalado com o anaconda, caso não esteja usando o anaconda, será necessário baixar o Jypyter Notebook
* Ao utilizar o JN, o recomendado é sempre abri-lo pelo prompt de comando, porque assim ele irá abrir na pasta exata onde você gostaria de trabalhar, do contrário ele irá abrir em uma pasta padrão, fazendo com que fique mais dificil navegar para o seu diretório de trabalho
   * No meu caso o caminho os passos são:
      * Abrir cmd
      * Navegar até a pasta usando o comando cd
         * O comando cd faz com que entremos em uma pasta
      * ..\Documents\MeuPc\PythonFundamentos\(nome do módulo do curso)>jupyter notebook
         * Depois disso o JS irá abrir no seu navegador padrão
            * Caso você queira usar um navegador que não seja o padrão, será pedido um token, depois de inserido é só utilizar o navegador
               * O token estará no prompt de comando

### **Rodando Scripts Python no cmd**
Primeiramente é bom saber alguns comandos basicos do cmd:
* cd (nomedapasta): entra em uma pasta
* dir: lista os arquivos existentes na pasta atual
* cls: limpa o prompt de comando
* python (nomedoarquivo.py): se o python estiver instalado, executa o arquivo.py utilizando o interpretador do python
* python: caso não seja colocado nenhum arquivo, o interpretador do python será carregado e você poderá utiliza-lo pelo próprio prompt de comando
    * exit(): sai do interpretador
## **[Módulo 02] - Variáveis, Tipos e Estruturas**

### Fundamentos
Python é uma linguagem interpretada, clara, de fácil leitura e bastante expressiva. Basicamente, existem 3 modos de executar programas em Python:
* Modo shell
* Modo script (aruivos com extensão .py)
* Modo interativo (Jupyter Notebook)

A Indentação é muito importante em python. Para a indentação é utilizado o 1 Tab ou 4 espaços.

ex:
```
print(nivel 1)  # primeiro nível hierárquico

if(True):
    print(nível 2)  # segundo nível hierárquico
```
### Comentários em Python
Começam com o caracter # ou """..."""

\# Comentário em uma única lina

"""
Comentário em mais 

de uma linha
"""

### Dicas
* Clareza é importante. Mantenha seu código limpo e organizado
* Código esparso é melhor que código denso
* Sempre documente seu código
* Siga os padrões não para criar complexidade, mas para manter a regra.
* Erros nunca serão silenciosos, a menos que propositalmente.
* Simples é melhor que complexo e complexo é melhor que complicado.
* Não se sinta obrigado a criar classes sem  uma boa razão.

### Números e Operações Matemáticas
Python possui 2 tipos de números principais:
* int → números inteiros, positivos ou negativos. Ex: -7 e 7
* float → números fracionários, positivos ou negativos. Ex: -7.1 e 7.1

Podemos usar a função `type()`, para saber qual é o tipo de um número.

Podemos usar as funções `int()` e `float()` para converter números.

### Funções Built-in
O python possui várias funções integradas e ainda possibilita você criar as suas próprias funções, para saber as funções built-in nativas do python [clique aqui](https://docs.python.org/3/library/index.html)

### Operações com Números

Operador|Significado|Exemplo
---|---|---
+|Soma|2 + 2 → 4
-|Subtração|3 - 2 → 1
*|Multiplicação|2 * 3 → 6
/|Divisão|10 / 2 → 5
%|Módulo|5 % 2 → 1
**|Potência|4 ** 2 → 16
int()|Converte para inteiro|int(3.2) → 3
float()|Converte para float|float(2) → 2.0

### Operações Relacionais

Operador|Significado
--|--
==|Igualdade / Equivalência
!=|Desigualdade / Inequivalência
\>|Maior que
<|Menor que
\>=|Maior que ou igual a
<=|Menor que ou igual a

### Variáveis e Operadores
As variáveis são usadas em nosso código Python para armazenar valores que  queresmo usar mais tarde.

São espaços em memória que armazenam valores

Por exemplo, nós podemos armazenar  o  valor 10 na variável b.

b = 10

O sinal de igual atribui o valor á direita (10) à variável do lado esquerdo (b). Você pode sobrescrever uma variável com um novo valor sempre que quiser. A variável  assumirá o novo valor.

A função `print()` em Python irá imprimir valores na tela (teremos um módulo inteiro sobre funções). Por exemplo:

`print(10)` → imprime na tela o valor 10

`print(b)` → imprime na tela o valor da variável b

Tudo que é impresso aparece  na tela de saída do Python.

### Regras a ser seguidas para criação de variáveis
1. Não podem começar com número.
2. Não pode haver espaços; utilize _ no lugar do espaço
3. Não é possível usar qualquer um desses  símbolos: ' " , < > / | \ ( ) @ # $ % ^ & * ~ - + !
4. Não se pode usar palavras reservadas

O item 3 é considerado uma boa prática de programação (PEP8). Visite os istes abaixo para mais informações:

https://www.python.org/dev

https://docs.python.org/devguide

### Operadores

### Operadores de Atribuição

Operador|Significado|Exemplo
---|---|---
=|Atribuiçãoz = 10
+=|Soma|z += 10 (equivalente a z = z + 10)
-=|Subtração|z -= 10 (equivalente a z = z - 10)
*=|Multiplicação|z *= 10 (equivalente a z = z * 10)
/=|Divisão|z /= 10 (equivalente a z = z / 10)
%=|Módulo|z %= 10 (equivalente a z = z % 10)
\**=|Potência|z \*\*= 10 (equivalente a z = z \*\* 10)
//=|Divisão inteira|z //= 10 (equivalente a z = z // 10)

### Operadores Lógicos

Operador|Significado|Exemplo
---|---|---
and|Se ambos operadores forem True, retorna True|(x and y) é True
or|Se um dos operadores for True, retorna True|(x or y) é True
not|Usado para reverter o estado da lógica|not(x and y) é False

### Strings
Strings são usadas em Python para gravar informações em formato de texto, como nomes por exemplo. Strings em Python são na verdade uma sequência de caracteres, o que significa, basicamente, que Python mantém o controle de cada elemento da sequência.

Python entende a string "Olá", como sendo  uma  sequência de letras  em uma ordem específica. Isso  significa que você será capaz de usar a indexação  para  obter um caracter específico (como a primeira letra ou a última letra).

String - sequência imutável de caracteres ou apenas  1 caracter
* "Essa é uma string"
* "a"

### <u>Indexando Strings</u>
Como Strings são sequências, o Python pode  usar índeces para chamar partes da sequência. Vamos aprender como isso funciona.

Em Python, usamos **colchetes []** para representar o índice  de um  objeto.

**→ Em Python, a indexação começa por 0.**

Por exemplo, podemos criar a string:

```
texto = 'Python e Análise de Dados'

texto[0] = P
texto[1] = y
texto[2] = t
```

É importante ressaltar que as strings têm uma importante propriedade conhecida como imutabilidade. Isto significa  que uma  vez que é criada uma string, os elementos dentro dela não podem ser substituídos ou alterados.

### Funções Built-in de Strings
Python é uma linguagem orientada a objeto, sendo assim  as  estruturas  de dados possum atributos (propriedades) e métodos (rotinas associadas às propriedades). Tanto os atributos quanto os métodos são acessados usando ponto (.).

Os métodos estão sob a forma:

``` 
objeto.atributo
objeto.método()
objeto.método(parâmetros)
```

Parâmetros são argumentos extras, que podemos passar para o método. Não se preocupe se os detalhes não fazem sentido 100% agora. Mais tarde, estaremos criando nossos próprios métodos.

### Estruturas de Dados

### <u>Listas</u>

Anteriormente, quando discutimos Strings, introduzimos o conceito de uma sequência em Python. As listas podem ser consideradas a versão geral de uma sequência em Python. Ao contrário de Strings, as listas são mutáveis, ou seja, os elementos  dentro de uma lista podem ser alterados.

As listas são contruídas com o uso de colchetes `[]` e vírgulas separando cada elemento da lista

```
lista = [item1, item2, ..., itemz]
```

Se você estiver familiarizado com outra linguagem de programação, você pode traçar paralelos entre matrizes em outras linguagens e listas em Python. Listtas em Python no entanto, tendem a ser mais felxíveis do que as matrizes em outras linguagens  por dois bons motivos:
   1. Listas não têm tamanho fixo (o que significa que não precisamos especificar quão grande uma lista será) 
   2. Listas não têm restrições de tipo fixo

Uma grande característica de estrutura de dados em Python é que elas suportam aninhamento. Isto significa que podemos usar estruturas de dados dentro de estruturas de dados.

### <u>Dicionários</u>

Até aqui falamos bastante sobre sequências em Python, mas agora vamos mudar um  pouco o foco e aprender sobre mapeamentos em Python. Se  você estiver familiarizado com outras linguagens de programação, pode imaginar os dicionários como tabelas de hash (hash tables).

Os dicionários são construídos com o uso de chaves `{}` e vírgulas separando cada elemento do dicionário.

`dict = {k1:v1, k2:v2, ..., kn:vn}`

Então, o que são mapeamentos?

Mapeamentos são uma coleção de objetos que são armazenados por uma chave, ao contrário de uma sequência de objetos armazenados por sua posição relativa.

Esse valor pode ser quase qualquer objeto Python.

Dicionários - mapeamento de chaves e valores

`{chave1: valor1, chave2: valor2}`

### <u>Tuplas</u>

Em Python, tuplas são muito semelhantes ás listas, no entanto, ao contrário de  listas, tuplas são imutáveis, o que significa  que não podem ser alteradas. Você usaria tuplas para apresentar dados que não devem  ser alterados, como os  dias da  semana  ou datas em um calendário.

As tuplas são construídas com o uso de parênteses `()` e vírgulas separando cada elemento da tupla.

`tupla = (item1, item2, ..., itemz)`

**"Por que se preocupar usando tuplas, uma vez que trata-se de um objeto com limitações e um número menor de métodos disponíveis?"**

Tuplas não são utilizadas com frequência, como listas por exemplo, mas são usadas  quando é necessário imutabilidade. Se em seu programa você precisa ter certeza de que os dados não sofrerão mudança, então tupla pode ser a sua solução. Ela fornece uma fonte conveniente de integridade de dados.

### **Resumo até aqui**

Tipo de Objeto|Categoria|Mutável?
---|---|---
Números|Numérico|Não
String|Sequência|Não
Listas|Sequência|Sim
Dicionários|Mapeamento|Sim
Tuplas|Sequência|Não


Operadores de Aritméticos
Operador|Significado|Exemplo
---|---|---
+|Soma|2 + 2 → 4
-|Subtração|3 - 2 → 1
*|Multiplicação|2 * 3 → 6
/|Divisão|10 / 2 → 5
%|Módulo|5 % 2 → 1
**|Potência|4 ** 2 → 16
int()|Converte para inteiro|int(3.2) → 3
float()|Converte para float|float(2) → 2.0


Operadores Relacionais
Operador|Significado
--|--
==|Igualdade / Equivalência
!=|Desigualdade / Inequivalência
\>|Maior que
<|Menor que
\>=|Maior que ou igual a
<=|Menor que ou igual a


Operadores de Atribuição
Operador|Significado|Exemplo
---|---|---
=|Atribuiçãoz = 10
+=|Soma|z += 10 (equivalente a z = z + 10)
-=|Subtração|z -= 10 (equivalente a z = z - 10)
*=|Multiplicação|z *= 10 (equivalente a z = z * 10)
/=|Divisão|z /= 10 (equivalente a z = z / 10)
%=|Módulo|z %= 10 (equivalente a z = z % 10)
\**=|Potência|z \*\*= 10 (equivalente a z = z \*\* 10)
//=|Divisão inteira|z //= 10 (equivalente a z = z // 10)


Operadores Lógicos
Operador|Significado|Exemplo
---|---|---
and|Se ambos operadores forem True, retorna True|(x and y) é True
or|Se um dos operadores for True, retorna True|(x or y) é True
not|Usado para reverter o estado da lógica|not(x and y) é False

Você vai perceber, que o conhecimento adquirido neste capítulo, será utilizado em todos os demais capítulos e quando trabalharmos com Análise de Dados.

Agora, faça os exercícios, compare suas respostas com o gabarito fornecido, faça o quiz, acesse a seção de referência e links úteis com material complementar e encontre comigo no Laboratório01, quando vamos trabalhar com um game Python.
## **[Módulo 03] - Loops, Condicionais, Métodos e Funções** 

### Resumo do que será visto no módulo
* Condicionais if/else/elif
* Estruturas de Repetição
* Métodos
* Funções
* Outras Operações

### Condicionais

O condicional **if** nos permite dizer ao computador para executar ações com base em um determinado conjunto de resultados.

Verbalmente, podemos imaginar que estamos dizendo ao computador:

"Ei, caso isso aconteça, execute esta ação."

```
if (expressão 1):
   print('comando executado caso a expressão 1 seja Verdadeira')
else:
   print('comando executado caso a expressão 1 seja Falsa')
```

O elif substitui a necessidade de criar várias estruturas de if...else aninhadas.

```
if (expressão 1):
   print('comando executado caso a expressão 1 seja Verdadeira')
elif (expressão 2):
   print('comando executado caso a expressão 1 seja Falsa e expressão 2 seja Verdadeira')
else:
   print('comando executado caso a expressão 1 e 2 sejam Falsas')
```

### Indentação

É importante ter um boa compreensão de como funciona o recuo em Python (indentação) para manter a estrutura em ordem no seu código.

### Estruturas de Repetição

1. Loop For

For, valida cada item em uma séride de valores

```
for item in série-de-items:
   Executar comandos
```

2. Loop While

O loop while em Python é uma das formas mais comuns para executar iteração.

A instrução while será executada repetidamente, seja uma única instrução ou grupo de instruções, desde que uma condição seja verdadeira.

Valida cada item em uma série de valores

```
while (expressão1):
   print('comando executado caso a expressão1 seja Verdadeira')
```

3. Range

A função `range()` nos permite criar uma lista de números em um intervalo específico.

A função `range()` tem o seguinte formato:

`range([start],[stop],[step])`

* [start] - número que inicia a sequência
* [stop] - número que encerra a sequência (não é incluído na sequência)
* [step] - diferença entre cada número da sequência

### Métodos

Nós já vimos alguns exemplos de métodos quando aprendemos sobre Estruturas de Dados em Python.

Os métodos são essencialmente funções  incorporadas em objetos.

Mais tarde, vamos aprender sobre como criar nossos próprios métodos que utilizam Programação Orientada a Objetos (OOP) e classes.

Métodos  permitem executar ações específicas no objeto e podem também ter argumentos, exatamente como uma função.

Os métodos são executados sob a forma:

`objeto.método(arg1, arg2, etc...)`

Com o Jupyter Notebook podemos ver rapidamentes todos os métodos possíveis para um objeto, usando a tecla TAB. Por exemplo, os métodos para o objeto lista são
* append
* count
* extend
* insert
* pop
* remove
* reverse
* sort

### Funções

Vamos agora estudar o que é uma função em Python. As Funções serão um dos nossos principais recursos, quando construírmos quantidades cada vez maiores de código para resolver problemas.

**Então o que é uma função?**

Função é um dispositivo que agrupa um conjunto de instruções para que elas possam ser executadas mais de uma vez. Funções também permitem especificar os parâmetros que podem servir como entrada para as funções.

Em um nível mais fundamental, a construção de funções nos permite reutilizar código, sem ter que escrevê-lo novamente. Nas aulas de Strings, utilizamos a função len() para obter o comprimento de uma String. Com funções, escrevemos os código uma única vez e repetimos a mesma instrução, fazendo a chamada á função, quantas vezes forem necessárias.

O formato geral de uma função é:

```
def nomedafunção(arg1,  arg2):
"""
Aqui vão os comentários, documentando sua função.
"""
   <Aqui vai seu código>
   <Retorno desejado pela função>
```

**E por que Função é importante?**

Funções em Python são uma forma de escrever a sua lógica em um único pacote e utilizá-la em diferentes lugares no seu código e quantas vezes quiser.

### Expressões Lambda

Uma das características mais úteis em Python (e para iniciantes, um pouco confuso) é a expressão lambda. Expressões lambda nos permitem criar funções 'anônimas'. Isto significa  que podemos fazer rapidamente funções ad-hoc sem  a necessidade de definir uma função usando a palavra reservada **def**.

Objetos de função desenvolvidos executando expressões lambda funcionam exatamente da mesma forma como  aqueles criados e atribuídos pela palavra reservada def. Mas há algumas diferenças fundamentais que fazem lambda útil em funções especializada:

* O corpo do lambda é uma única expressão, não um bloco de instruções
* O corpo do lambda é semelhante a uma instrução de retorno do corpo def.

Expressões lambda realmente são úteis, quando usadas em conjunto com as funções `map()`, `filter()` e `reduce()`.

Expressões lambda são usadas para  criar funções simples.

São também chamadas funções in-line ou apenas funções anônimas.

`lambda x: x**2`

**Diferença entre def e lambda para criar funções:**

* def → cria um objeto e atribui um nome a ele (nome da função)
* lambda → cria um objeto, mas o retorna como um resultado em tempo de execução
## **[Módulo 04] - Tratamento de Arquivos, Módulos, Pacotes e Funções Built-in

### O que estudaremos neste capítulo?
* Manipulação de Arquivos em Python
* Módulos e Pacotes
* Pypi e Instalação de Pacotes
* Pacotes Math e Datetime
* Funções Built-in Map, Reduce, Filter, Zip e Enumerate
* List Cromprehension
* Erros e Exceções

### Arquivo

Sempre ao utilizar arquivos, será necessário abri-lo, no entanto, se abri-lo para leitura(read), não será possível utilizar métodos de escrita(write) e vice-versa.

```
#  Abrindo  arquivo para leitura
a = open('caminhodoarquivo.txt', 'r')

# Lendo o arquivo
print(a.read())

# Contar o número de  caracteres
print(a.tell())

# Retornar para o início do arquivo
print(a.seek(0,0))

# Ler  os primeiros 10 caracteres
print(a.read(10))
```

```
# Abrindo arquivo para gravação
a2 = open('caminhodoarquivo.txt', 'w')

# Gravando  arquivo
a2.write('Mensagem que será colocada no  arquivo, apagando o que já estiver no arquivo')

# Fechando o arquivo para que  ele possa ser aberto em modo leitura e ser lido
a2.close()

# Acrescentando conteúdo
a2 = open('caminhodoarquivo.txt', 'a')
a.write('mensagem a ser adicionada no  arquivo')
```

### Módulos e Pacotes

Se você sair do interpretador Python  e entrar novamente, todas as definições que você fez (funções  e variáveis) são perdidas.

Portanto, se você quiser escrever um programa  um pouco mais longo, você precisa usar um editor de texto ou uma IDE para escrever seu código, salver e então executar o arquivo no interpretador Python.

Isso é conhecido  como a criação  de  um script.

À medida que seu programa fica maior, você pode querer dividi-lo em vários módulos para facilitar  a manutenção.

Você também pode querer usar uma função que você escreveu, em vários programas sem ter que copiar sua  definição em cada programa.

Para suportar isso, Python tem uma maneira de colocar tais definições em um arquivo e usá-las em um script ou em uma instância interativa do interpretador (como no Jupyter Notebook).

Esse arquivo é chamado de módulo

Módulos em Python são simplesmete arquivos Pythom com a extensão **.py**, que implementam um conjunto de funções.

Importamos o módulo em  nosso  script Python, usando o comando import:

`import math`

A primeira vez que um módulo é carregado em um script Python, ele é inicializado e fica disponível para uso.

Você precisa importar um módulo apenas uma vez no seu código.

Escrever módulos Python é muito simples. Para criar um módulo de sua preferência, basta criar um novo arquivo .py com o nome do módulo e, em seguida, importa-lo usando o nome do arquivo Python (se a extensão .py), utilizando o comando de importação.

`meu_modulo.py`

`import 'meu_modulo'`

Também é possível importar funções específicas de um módulo

`from math import sqrt`

O Anaconda traz na instalação uma série de módulos disponíveis, principalmente módulos para computação científica e Data Science.

Para verificar os módulos e pacotes instalados, use o comando:

`conda list`

Mas você pode instalar qualquer módulo que desejar e que seja compatível com a sua versão da linguagem Python!

Para isso, abra o prompt de comando no seu computador e use o comando:

`conda intall "nome-do-modulo"`

ou

`pip install "nome-do-modulo`

Por exemplo, se você quiser instalar um módulo para criar arquivos do Microsoft PowerPoint a partir do Python.

http://python-pptx.readthedocs.io/en/latest

`pip instal python-pptx`

Existem diversos módulos do Python criados por desenvolvedores e empresas ao redor do mundo.

### Pacotes

Pacotes são uma forma de estruturar os módulos Python.

`import modulo`
`import pacote.modulo`

Um pacote é um conjunto de módulos Python.

Enquanto um módulo é um único arquivo Python, um pacote é um diretório de módulos Python contendo um arquivo \__init__.py

`import pacote.modulo`

O repositório de pacotes do  Pythn, é o Pypi (Python Package Index) com mais  de 130 mill pacotes disponíveis.

https://pypi.python.org/pypi

### Função Map

Python fornece várias funções que permitem uma abordagem funcional à programação, oferecendo mais  facilidade na criação do seu código.

Podemos dizer que a programação funcional é uma  programação orientada à expressão.

Funções orientadas à expressão, em Python:
* map(Função, Sequência)
* reduce(Função, Sequência)
* filter(Função, Sequência)
* lambda
* list comprehension

```
lista = [1, 2, 3, 4, 5]
quadrados = []

for x in lista:
   quadrados.append(x ** 2)

quadrados
[1, 4, 9, 16, 25]
```

Como esta pode ser uma operação comum, Python nos fornece uma função interna (build-in) que faz a maior parte do trabalho por nós.

Map é uma função que recebe 2 argumentos:
* Uma função
* Uma sequência

`map(função, sequência)`

O primeiro argumento é o nome de uma função e o segundo uma sequência (por exemplo, uma lista).

`map(função, sequência)`

`map()` aplica a função a todos os elementos da sequência.

Uma nova lista com os elementos alterados pela função é retornado.

### Função Reduce

Reduce é uma função que recebe 2 argumentos (assim como a função map):
* Uma função
* Uma sequência

`reduce(função, sequência)`

O primeiro argumento é o nome de uma função e o segundo uma sequência (por exemplo, uma lista).

Ao contrário da função map que aplica a função a cada elemento da sequência e retorna uma outra sequência de elementos, a função reduce aplica a função passada como parâmetro aos elementos da sequência, até que reste apenas um elemento.

### Função Filter

A exemplo das funções built-in. `map()` e `reduce()`, a função `filter()` também recebe 2 argumentos, uma função e uma sequência.

`filter(função, sequência)`

A função passada como parâmetro para `filter()`, deve retornar um valor booleano, True ou False.

A função será aplicada a todos os valores de uma sequência e os valores serão retornados, apenas se retornarem True para a função.

### List Cromprehension

Como vimos nos itens anteriores, podemos usar as funções `map()`, `reduce()` e `filter()`, para aplicar uma determinada função a uma sequência de dados.

Mas como está é uma atividade comum em Python, a linguagem fornece alternativas ainda mais flexíveis que `map()` e `filter()`.

List Comprehension, aplica uma expressão arbitrária (ao invés de aplicar apenas uma função) a uma sequência de elementos.

List Comprehension, permite desenvolver listas usando uma notação diferente. Seria essencialmente uma linha de loop for, contruída dentro de `[]`.

Por exemplo:

`lst = [x for x in 'sequência']`

Nós normalmente usamos loops **for** quando trabalhamos com funções `map()` e usamos list comprehension quando esta for mais fácil ser aplicada.

No entanto, há uma vantagem substancial de desempenho ao utilizar a list comprehension.

### Zipe e Enumerate

A função `zip()` agrega os valores de duas sequências e retorna uma tupla.

`zip(sequência, sequência)`

`zip()` poder ser usado quando o número de elementos for diferente em cada sequência. Mas o objeto resultante terá o mesmo número de elementos da sequência menor.

Ou seja:

```
zip([1, 2, 3, 4], [1, 2, 3])

(1, 1) (2, 2) (3, 3)
```

Outra função bastante útil é `enumerate()`

A função enumerate permite retornar o índice de cada valor em uma  sequência, a medida  que você percorre toda a sequência.

Enumerate retorna uma tupla no formato `tupla(índice, valor)`.

`enumerate(sequência)`

### Erros e Exceções

Código faltando ':', irá apresentar um erro se for executada.

```
while True
   print('Bem-vindo')
```

Porém, mesmo quando uma expressão estiver sintaticamente correta, ainda poderão ocorrer erros e neste caso, chamamos de Exceções.

Podemos tratar exceções em Python, da seguinte forma:

```
try:
   aqui vão as opreações...
except Exceção1:
   Se houver a Exceção1, execute este bloco
except Exceção2:
   Se houver a Exceção2, execute este bloco
else:
   Se não houver exceção, execute este bloco
```

Temos ainda a palavra reservada Finally, que nos  permite executar código, mesmo que exceções ocorram.

Uma lista completa de exceções em Python, poder ser encontrada aqui:

https://docs.python.org/3.6/library/exceptions.html
## **[Módulo 05] - Orientação a Objetos**

###  Resumo do que aprenderemos neste módulo:

Programação Orientada a Objetos (POO) tende a ser um dos principais obstáculos para iniciantes em Python.

* Usando a palavra reservada class
* Criando atributos de class
* Criando métodos em uma classe
* Instanciando Objetos
* Herança
* Métodos especiais

A orientação a objetos é um modelo de  <u>análise</u>, <u>projeto</u> e <u>programação</u> de sistemas de <u>software</u> baseado na composição e interação entre diversas unidades de software chamadas de objetos.

A **Programação Orientada a Objetos (POO)**, foi criada para tentar aproximar o mundo real e o mundo virtual. A ideia fundamental é tentar simular o mundo real dentro do computador.

Na Programação Orientada a Objetos, o programador (você) é responsável por moldar o mundo dos objetos, e definir como os objetos devem interagir entre si.

Os objetos "conversam" uns com os outros através do envio de mensagens e o papel principal do programador é definir quais serão as mensagens que cada  objeto pode receber e também qual a ação que o objeto deve realizar ao receber cada mensagem.

Alguns exemplos de linguagens orientadas a objetos modernas utilizadas por grandes empresas em todo o mundo são:

Java, C#, C++, Ruby, Lisp, Python,  etc.

### Programação Estruturada x Programação Orientada a Objetos

* Programação Estruturada:
   * Sequência
   * Decisão
   * Iteração (Repetição)

Na Programação Estruturada uma aplicação é composta por dados e funções.

* Programação Orientada a Objetos:
   * A escrita do código tenta trazer objetos do mundo real para se tornar parte do seu código

Aplicação → Cada objeto sem atributos e métodos

Ex:

```
====================
|+Classe = Cachorro|  # nome do objeto
====================
|-tamanho: int     |  # atributos do objeto
|-raca: String     |
====================
|*latir()          |  # métodos do objeto
====================
```

### Pricipais conceitos da Programação Orientada a Objetos

* Classe
   * São abstrações computacionais que representam entidades do mundo real
   * É um template e cada instância de uma classe é um objeto
* Objeto
   * É uma instância de uma classe que por sua vez possui atributos que são características ou propriedades do objeto
* Atributos
   * São características ou propriedades que ajudam a identificar os objetos
* Métodos
   * São ações do objeto
   * São funções dentro de uma classe
* Mensagem
   * É a chamada a um objeto, para invocar um de seus métodos
* Herança
   * É o mecanismo pelo qual uma classe chamada subclasse pode extender uma outra classe chamada de superclasse, aproveitando seus atributos e métodos, ou seja, a subclasse herda atributos e métodos da superclasse
   * Ela possibilita que as classes compartilhem seus atributos, métodos e outros membros dentro da classe em si
* Polimorfismo
   * Principio apartir do qual as classes derivadas de uma unica classe base são capazer de invocar os métodos que embora apresentem a mesma definição, comportam-se de maneira diferente  para cada  uma  das classes derivadas
   * Com o Polimorfismo  os mesmos atributos  e métodos podem ser utlizados em objetos distintos, porém com implementações lógicas diferentes
* Encapsulamento
  * É a técnica que faz com que detalhes internos do funcionamento dos métodos de uma classe permaneçam ocultos para os objetos

### Classes o Objetos

A classe é a estrutura básica do paradigma de orientação a objetos, que representa o tipo do objeto, um modelo a partir do qual os objetos serão criados.

Uma classe é apenas  um molde. Uma especificação que  define o que um objeto desse tipo deverá ter como atributo e como ele deve se comportar.

Por exemplo:

Podemos criar a classe Livro.

A classe é uma espécie de template que define a natureza de um futuro objeto.

A partir de classes, nós contruímos instâncias.

Cada instância é um objeto.

Uma instância, é um objeto específico, criado a partir de uma classe.

Objetos representam entidades, com suas qualidades (atributos) e ações (métodos) que estas podem realizar.

Em Python tudo é um objeto.

list, tuple, dict, int, float

E como podemos criar nossos próprios objetos em Python?

Objetos definidos pelo usuário em Python  são criados a partir de instâncias de classes criadas usandoa  palavra reservada **class**.

Por convenção, o nome de uma classe começa com letra maiúscula.

Em Python, novos objetos são criados a  partir das  classes. O objeto é uma instância da classe, quepossui características próprias.

### Métodos

Métodos são funções definidas dentro do corpo de uma classe.

Eles são usados para realizar operações com os atributos dos nossos objetos.

Métodos são usados no conceito de encapsulamento, do paradigma de Programação Orientada a Objetos.

Métodos são basicamente funções definidas dentro de uma classe, para manipular os objetos criados a  partir da classe.

Utiliza-se a palavra reservada **def** para criar métodos, da mesma forma que se cria funções.

Podemos criar classes para nossas atividades de análise de dados e criar métodos específicos para cada tarefa, encapsulando nossa lógicade programação.

### Herança

Herança é uma forma de gerar novas classes usando classes que foram definidas previamente.

Estas novas classes formadas, são chamadas classes derivadas ou sub-classes.

A classe  que deu origem a sub-classe, é chamada super-classe ou classe base.

Um dos principais benefícios da Herança é a reutilização de código e a redução da complexidade dos programas.

As classes derivadas estendem as funcionalidades das classes base.

### Métodos Especiais

Classes em Python podem implementar determinadas operações com métodos especiais.

Ao usar métodos especiais, sua classe poderá ter um comportamento semelhante a um dicionário, uma função ou mesmo um número.

Você já utilizou um método especial nos vídeos anteriores:

`__init__`

Por exemplo, quando você usa a função **del** para remover um atributo de um objeto, o método especial **\_\_delattr__** é chamado

Você digita isso: `del obj.my_attrib`

Python chama isso: **`obj._delattr_("my_attrib")`**

Ou seja, você não precisa fazer uma chamada ao método diretamente.

Python oferece vários métodos especiais para você!