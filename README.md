# DESAFIO BACK END JUNIOR - FEITO POR: KYLIE SANTOS

## sobre o projeto
esta é uma api rest simples para leitura de usuários, desenvolvida em python com o framework flask. o projeto foi criado como parte de um desafio técnico para uma vaga de desenvolvedor back-end.

a api serve dados a partir de um arquivo mock-users.json e segue uma arquitetura em camadas (controllers, services, repository) para uma clara separação de responsabilidades. o projeto também inclui um conjunto de testes automatizados usando pytest.

---

## o que ele faz
- lista usuários com paginação.  
- permite a busca de usuários por nome ou e-mail.  
- permite a filtragem de usuários por cargo (role) e por status (is_active).  
- retorna os dados de um usuário específico através do seu id.  

---

## estrutura de pastas

```
├── app/
│ ├── init.py
│ ├── controllers.py # camada de rotas (http)
│ ├── services.py # camada de lógica de negócio
│ └── repository.py # camada de acesso a dados
├── tests/
│ ├── conftest.py # configuração dos testes
│ └── test_users.py # testes da api de usuários
├── .env # variáveis de ambiente
├── mock-users.json # arquivo com os dados dos usuários
├── pyproject.toml # arquivo de configuração do projeto
├── requirements.txt # dependências do projeto
└── run.py # ponto de entrada da aplicação
```

## como executar

### pré-requisitos
- Flask  
- python-dotenv  
- pytest  

### instalação
clone o repositório para a sua máquina local:

git clone https://github.com/kyliews/desafiobackjunior-kylie-valcann-

crie e ative um ambiente virtual:

## windows
python -m venv venv
.\venv\scripts\activate

## macos/linux
python3 -m venv venv
source venv/bin/activate


instale as dependências do projeto:

pip install -r requirements.txt


instale o projeto em modo editável (pois tem importações para os testes):

pip install -e .


crie um arquivo .env na raiz do projeto e adicione a seguinte linha:

FLASK_DEBUG=1


## execução

com o ambiente virtual ativado inicie o servidor com o seguinte comando:

python run.py


a api estara no endereço:
http://127.0.0.1:5000

## rodando os testes

para garantir que tudo está funcionando corretamente, execute a suíte de testes automatizados no terminal: 

pytest

```
exemplos de uso com curl
listar usuários (página 1, 10 por página)
curl "http://127.0.0.1:5000/users"

listar usuários com paginação
curl "http://127.0.0.1:5000/users?page=2&page_size=5"

buscar por nome ou email
curl "http://127.0.0.1:5000/users?q=hoffmann"

filtrar por cargo e status
curl "http://127.0.0.1:5000/users?role=manager&is_active=false"

obter um usuário por id
curl "http://127.0.0.1:5000/users/1"

tentar obter um usuari que nao existe
curl "http://127.0.0.1:5000/users/999"
```
