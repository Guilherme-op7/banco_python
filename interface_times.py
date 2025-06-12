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
        print(f"id: {time[0]} | nome: {time[1]} | cidade: {time[2]} | técnico: {time[8]} | liga: {time[9]}")
    cursor.close()
    conexao.close()

def buscar_time():
    nome = input("digite o nome do time para buscar: ")
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "SELECT * FROM times_futebol WHERE nome LIKE %s"
    cursor.execute(sql, (f"%{nome}%",))
    resultados = cursor.fetchall()
    if resultados:
        for time in resultados:
            print(f"id: {time[0]} | nome: {time[1]} | cidade: {time[2]} | técnico: {time[8]} | liga: {time[9]}")
    else:
        print("nenhum time encontrado.")
    cursor.close()
    conexao.close()

def inserir_time():
    print("digite os dados do novo time:")
    nome = input("nome: ")
    cidade = input("cidade: ")
    estado = input("estado (ou deixe vazio): ") or None
    pais = input("país: ")
    ano_fundacao = input("ano de fundação: ")
    estadio = input("estádio: ")
    capacidade_estadio = input("capacidade do estádio: ")
    tecnico = input("técnico: ")
    liga = input("liga: ")

    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    INSERT INTO times_futebol (nome, cidade, estado, pais, ano_fundacao, estadio, capacidade_estadio, tecnico, liga)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = (nome, cidade, estado, pais, ano_fundacao, estadio, capacidade_estadio, tecnico, liga)
    cursor.execute(sql, valores)
    conexao.commit()
    print("time inserido com sucesso.")
    cursor.close()
    conexao.close()

def atualizar_time():
    id_time = input("digite o id do time que deseja atualizar: ")
    print("digite os novos dados (deixe vazio para não alterar):")
    nome = input("nome: ")
    cidade = input("cidade: ")
    estado = input("estado: ")
    pais = input("país: ")
    ano_fundacao = input("ano de fundação: ")
    estadio = input("estádio: ")
    capacidade_estadio = input("capacidade do estádio: ")
    tecnico = input("técnico: ")
    liga = input("liga: ")

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
        print("nenhum dado para atualizar.")
        return

    valores.append(id_time)

    sql = f"UPDATE times_futebol SET {', '.join(campos)} WHERE id = %s"
    cursor.execute(sql, valores)
    conexao.commit()
    print("time atualizado com sucesso.")
    cursor.close()
    conexao.close()

def deletar_time():
    id_time = input("digite o id do time que deseja deletar: ")
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "DELETE FROM times_futebol WHERE id = %s"
    cursor.execute(sql, (id_time,))
    conexao.commit()
    print("time deletado com sucesso.")
    cursor.close()
    conexao.close()

def menu():
    while True:
        print("\n==== sistema de times de futebol ====")
        print("1 - listar todos os times")
        print("2 - buscar time por nome")
        print("3 - inserir novo time")
        print("4 - atualizar time")
        print("5 - deletar time")
        print("0 - sair")
        escolha = input("escolha uma opção: ")

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
            print("saindo...")
            break
        else:
            print("opção inválida. tente novamente.")

if __name__ == "__main__":
    menu()
