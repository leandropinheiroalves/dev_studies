[Aula 01] - O que é Git? O que é versionamento?
    → Git != GitHub
    → Git de uma maneira bem simplória é um Software de Controle de Versão (VCS)
    → GitHub de uma maneira bem simplória é um Plataforma de Rede Social para Programadores

    [Git]
        → Basicamente se trata de versionamento, porque constantemente estamos trabalhando com diversas versões de uma mesma coisa
        Ex: Um cliente pede para desenvolver um site, você cria uma pasta para o site do cliente e a cada melhoria você salva ela:
            →site-cliente                →→→ Fase inicial, criando pasta para uma boa organização
            →site-cliente.zip            →→→ Depois da aprovação do cliente que o caminho está certo, você zipa o site para guarda-lo
            →site-cliente-v2.zip         →→→ Depois de algumas melhorias vem a Versão 2
            →site-cliente-deu-bosta.zip  →→→ Ouve um erro no site, e você salva mesmo assim, pois pode ser que aconteça um problema maior no futuro
            →site-cliente.zip-resolvido  →→→ Depois de resolver o problema você salva mais uma vez
            →site-cliente-agora-vai.zip  →→→ Depois de mais algumas mudanças parece que agora vai
            →site-cliente-mudou-tudo.zip →→→ Cliente decidiu mudar tudo
            ↑ No caso acima, é necessário um VCS(Controle de versão) para que nada se perca e fique mais facil trabalhar em conjunto com outras pessoas

    [Versionamento (VCS]
        → Primeiro VCS foi criado em 1972 é funcionava de forma centralizada/linear
        → Versionamento centralizado/linear:
            → Nesse tipo de versionamento, era necessário estar sempre conectado com o servidor do repositorio central
            → Era possível várias pessoas enviarem pastas para o servidor central ao mesmo tempo usando o commit
                → Commit: Quando você envia uma pasta para um repositório central, você está fazendo um commit
            → Alguns exemplos de Software de Versionamento Centralizados:
                → Ca Software Change Manager (CCC)
                → Source Code Control System (SCCS)
                → Panvalet
                → *Concurrent Version System (CVS)
                → *Apache Subversion (SVN)
                → ClearCase
                → Visual SourceSafe
                → Perforce

    [Versionamento distribuído]
        → Este tipo de versionamento é mais moderno, ele possibilita que cada pessoa do projeto tenha um software de versionamento no próprio computador
        → Nesse caso não é necessário estar conectado com o servidor
        → Nesse tipo de VCS existe um repositório remoto (nuvem)
        → Os programadores nesse modo enviam o commit para um repositório local, armazenado na própria máquina
        → Quando se acomulam vários commits, o programador faz um push, que envia todos os commits para o repositório remoto
            ► Push: Basicamente jogar o versionamento que está na sua máquina para o repositório remoto
        → Alguns exemplos de Software de Versionamento Distribuído:
            → Mercurial
            → Bazaar
            → Code Co-op
            → GNU arch
            → Monotone
            → Fossil
            → *BitKeeper
            → *Git

    [Principais Vantagens de se utilizar VCS]
        → Controle de histórico
        → Trabalho em equipe
        → Ramificação do projeto
        → Segurança
        → Organização

[Aula 02] - O que é GitHub? Pra que ele serve?

    [GitHub]
        → GitHub é um repositório remoto, onde fica armazenado as versões do seu projeto
        → GitHub também é uma plataforma social, nela você pode se conectar com pessoas, e ajudar e ser ajudado por elas
        → Vantagens do GitHub:
            ► Repositórios ilimitados
            ► Hospedagem de código-fonte
            ► Características de rede social
            ► GitHub Pages integrado
            ► Colaboração
            ► Forks → Copiar um projeto completo

    [Só existe o GitHub?]
        → GitLab
        → Bitbucket
        → PHABRICATOR
        → Gogs
        → kallithea

[Aula 03] - A Evolução do Git e GitHub

    [Um pouco de história]
        → 1985:
            →→ CVS
                ► Centralizado
                ► Open Source
                ► Mais popular
                ► Alguns problemas

        → 2000:
            →→ SVN
                ► Centralizado
                ► Open Source
                ► Ativo até hoje
                ► CVS-like (tentava copiar tudo do CVS)
            →→ BitKeeper
                ► Distribuído
                ► Proprietário
                ► Versão comunidade
                    ► Maior cliente da versão comunidade era o kernel do Linux do (Linus Torvalds)
                ► CVS-free (totalmente diferente do CVS)

        [A treta no BitKeeper]
            →→ 2004:
                ► Um utlizador do BitKeeper (Andrew Tridgell):
                    ► Criou um programa SourcePuller
                    ► Utilizou Engenharia Reversa
                    ► Conseguiu destravar alguns recursos do BitKeeper pago
                    ► Causando uma treta entre o criador do BitKeeper (Larry McVoy) e ele
            →→ 2005:
                ► BitKeeper criou uma nova licença que:
                    ► Cancelava muitas coisas da versão comunidade
                    ► Bloqueava o acesso ao metadados
                        ► Só deixando acesso para versão comercial
                            ► O criador do kernel do Linux (Linus Torvalds) não gostou
                                ► Tentou convencer o BitKeeper a reconsiderar mas não teve jeito
                                ► Então Linus Torvalds resolveu criar seu próprio software
                                ► Criando assim em 2005 o Git
                ► Git:
                    ► Distribuído
                    ► Open Source
                    ► Feito em 10 dias (com pressa e raiva)
                    ► Focado na performance, sendo muito melhor que os concorrentes da época

    [O que quer dizer 'Git'? (Nas palavras de seu criador Linus Torvalds)]
        → Três letras do alfabeto, formando um nome que era facil de falar e nenhuma unix utilizava como comando
        → Diz ironicamente que é uma gíria inglesa que significa:
            ► Teimoso, cabeça-dura, pensa que sempre está certo (fez em homenagem a ele)
        → Se o Git estiver funcionando bem e você quiser meter o louco em alguém:
            ► Global information tracker
        → SE o Git estiver uma bosta e dando erro:
            ► Goddman idiotic truckload of shit (Basicamente um caminhão idiota cheio de bosta)

    [E o GitHub?]
        → 2008:
            →→ GitHub foi criado por 4 amigos:
                ► Chris Wanstrath
                ► Tom Preston-Werner:
                    ► Criou o Gravatar
                ► Scott Chacon:
                    ► Autor do livro Pro Git
                ► P. J. Hyett

    [Vantagens GitHub]
        → 2008:
            ► Proprietário (mas com uma mente um pouco aberta)
            ► Hospedagrem de código
            ► Baseado em Git
        → 2009: 46k repositórios (crescimento meteórico)
        → 2010: 100k usuários / 1M repositórios
        → 2011: Ultrapassou SourceForge (que era a principal ferramenta do mercado)
        → 2013: 3M usuários / 5M repositórios
        → 2016: 14° lugar na lista da Forbes(Uma lista de 100 empresas de nuvem que você tem que ficar de olho porque elas serão o futuro)
        → 2018:
            ► Maior ataque de DDoS da história contra o GitHub(o maior ataque da história)
            ► Adquiridos pela Microsoft (US$ 7.5 Bilhões)
                ► Deixar o GitHub com operação independente
                ► 2020: GitHub compra a npm(node pack manager)

    [E esse mascote estranho do GitHub]
        → Não tem significado específico, os donos do GitHub só gostaram do desenho

[Aula 04] - Instalações e configurações importantes

    [Programas Necessários]
        → Google Chrome
            ► Digitar ?standalone=1 no final da barra de downloads
        → Virtual Studio Code
            ► Versão Stable: Versão mais estável e mais recomendada para o uso
            ► Versão Insiders: Versão mais atual e avançada, porém menos estável
        → Git SCM
        → GitHub Desktop

[Aula 05] - Criando o primeiro Repositório

    ► Criar repositório local (Git) com o nome Ola Mundo

    [Termos usados]
        → Commit
            ► Envia as alterações feitas no seu projeto, para o seu repositório local (Git)
        → Push
            ► Empurra todas as alterações do seu repositório local (Git) para o repositório remoto (GitHub)
        → Pull
            ► Puxa todas as alterações do repositório remoto (GitHub) para o seu repositório local (Git)
        → Fetch
            ► Verifica as versões do repositório remoto e do repositório local, informando as diferenças e quais ações podem ser feitas

    [Alguns comandos GitHub Desktop]
        → Ctrl + Shift + A:
            ► Abrir repositório diretamente no Visual Studio Code
        → Ctrl + P:
            ► Push
        → Ctrl + Enter depois Ctrl + P:
            ► Faz o commit das alterações para o repositório local e em seguida já faz o Push pro repositório remoto

[Aula 06] - Instalando GitHub Desktop no Linux (Ubuntu foi utilizado na aula)

    [Programas Necessários]
        → Git:
            ► No Ubuntu, Ctrl + Alt + T para abrir o terminal
            ► sudo apt update (sera pedido a senha)
            ► sudo apt upgrade -y (-y confirma sozinho)
            ► sudo apt install git -y
                ► git --version (ver versão do Git)
        → Google Chrome
        → Virtual Studio Code
            ► Versão Stable: Versão mais estável e mais recomendada para o uso
            ► Versão Insiders: Versão mais atual e avançada, porém menos estável
        → GitHub Desktop:
            ► Ainda não disponível para Linux
            ► No entanto, GitHub Desktop é um software livre
                ► github.com/shiftkey
                ► Ir até os repositorios do shiftkey e encontrar o repositório desktop
                ► Ir no readme e cliclar em latest releases
                ► No caso do Ubuntu baixair o .deb

[Aula 07] - Clonando um Repositório

    [O que é Repositório]
        → É uma área onde eu tenho código que está versionado, esse repositório pode ser público ou privado

    [Como clonar um Repositório]
        → Entrar no github.com/gustavoguanabara e entrar no repositório html-css
            ► Clicar em code, depois em Open With GitHub Desktop
            ► Escolher a pasta do seu computador onde deseja salvar e confirmar

    [Como saber se uma pasta está versionada]
        → Entre na pasta e configure para exibir os arquivos ocultos
            ► Se existir uma pasta oculta chamada .git, está pasta está sendo versionada

[Aula 08] - Versionando seus projetos antigos

    [Criando um novo Repositório]
        → GitHub Desktop:
            →→ Ir em File > New repository... ou apertar o atalho Ctrl + N
            →→ Será necessário:
                ► Colocar um nome para o seu repositório
                ► Colocar uma descrição
                ► Escolher o local onde será criado o repositório
                    ► Sempre marque a opção de iniciar o repositório com um README
                ► Escolher o Git Ignore baseado na linguagem do código
                    ► Ao escolher a linguagem, o git irá ignorar arquivos compilados e deixar só os códigos necessários para sua aplicação
                ► Escolher Licença (por padrão MIT)
            →→ Depois dos passos acima, o repositório será criado localmente, mas ainda será necessário:
                ► Publicar seu repositório local no repositório remoto:
                    ► Clicar em Publish repository no GitHub Desktop
                        ► Será necessário um nome e uma descrição para o repositório remoto
                            ► Por padrão ele já utiliza o nome e a descrição do repositório local, mas é possível alterar
                        ► Será necessário escolher se o repositório será público ou privado
                        ► Será necessário escolher uma organização
                            ► No caso de usuário sem organização escolher None, escolha que já vem por padrão

[Aula 09]  Você sabe usar Issues?

    [O que é uma Issue?]
        → Issue é um problema identificado por alguém que não sabe como resolver o problema, por exemplo:
            ► Um usuário está usando o vscode e ele dá um problema inesperado
                ► Caso o usuário não saiba como resolver o problema, ele pode ir no repositório da do vscode e abrir uma issue informando o problema
        → Sempre que for identificado um problema, antes de abrir uma Issue, procure no repositóri da organização responsável se já não existe uma issue sobre o assunto
        → Issues são muito importantes para você contribuir com projetos livres, olhando as issues abertas e tentando fecha-las.

[Aula 10] - Guia da Linguagem Markdown

    [Markdown]
        → Uma linguagem focada em marcação, assim como HTML
        → É compátivel com vários sites, inclusive o GitHub
        → Basicamente serve para criar formatações em um texto dentro de um site ou arquivo de uma forma mais simples que o html
        → README.md é um arquivo markdown que existe nos repositórios do GitHub
        → É utilizado dentro do GitHub no README, arquivos .md, em issues e pull requests.

    [Aluns comando em Markdown]
        → Negrito (** ou __): utlizado no início e no final das frases ou palavras
        → Itálico (* ou _): utlizado no início e no final das frases ou palavras
        → Riscado no meio (~~): utlizado no início e no final das frases ou palavras
        → Título Principal (#): utilizado no inicio da frase
        → Título Nível 2 (##): utilizado no inicio da frase
        → Título Nível 3 (###): utilizado no inicio da frase
        → Linha (--- ou ***): cria uma linha de separação
        → Lista numerada (1.): cria uma lista númerada, pode ser colocado qualquer número que ele irá organizar de forma cronológica
            ► (   1.): 3 espaços antes cria um sub item do item anterior
        → Lista demarcada (* ou -): cria uma lista demarcada
            ► (   * ou    -): 3 espaços antes cria um sub item do item anterior
        → Lista de tarefas (-[]): cria uma lista de check list
            ► (-[x]): mostra que a tarefa foi marcada
        → Colocar imagens (![texto](link): coloca imagem apartir de um link
            ► também é possível arrastar a imagem que você tenha para dentro do texto
        → Links ([texto](link)): faz com que o texto entre [] fique com hiperlink do link adicionado entre ()
        → Tabelas (|):
            ► Colocar os termos separados por | faz com que se crie a linha da tabela
                Num | Nome | Nota
                ---|---|---
                1|Gustavo|8,5
                2|José|10
                3|Maria|9
        → Comando (`): utlizado no início e no final do comando para mostrá-lo como comando
        → Trechos de programa(```): utlizado no início e no final do bloco de comando para mostrá-los como código
        → Emojis (:): depois que colocar os : vai aparecer indicações
            ► github.com/ikatyang > repositories > emoji-cheat-sheet
                ► todos os emojis disponíveis de forma organizada
            ► emojipedia.org
                ► códigos para poder utilizar os emojis nos nomes das issues
        → Marcar pessoas (@): utilizar antes do @ o nome da conta no github para criar um link para o perfil dela
        → Quotes (>): colocar o sinal de maior antes do link da postagem para mensioná-la
            ► clicar na mensagem que quer da quote e ir em quote

[Aula 11] - Seu GitHub muito mais seguro

    [Dicas para senhas fortes]
        → Pelo menos 8 caracteres
        → Letras e números
        → Maiúsculas e minúsculas
        → Símbolos
        → Evitar nomes e palavras comuns
        → Evitar padrões
        → Nunca compartilhe uma senha

    [Utilizar Autênticação em dois passos]
        → Baixar no GooglePlay o Google Authenticator
        → Utilizar não só no GitHub mas em todas as contas que permitirem autênticação em 2 passos

[Aula 12] - Git Branches de forma fácil e com exemplo

    [Branch ou Ramificações]
        → Branch é uma ramificação do seu produto principal, que normalmente é chamado master
        → A branch principal é a master, e depois de muitos commits pra ela, você pode fazer um pull pra origin
            ► master: principal branch local do seu projeto
            ► origin: branch remota do seu projeto, que serve como um backup
                ► a cada commit nova você cria um versionamento novo no seu projeto
                ► depois é feio um push para o repositório remoto

    [Branches em Projetos Grandes]
        → Não commitar tudo na brach master!
            ► Se ouver algum erro, você estará mandando esse erro pro seu ramo principal e isso é péssimo
            ► O correto é criar um projeto estável, e depois todas as alterações que forem ser feitas, criar novas branches para elas
            ► Depois que seu novo ramo estiver estável e passar por todas as avaliações necessárias, você pode joga-la na branch principal usando o merge
                ► Merge: Ele joga seu ramo secundário no ramo principal
            ► Quando se usa ramos secundários, a qualquer momento você pode descarta-los que nada será alterado do ramo principal




















