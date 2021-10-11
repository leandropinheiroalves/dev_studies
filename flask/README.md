# **Módulo 1 - Introdução ao Rest Api com Flask**

>## O que é uma API
* É um conjunto de rotinas para acesso a um aplicativo/software/plataforma baseado na Web
* Acrônimo de Application Programming Interface - Interface de programção de aplicativos
* APIs são importantes quando se tem a intenção de realizar integrações com outros serviços
* Com as APIs a comunicação de software fica transparente ao usuário
* APIs podem ser locais, baseada em web e baseada em programas

>## O que é REST
* É um modelo a ser utilizado para projetar arquiteturas de software baseado em comunicação via rede
* Acrônimo de Representational State Tranfer - Transferência de Estado Representacional
* Foi definido por Roy Fielding em sua tese de doutorado (PhD) na UC Irvine no ano 2000
* REST projeta a ideia de que todo recurso deveria responder aos mesmos métodos

>## O que é um REST API
* É uma API desenvolvida utilizando os princípios da arquitetura REST
* Um REST API é utilizado na comunicação/integração entre software através de serviços web
* Um REST API é consumido através de requisições HTTP
* REST APIs são geralmente representadas em seus formatos por JSON e XML. Também são usados páginas HTML, PDF e arquivos de imagens.
* Ao implementar um REST API, cada método deve ser responsável por um tipo diferente de ação. Exemplo: Consulta, Alteração, Inclusão e Exclusão.

>## Métodos do protocolo HTTP
* GET - Método que solicita algum recurso ou objeto do servidor por meio da URI.
* POST - Método usado para envio de arquivo/dados ou formulário HTML para o servidor.
* PUT - Aceitar criar ou modificar um objeto do servidor.
* DELETE - Informa  por  meio da URI o objeto a ser deletado.

>## URL, URN e URI
* URL: Uniform Resource Locator - Localizador de Recursos Universal
  * Host que será acessado. Exemplo: globallabs.academy
* URN: Uniform Resource Name - Nome do Recurso Universal
  * É o recurso que será identificado. Exemplo: /category/blog/
* URI: Uniform Resource Identifier - Identificador de Recursos Universal
  * É o identificador do recurso, podendo ser uma imagem, um arquivo ou uma página. Exemplo: https://globallabs.academy/category/blog
  * URI une Protocolo(https://), URL (globallabs.academy) e a URN (/category/blog)

>## XML e JSON
* XML - Extensible Markup Language
  * É uma linguagem de marcação
  * Utilizada para compartilhamento de informções através de requisições HTTP
    ```
    <xmlcep>
        <cep>22041-001</cep>
        <logradouro>Avenida Atlântica</logradouro>
        <complemento>de 2174 a 2634 - lado par</complemento>
        <bairro>Copacabana</bairro>
        <localidade>Rio de Janeiro</localidade>
        <uf>RJ</uf>
        <unidade/>
        <ibge>3304557</ibge>
        <gia/>
    </xmlcep>
    ```
* JSON - JavaScript Object Notation
  * É um formato de troca de dados entre sistemas independente da linguagem utilizada derivada do JavaScript
  * Muitas linguagens possuem suporte nativo a JSON
    ```
    {
        "cep":"22041-001",
        "logradouro":"Avenida Atlântica",
        "complemento":"de 2174 a 2634 - lado par",
        "bairro":"Copacabana",
        "localidade":"Rio de Janeiro",
        "df":"RJ",
        "unidade":"",
        "ibge":"3304557",
        "gia":""
    }
    ```

>## Framework Flask
* É um microframework para Python utilizado para desenvolvimento de aplicações WEB.
* É chamado de microframework porque mantém um núcleio simples, mas é estendível
* Flask não possui camada de abstração para banco de ados, validação de formulários entre outros, mas é possível estender com outras bibliotecas
* Por ser leve e simples de se usar, Flask é um dos frameworks Python mais utilizados para desenvolvimento de APIs.

# **Módulo 2 - Instalando Flask, criado ambiente virtual e introdução a Postman**

## O que utilizaremos
* Python 3.7
* Pycharm Community
* Flask
* Postman

## PIP
* Sistema de gerenciamento de pacotes
* Utilizado para instalar e gerenciar pacotes/bibliotecas em Python
* Já vem empacotado com Python desde a versão 3.4
   
## Instalação do Flask
  `> pip install Flask`

## Criando um ambiente virtual (VirtualEnv)
* Ferramenta para criar ambientes Python isolados
* Vem integrado com o Python desde a versão 3.3
* Extremamente útil para se trabalhar com projetos que utilizam bibliotecas com versões diferentes.

```
PS C:\Users\rafeg> python -m venv .\.virtualenvs\minha_virtualenv
PS C:\Users\rafeg> .\.virtualenvs\minha_virtualenv\Scripts\activate
(minha_virtualenv) PS C:\Users\rafeg> pip install Flask
```

## Pycharm
* IDE para desenvolvimento Python
* Robusta e torna o desenvolvimento muito mais rápido
* Possui versão paga e versão gratuita (Community)
* https://www.jetbrains.com/pycharm/download

## Postman
* Ferramenta utilizada para realizar requisições HTTP
* Com ela é possível chamar qualquer método e também enviar parâmetros
* https://www.getpostman.com/downloads/

# **Módulo 3 - Utilizando métodos, biblioteca Request e JSON**

* Agenda:
  * Retornando JSON
  * Entendendo tipagem na URI
  * Entendendo métodos
  * Lendo informações de entrada vindo como JSON através da requisição
  * Utilizando Postman para teste da API
  * Utilizando biblioteca Request para teste da API

# **Módulo 4 - Desenvolvendo uma Rest Api completa**

## Agenda
* Criando uma lista de registros
* Implementando métodos GET, POST, PUT e DELETE
* Manipulando dados com as API e métodos implementados

## Tarefa que realizaremos
* Veremos como implementar uma API para inclusão de novos desenvolvedores e seus conhecimentos
* Iremos manipular uma lista que irá conter o nome do desenvolvedor e suas habilidades(linguagens que domina)
* Tudo isso será feito através de API's

## Exercício para praticar
* Desenvolva uma API que gerencie um cadastro de tarefas.
* A API terá uma lista de tarefas que deverá ter os seguintes campos:
  * id
  * reponsável
  * tarefa
  * status
* A API deverá permitir listar todas as tarefas e também incluir novas tarefas
* A API deveŕa permitir consultar uma tarefa através do ID, alterar o status de uma tarefa e também excluir uma tarefa.
* Nenhuma outra alterção deverá ser permitida além do status da tarefa

### Dica
* Abaixo como ficará o início do cadastro de tarefas e como realizar a alteração do status.
* O método POST deverá receber o ID e o Status e assim realizar a alteração apenas do Status e não de todo o dicionário.
```
tarefas = [
    {
        'id':0,
        'responsavel':'Rafael',
        'tarefa':'Desenvolver método Get',
        'status':'concluido'
    },
    {
        'id':1,
        'responsavel':'Galleani',
        'tarefa':'Desenvolver método POST',
        'status':'pendente' 
    }
]

tarefas[1]['status'] = 'concluido'
```

# **Módulo 5 - Desenvolvendo uma REST API com a extensão Flask-RESTful**

## Agenda
* O que é RESTful
* A extensão Flask-RESTful
* Alterando nossa API REST para utilizar a extensão Flask-RESTful

## REST vs RESTful
* REST é um estilo arquitetônico, um modelo para se seguir ao desenvolver APIs.
* RESTful é um serviço web que utiliza desse paradigma. É utilizado para definir aplicações que implmentam webservices que utilizam a arquitetura REST.
* Podemos dizer que uma aplicação web que segue a arquitetura REST, ela é RESTful, ou seja, tem a capacidade de seguir a arquitetura REST.

## Flask-RESTful
* É uma extensão do Flask que adiciona suporte para construção rápida de REST APIs
* O uso Flask-RESTful acaba incentivando as práticas recomendadas para a arquitetura REST com uma configuração leve.
```
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
  def get(self):
    return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
  app.run(debug=True)

```

## Exercício para praticar
* Acrescentar na API de habilidade(módulo habilidades) os métodos PUT, POST e DELETE
* O método POST deverá inserir uma nova habilidade na lsita
* O método PUT a partir de um ID (identificação da posição) deverá  alterar o nome da habilidade que está naquela posição
* O método DELETE deverá deletar uma  habilidade que esteja na posição informado na requisição

# **Módulo 6 - Manipulando banco de dados com SQLAlchemy**

## Agenda
* O que é SQLAlchemy
* Banco de dados SQLite
* Como criar um banco de dados com SQLAlchemy
* Realizando operções de banco de dados (insert, update, select e delete)

## SQLAlchemy
* É um ORM para Python.
* Um ORM (object-relational mapping) em português Mapeamento objeto-relacional, ajuda na abstração das tabelas de banco de dados na orientação à objeto.
* Em ORMs tabelas viram classes e o desenvolvedor não precisa ter conhecimento SQL.
* SQLAlchemy fornece um conjunto completo de padrões de persistência, projetados para acesso a banco de dados eficiente e de alto desempenho, adaptado em uma linguagem de domínio Pythonica simples.

## SQLite
* É uma biblioteca de linguagem C que implementa um mecanismo de banco de dados pequeno, rápido e autônomo.
* É o mecanismo de banco de dados mais usado no mundo.
* Ele é incorporado em smartphones por exemplo.
* Com o SQLite é possível montar uma instância de banco de dados sem precisar realizar uma instalação de um banco.
* É muito prático para ambientes de desenvolvimento

## Exercício para praticar
* Em um novo diretório crie um banco de dados com três tabelas. Tabela Programador, tabela Habilidades e uma terceira tabela que ligue o programador com a habilidade, cujo nome será programador_habilidade
* A tabela Programador deve conter os campos:
  * id
  * nome
  * idade
  * email
* A tabel Habilidades deve conter os campos:
  * id
  * nome
* A tabela programador_habilidade deve conter os campo:
  * id
  * programador (FK com programador)
  * habilidade (FK com habilidade)

# **Módulo 7.1 - REST API com persistência em banco de dados**

## Agenda
* Incluir no projeto anterior um app Flask
* Elaborar as API para persistência em banco de dados com SQLAlchemy
* Além da persistência em banco de dados, também realizaremos todas as consultas em banco de dados

## Exercício para praticar
* No mesmo projeto da aula incluir para a modelagem Atividades uma API para retornar todas as atividades pelo nome da Pessoa responsável
* Incluir na modelagem de Atividade um campo Status que deverá receber pendente ou concluído
* Criar uma API que através do ID da atividade permita consulta e alterar apenas o Status da Atividade.
* Acrescentar uma tratativa de exceção em todos os métodos para enviar uma mensagem tratada caso o registro informado não exista

# **Módulo 7.2 - REST API com autenticação

## Agenda
* Incluir no projeto anteriro uma autenticação básica.
* Conhecer a extensão flask-httpauth
* Inserir autenticação através de usuários registrados em hard code no código.
* Inserir autenticação através de tabela de usuários no banco de dados.

## Flask-httpauth
* É uma extensão para o framework Flask que simplifica o uso de autenticação
* Com flask-httpauth além da implementação da autenticação ser mais simples, também é possível realizar diferentes tipos de autenticação, do tipo básico com usuário e senha até com token.
* https://flask-httpauth.readthedocs.io/en/latest/

### Flask-httpauth
```
from flask import Flask
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
  "john": "hello",
  "susan": "bye"
}

@auth.get_password
def get_pw(username):
  if username in users:
    return users.get(username)
  return None

@app.route('/')
@auth.login_required
def index():
  return f"Hello, {auth.username()}"

if __name__ == '__main__':
  app.run()
```

## Exercício para praticar
* No mesmo projeto incluir verificação em todos os métodos com exceção dos métodos de consulta, esses continuarão públicos.
* Incluir na tabela Usuários um campo com o nome Ativo, que pode ter 0 ou 1, indicando que o usuário está ativado (1) ou desativado (0)
* Ao realizar a autenticação, além do login e senha serem válidos, também será necessário validar se o usuário está ativado