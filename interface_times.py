import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="times"
    )

def listar_times():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, cidade, estado, pais, ano_fundacao, estadio, capacidade_estadio, tecnico, liga FROM times_futebol")
    times = cursor.fetchall()
    for time in times:
        print(f"ID: {time[0]} | Nome: {time[1]} | Cidade: {time[2]} | Técnico: {time[8]} | Liga: {time[9]}")
    cursor.close()
    conexao.close()

def buscar_time():
    nome = input("Digite o nome do time para buscar: ")
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "SELECT * FROM times_futebol WHERE nome LIKE %s"
    cursor.execute(sql, (f"%{nome}%",))
    resultados = cursor.fetchall()
    if resultados:
        for time in resultados:
            print(f"ID: {time[0]} | Nome: {time[1]} | Cidade: {time[2]} | Técnico: {time[8]} | Liga: {time[9]}")
    else:
        print("Nenhum time encontrado.")
    cursor.close()
    conexao.close()

def inserir_time():
    print("Digite os dados do novo time:")
    nome = input("Nome: ")
    cidade = input("Cidade: ")
    estado = input("Estado (ou deixe vazio): ") or None
    pais = input("País: ")
    ano_fundacao = input("Ano de fundação: ")
    estadio = input("Estádio: ")
    capacidade_estadio = input("Capacidade do estádio: ")
    tecnico = input("Técnico: ")
    liga = input("Liga: ")

    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    INSERT INTO times_futebol (nome, cidade, estado, pais, ano_fundacao, estadio, capacidade_estadio, tecnico, liga)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = (nome, cidade, estado, pais, ano_fundacao, estadio, capacidade_estadio, tecnico, liga)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Time inserido com sucesso!")
    cursor.close()
    conexao.close()

def atualizar_time():
    id_time = input("Digite o ID do time que deseja atualizar: ")
    print("Digite os novos dados (deixe vazio para não alterar):")
    nome = input("Nome: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    pais = input("País: ")
    ano_fundacao = input("Ano de fundação: ")
    estadio = input("Estádio: ")
    capacidade_estadio = input("Capacidade do estádio: ")
    tecnico = input("Técnico: ")
    liga = input("Liga: ")

    conexao = conectar()
    cursor = conexao.cursor()


    campos = []
    valores = []

    if nome: campos.append("nome=%s"); valores.append(nome)
    if cidade: campos.append("cidade=%s"); valores.append(cidade)
    if estado: campos.append("estado=%s"); valores.append(estado)
    if pais: campos.append("pais=%s"); valores.append(pais)
    if ano_fundacao: campos.append("ano_fundacao=%s"); valores.append(ano_fundacao)
    if estadio: campos.append("estadio=%s"); valores.append(estadio)
    if capacidade_estadio: campos.append("capacidade_estadio=%s"); valores.append(capacidade_estadio)
    if tecnico: campos.append("tecnico=%s"); valores.append(tecnico)
    if liga: campos.append("liga=%s"); valores.append(liga)

    if not campos:
        print("Nenhum dado para atualizar.")
        return

    valores.append(id_time)

    sql = f"UPDATE times_futebol SET {', '.join(campos)} WHERE id = %s"
    cursor.execute(sql, valores)
    conexao.commit()
    print("✅ Time atualizado com sucesso!")
    cursor.close()
    conexao.close()

def deletar_time():
    id_time = input("Digite o ID do time que deseja deletar: ")
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "DELETE FROM times_futebol WHERE id = %s"
    cursor.execute(sql, (id_time,))
    conexao.commit()
    print("🗑️ Time deletado com sucesso!")
    cursor.close()
    conexao.close()

def menu():
    while True:
        print("\n==== Sistema de Times de Futebol ====")
        print("1 - Listar todos os times")
        print("2 - Buscar time por nome")
        print("3 - Inserir novo time")
        print("4 - Atualizar time")
        print("5 - Deletar time")
        print("0 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            listar_times()
        elif escolha == "2":
            buscar_time()
        elif escolha == "3":
            inserir_time()
        elif escolha == "4":
            atualizar_time()
        elif escolha == "5":
            deletar_time()
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
