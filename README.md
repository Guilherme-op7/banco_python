---

# 🐍 Sistema de Cadastro de Times de Futebol - Python + MySQL

Este projeto foi a **minha primeira experiência conectando o Python com um banco de dados MySQL**, rodando tudo direto pelo terminal.

O sistema permite **listar**, **buscar**, **inserir**, **atualizar** e **deletar** times de futebol em um banco de dados.

---

## ✅ O que o sistema faz

- Listar todos os times cadastrados
- Buscar times pelo nome
- Inserir novos times
- Atualizar dados de um time existente
- Deletar times pelo ID

---

## ⚙️ Tecnologias utilizadas

- **Python**
- **MySQL**
- **Biblioteca:** `mysql-connector-python`

---

## 🏗️ Estrutura do Banco de Dados

> Banco: `times`

> Tabela: `times_futebol`

### Exemplo da estrutura da tabela:

| Campo               | Tipo             |
|---------------------|------------------|
| id                  | INT (PK, AI)     |
| nome                | VARCHAR          |
| cidade              | VARCHAR          |
| estado              | VARCHAR (NULL)   |
| pais                | VARCHAR          |
| ano_fundacao        | INT              |
| estadio             | VARCHAR          |
| capacidade_estadio  | INT              |
| tecnico             | VARCHAR          |
| liga                | VARCHAR          |

---

## 🚀 Como executar o sistema

1. Certifique-se de ter o **MySQL** rodando localmente e o banco de dados `times` criado.

2. Instale o conector MySQL para Python:

```bash
pip install mysql-connector-python

3. Atualize as configurações de conexão no código se necessário (host, user, senha...).


4. Execute o programa no terminal:



python nome_do_arquivo.py


---

🖥️ Exemplo de Execução do Menu no Terminal

==== sistema de times de futebol ====
1 - listar todos os times
2 - buscar time por nome
3 - inserir novo time
4 - atualizar time
5 - deletar time
0 - sair
escolha uma opção:

👉 A partir daqui, o usuário digita o número da opção desejada e o sistema executa a função correspondente.


---

🙏 Agradecimentos

> Gostaria de agradecer ao Professor Robson, que me apresentou o conceito de banco de dados, despertando meu interesse e curiosidade para aprender a fazer essa conexão com Python.




---

✍️ Autor

Guilherme dos Santos Neto
