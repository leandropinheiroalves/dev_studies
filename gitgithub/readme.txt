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
                → Push: Basicamente jogar o versionamento que está na sua máquina para o repositório remoto
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

    → GitHub é um repositório remoto, onde fica armazenado as versões do seu projeto
    → GitHub também é uma plataforma social, nela você pode se conectar com pessoas, e ajudar e ser ajudado por elas
    → Vantagens do GitHub:
        → Repositórios ilimitados
        → Hospedagem de código-fonte
        → Características de rede social
        → GitHub Pages integrado
        → Colaboração
        → Forks → Copiar um projeto completo

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


