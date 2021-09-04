[Aula 01] - O que é Git? O que é versionamento?
    → Git != de GitHub
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

        → Versionamento distribuído:
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

        → Principais Vantagens de se utilizar VCS
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

    → Só existe o GitHub?
        → GitLab
        → Bitbucket
        → PHABRICATOR
        → Gogs
        → kallithea



























