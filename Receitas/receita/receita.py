receitas = {}

def adicionar_receita():
    nome = input("Digite o nome da receita: ").title()
    ingredientes = input("Digite os ingredientes (separe por vírgula): ")
    modo_preparo = input("Digite o modo de preparo: ")
    receitas[nome] = {
        "ingredientes": ingredientes,
        "modo_preparo": modo_preparo
    }
    print(f"\nReceita '{nome}' adicionada com sucesso!\n")

def listar_receitas():
    if not receitas:
        print("Nenhuma receita cadastrada ainda.\n")
    else:
        print("\n=== Receitas cadastradas ===")
        for nome in receitas:
            print(f"- {nome}")
        print()

def buscar_receita():
    nome = input("Digite o nome da receita que deseja ver: ").title()
    if nome in receitas:
        print(f"\nReceita: {nome}")
        print(f"Ingredientes: {receitas[nome]['ingredientes']}")
        print(f"Modo de preparo: {receitas[nome]['modo_preparo']}\n")
    else:
        print("Receita não encontrada.\n")

def menu():
    while True:
        print("=== Menu de Receitas ===")
        print("1. Adicionar receita")
        print("2. Listar receitas")
        print("3. Buscar receita")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_receita()
        elif opcao == "2":
            listar_receitas()
        elif opcao == "3":
            buscar_receita()
        elif opcao == "4":
            print("Saindo... até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")