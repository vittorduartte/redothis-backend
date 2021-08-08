# 📜 Redothis - Gerenciando e documentando a criação acadêmica 

 [🇧🇷] O Redothis é uma plataforma de gerenciamento de projetos acadêmicos. Inicialmente projetado para trabalhos de propósitos gerais. Para mais, leia o README. [🇺🇸] The Redothis this a platform for management academic project of general purposes. For more read the README.

<p align="center">
<img src="https://raw.githubusercontent.com/vittorduartte/redothis-backend/main/assets/redothis_frontend" alt="Mateus Vitor Duarte" border="0">
</p>

<p align="center">
  <img alt="PRs welcome!" src="https://img.shields.io/static/v1?label=PRs&message=WELCOME&style=for-the-badge&color=E34447&labelColor=222222" />
     
   <img alt="Stars" src="https://img.shields.io/github/stars/vittorduartte/redothis-backend?color=E34447&label=STARS&logo=3C424B&logoColor=3C424B&style=for-the-badge&labelColor=222222" />

   <img alt="Forks" src="https://img.shields.io/github/forks/vittorduartte/redothis-backend?color=E34447&label=FORKS&logo=3C424B&logoColor=3C424B&style=for-the-badge&labelColor=222222" />

   <img alt="Issues" src="https://img.shields.io/github/issues/vittorduartte/redothis-backend?color=E34447&label=ISSUES&logo=3C424B&logoColor=3C424B&style=for-the-badge&labelColor=222222" />

   <img alt="GitHub license" src="https://img.shields.io/github/license/vittorduartte/redothis-backend?color=E34447&label=LICENSE&logo=3C424B&logoColor=3C424B&style=for-the-badge&labelColor=222222" />

  <a href="https://github.com/vittorduartte">
    <img alt="Follow vittorduartte" src="https://img.shields.io/static/v1?label=Follow&message=vittorduartte&style=for-the-badge&color=E34447&labelColor=222222" />
  </a>
  <a href="https://github.com/elheremes">
    <img alt="Follow elheremes" src="https://img.shields.io/static/v1?label=Follow&message=elheremes&style=for-the-badge&color=1D4080&labelColor=222222" />
  </a>
</p>

💡[🇧🇷] O Redothis é uma maneira de professores e alunos organizarem o desenvolvimento de projetos acadêmicos documentando todas as etapas e gerenciando as versões e artefatos geradas em cada parte desse processo.
Inicialmente desenvolvido para trabalhos acadêmicos de propósitos gerais, a plataforma está atualmente
ajustada para receber projetos de Trabalho de Conclusão de Curso - TCC que é o formato usualmente utilizado
pelas instituições.

💡[🇺🇸] Is coming.

## 💻 Configuração para Desenvolvimento

O projeto requer a utilização das versões 3 do Python, bem como o gerenciador de ambientes **Pipenv**.

1. Instalação **Pipenv**:
```sh
pip install pipenv
```

2. Clone do repositório do projeto:
```sh
git clone https://github.com/vittorduartte/redothis-backend
```

3. Criação do arquivo **.env** de variáveis de ambiente:
```sh
cd redothis-backend
touch .env
```

4. Conteúdo do arquivo **.env**:
```environment
FLASK_APP=redothis/app.py
FLASK_ENV=development
SECRET_KEY="<escolha_uma_chave_secreta>"
SQLALCHEMY_DATABASE_URI="sqlite:///database.db"
JWT_REQUIRED_CLAIMS="['exp']"
```

5. Ativação do ambiente e execução do servidor:
```sh
pipenv install
pipenv shell
flask run
```

## 📈 Exemplo de uso

Alguns exemplos interessantes e úteis sobre como seu projeto pode ser utilizado.

Adicione blocos de códigos e, se necessário, screenshots.

_Para mais exemplos, consulte a [Wiki](wiki)._ 

## 🚀 Deployment

Instruções para deploy do projeto.

## 🗃 Histórico de lançamentos

<!-- * 0.0.1
    * MUDANÇA: Atualização de docs (código do módulo permanece inalterado)
* 0.2.0
    * MUDANÇA: Remove `setDefaultXYZ()`
    * ADD: Adiciona `init()`
* 0.1.1
    * CONSERTADO: Crash quando chama `baz()` (Obrigado @NomeDoContribuidorGeneroso!)
* 0.1.0
    * O primeiro lançamento adequado
    * MUDANÇA: Renomeia `foo()` para `bar()` -->
* 0.0.1
    * Representação do diagrama relacional do banco de dados:
         
         <img src="https://raw.githubusercontent.com/vittorduartte/redothis-backend/main/assets/database_diagram.png">

## 📋 Meta

Mateus Vitor – [Portfólio](https://vittorduartte.github.io/) – mateusriograndense@gmail.com

<!-- Distribuído sob a licença XYZ. Veja `LICENSE` para mais informações. -->

[https://github.com/vittorduartte/redothis-backend](https://github.com/vittorduartte/redothis-backend)

## 🚀 Contribuição

1. Faça o _fork_ do projeto (<https://github.com/vittorduartte/redothis-backend/fork>)
2. Crie uma _branch_ para sua modificação (`git checkout -b meu-novo-recurso`)
3. Faça o _commit_ (`git commit -am 'Adicionando um novo recurso...'`)
4. _Push_ (`git push origin meu-novo-recurso`)
5. Crie um novo _Pull Request_