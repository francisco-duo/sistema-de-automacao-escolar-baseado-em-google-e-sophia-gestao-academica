import os
import time


def inicio_letivo():
    """Função para iniciar o ano ou semestre letivo."""
    print("\n==== Início do Ano/Semestre Letivo ====")
    print("Preparando ambiente para o início do ano/semestre letivo...")
    time.sleep(2)
    print("-> Calendário atualizado!")
    print("-> Turmas configuradas!")
    print("-> Professores e alunos cadastrados!\n")


def gerenciar_emails():
    """Função para gerenciar emails."""
    print("\n==== Gerenciamento de Emails ====")
    print("Escolha uma ação:")
    print("1. Criar novos emails")
    print("2. Atualizar emails existentes")
    print("3. Excluir emails")
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        print("Criando novos emails...")
    elif opcao == "2":
        print("Atualizando emails existentes...")
    elif opcao == "3":
        print("Excluindo emails...")
    else:
        print("Opção inválida! Tente novamente.")
    time.sleep(1)
    print("Operação concluída.\n")


def gerenciar_grupos():
    """Função para gerenciar grupos."""
    print("\n==== Gerenciamento de Grupos ====")
    print("Escolha uma ação:")
    print("1. Criar grupos")
    print("2. Inserir emails em grupos")
    print("3. Remover emails de grupos")
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        print("Criando grupos...")
    elif opcao == "2":
        print("Inserindo emails em grupos...")
    elif opcao == "3":
        print("Removendo emails de grupos...")
    else:
        print("Opção inválida! Tente novamente.")
    time.sleep(1)
    print("Operação concluída.\n")


def menu():
    """Função principal do menu."""
    while True:
        os.system("clear" if os.name == "posix" else "cls")
        print("==== Menu Principal ====")
        print("1. Início do Ano/Semestre Letivo")
        print("2. Gerenciamento de Emails")
        print("3. Gerenciamento de Grupos")
        print("0. Sair")
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            inicio_letivo()
        elif opcao == "2":
            gerenciar_emails()
        elif opcao == "3":
            gerenciar_grupos()
        elif opcao == "0":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")
        input("Pressione Enter para voltar ao menu...")


if __name__ == "__main__":
    menu()
