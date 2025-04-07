from datetime import datetime
from database import (
    conectar, cadastrar_cliente, cadastrar_servico, criar_tabelas,  listar_servicos, listar_agendamentos,agendar_horario, atualizar_status_agendamento, atualizar_tabela_agendamentos
)


def validar_data_hora(data_hora):
    try:
        data_hora_obj = datetime.strptime(data_hora, "%d/%m/%Y %H:%M")
        return True, data_hora_obj
    except ValueError:
        return False, "Formato de data/hora inválido. Use DD/MM/AAAA HH:MM"


def main():
    atualizar_tabela_agendamentos()  
    criar_tabelas()
    while True:
        print("\n--- Barber House ---")
        print("1. Cadastrar cliente")
        print("2. Cadastrar serviço")
        print("3. Agendar horário")
        print("4. Listar agendamentos")
        print("5. Atualizar status do agendamento")
        print("6. Sair")
        opcao = input("Escolha uma das opções: ")

        if opcao == "1":
            nome = input("Nome do cliente: ")
            sobrenome = input("Sobrenome do cliente: ")
            id_cliente = cadastrar_cliente(nome, sobrenome)
            if id_cliente:
                print(f"Cliente cadastrado com ID: {id_cliente}")
        elif opcao == "2":
            nome_servico = input("Nome do serviço: ")
            preco_servico = float(input("Preço do serviço: "))
            cadastrar_servico(nome_servico, preco_servico)
        elif opcao == "3":
            id_cliente = int(input("ID do cliente: "))
            servicos = listar_servicos()
            if not servicos:
                print("Nenhum serviço foi cadastrado")
                continue
            print("\n-- Serviços Disponíveis --")
            for servico in servicos:
                print(f"{servico[0]} - {servico[1]} (R${servico[2]:.2f})")
            servico_id = int(input("Escolha o ID do serviço: "))
            data_hora = input("Digite a data e hora do agendamento (formato: DD/MM/AAAA HH:MM): ")
            valido, resposta = validar_data_hora(data_hora)
            if not valido:
                print(resposta)
            else:
                agendar_horario(id_cliente, servico_id, resposta.strftime("%Y-%m-%d %H:%M"))
        elif opcao == "4":
            agendamentos = listar_agendamentos()
            if not agendamentos:
                print("Nenhum agendamento encontrado.")
            else:
                print("\n--- Agendamentos ---")
                for agendamento in agendamentos:
                    print(f"ID: {agendamento[0]} | Cliente: {agendamento[1]} {agendamento[2]} | Serviço: {agendamento[3]} (R${agendamento[4]:.2f}) | Status: {agendamento[5]} | Data/Hora: {agendamento[6]}")
        elif opcao == "5":
            agendamento_id = input("ID do agendamento: ")
            novo_status = input("Novo status (pendente/concluído/cancelado): ")
            if novo_status not in ["pendente", "concluído", "cancelado"]:
                print("Status inválido")
            else:
                atualizar_status_agendamento(agendamento_id, novo_status)
        elif opcao == "6":
            print("Saindo do sistema")
            break
        else:
            print("Opção inválida. Tente novamente")

if __name__ == "__main__":
    main()