import json
import os

# Nome do arquivo para armazenar o estoque
ESTOQUE_FILE = 'estoque.json'

def carregar_estoque():
    """Carrega o estoque de um arquivo JSON."""
    if os.path.exists(ESTOQUE_FILE):
        with open(ESTOQUE_FILE, 'r') as file:
            return json.load(file)
    return {}

def salvar_estoque(estoque):
    """função para os dados estoque em um arquivo JSON."""
    with open(ESTOQUE_FILE, 'w') as file:
        json.dump(estoque, file, indent=4)

def adicionar_item(estoque):
    """Adiciona um item ao estoque."""
    codigo = input("Digite o código do item: ")
    if codigo in estoque:
        print("Código já existente. Use a opção de edição para atualizar o item.")
        return

    nome = input("Digite o nome do item: ")
    quantidade = int(input("Digite a quantidade: "))
    estoque[codigo] = {'nome': nome, 'quantidade': quantidade}
    salvar_estoque(estoque)
    print(f"Item '{nome}' adicionado com sucesso.")

def visualizar_estoque(estoque):
    """Exibe todos os itens que estão cadastrados no estoque."""
    if not estoque:
        print("O estoque está vazio.")
        return
    print("Itens em estoque:")
    for codigo, dados in estoque.items():
        print(f"Código: {codigo}, Nome: {dados['nome']}, Quantidade: {dados ['quantidade']}")

def remover_item(estoque):
    """Remove o item qual for selecionado no estoque."""
    codigo = input("Digite o código do item a ser removido: ")
    if codigo in estoque:
        del estoque [codigo]
        salvar_estoque(estoque)
        print(f"Item com código '{codigo}' removido com sucesso.")
    else:
        print("Item não encontrado no estoque.")

def editar_item(estoque):
    """Edita o item qual for selecionado no estoque."""
    codigo = input("Digite o código do item a ser editado: ")
    if codigo not in estoque:
        print("Item não encontrado no estoque.")
        return

    print(f"Dados atuais - Nome: {estoque[codigo]['nome']}, Quantidade: {estoque[codigo]['quantidade']}")
    print("O que você deseja editar (Selecione a opcao conforme o numero)?")
    print("1. Nome")
    print("2. Quantidade")
    print("3. Código")
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        novo_nome = input("Digite o novo nome: ")
        estoque [codigo]['nome'] = novo_nome
    elif escolha == '2':
        nova_quantidade = int(input("Digite a nova quantidade: "))
        estoque [codigo]['quantidade'] = nova_quantidade
    elif escolha == '3':
        novo_codigo = input("Digite o novo código: ")
        if novo_codigo in estoque:
            print("Novo código já existe. Use outro código.")
            return
        estoque [novo_codigo] = estoque.pop(codigo)
    else:
        print("Opção inválida.")
        return

    salvar_estoque(estoque)
    print(f"Item com código '{codigo}' atualizado com sucesso.")

def menu():
    """Exibe o menu principal e executa a ação selecionada."""
    estoque = carregar_estoque()
    while True:
        print("\nMenu:")
        print("1. Adicionar Item")
        print("2. Visualizar Estoque")
        print("3. Remover Item")
        print("4. Editar Item")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            adicionar_item(estoque)
        elif escolha == '2':
            visualizar_estoque(estoque)
        elif escolha == '3':
            remover_item(estoque)
        elif escolha == '4':
            editar_item(estoque)
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
