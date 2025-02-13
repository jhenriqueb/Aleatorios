from restaurante import Restaurante, Cliente, Prato, Bebida, TamanhoBebida
PRATOS = [
    Prato("1. Feijoada", 45.0, 30),
    Prato("2. Filé à Parmegiana", 55.0, 25),
    Prato("3. Salmão Grelhado", 65.0, 20),
    Prato("4. Lasanha", 40.0, 25),
    Prato("5. Risoto de Camarão", 58.0, 30)
]

BEBIDAS = [
    Bebida("1. Coca-Cola", 8.0, TamanhoBebida.M),
    Bebida("2. Suco de Laranja", 10.0, TamanhoBebida.M),
    Bebida("3. Água Mineral", 5.0, TamanhoBebida.M),
    Bebida("4. Cerveja", 12.0, TamanhoBebida.M),
    Bebida("5. Vinho Tinto", 40.0, TamanhoBebida.M)
]

def mostrar_menu():
    print("\n=== Menu de Opções ===")
    print("1. Adicionar mesa")
    print("2. Fazer pedido")
    print("3. Ver conta de uma mesa")
    print("4. Ver mesas ocupadas")
    print("5. Sair")
    return input("Escolha uma opção: ")

def mostrar_cardapio_pratos():
    print("\n=== Cardápio de Pratos ===")
    for prato in PRATOS:
        print(f"{prato.nome} - R$ {prato.preco_base:.2f} (Tempo: {prato.tempo_preparo} min)")

def mostrar_cardapio_bebidas():
    print("\n=== Cardápio de Bebidas ===")
    for bebida in BEBIDAS:
        print(f"{bebida.nome} - R$ {bebida.preco_base:.2f}")

def criar_pedido():
    nome_cliente = input("Nome do cliente: ")
    cliente = Cliente(nome_cliente)
    
    itens = []
    while True:
        print("\nTipo de item:")
        print("1. Prato")
        print("2. Bebida")
        print("3. Finalizar pedido")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "3":
            break
            
        if opcao == "1":
            mostrar_cardapio_pratos()
            try:
                escolha = int(input("\nEscolha o número do prato (1-5): ")) - 1
                if 0 <= escolha < len(PRATOS):
                    itens.append(PRATOS[escolha])
                else:
                    print("Opção inválida!")
            except ValueError:
                print("Por favor, digite um número válido!")
            
        elif opcao == "2":
            mostrar_cardapio_bebidas()
            try:
                escolha = int(input("\nEscolha o número da bebida (1-5): ")) - 1
                if 0 <= escolha < len(BEBIDAS):
                    print("\nEscolha o tamanho:")
                    print("1. Pequeno (P)")
                    print("2. Médio (M)")
                    print("3. Grande (G)")
                    
                    tamanho_opcao = input("Opção: ")
                    tamanho = {
                        "1": TamanhoBebida.P,
                        "2": TamanhoBebida.M,
                        "3": TamanhoBebida.G
                    }.get(tamanho_opcao)
                    
                    if tamanho:
                        bebida = BEBIDAS[escolha]
                        nova_bebida = Bebida(bebida.nome.split(". ")[1], bebida.preco_base, tamanho)
                        itens.append(nova_bebida)
                    else:
                        print("Tamanho inválido!")
                else:
                    print("Opção inválida!")
            except ValueError:
                print("Por favor, digite um número válido!")
    
    return cliente, itens

def main():
    restaurante = Restaurante()
    
    while True:
        opcao = mostrar_menu()
        
        if opcao == "1":
            numero = int(input("Número da mesa: "))
            restaurante.adicionar_mesa(numero)
            
        elif opcao == "2":
            if not restaurante.mesas:
                print("\nNão há mesas cadastradas!")
                continue
                
            print("\nMesas disponíveis:", [mesa.numero for mesa in restaurante.mesas])
            numero_mesa = int(input("Número da mesa para o pedido: "))
            
            mesa = next((mesa for mesa in restaurante.mesas if mesa.numero == numero_mesa), None)
            if mesa:
                cliente, itens = criar_pedido()
                mesa.registrar_pedido(cliente, itens)
            else:
                print("\nMesa não encontrada!")
                
        elif opcao == "3":
            numero_mesa = int(input("Número da mesa: "))
            mesa = next((mesa for mesa in restaurante.mesas if mesa.numero == numero_mesa), None)
            if mesa:
                print(mesa.imprimir_conta())
                
                if mesa.pedidos:
                    finalizar = input("\nDeseja finalizar o pedido? (S/N): ").upper()
                    if finalizar == 'S':
                        mesa.pedidos.clear()
                        print(f"\nPedido da mesa {numero_mesa} finalizado com sucesso!")
                    elif finalizar == 'N':
                        print("\nPedido mantido em aberto.")
                    else:
                        print("\nOpção inválida! Pedido mantido em aberto.")
            else:
                print("\nMesa não encontrada!")
                
        elif opcao == "4":
            mesas_ocupadas = restaurante.listar_mesas_ocupadas()
            if mesas_ocupadas:
                print("\nMesas ocupadas:", [mesa.numero for mesa in mesas_ocupadas])
            else:
                print("\nNão há mesas ocupadas!")
                
        elif opcao == "5":
            print("\nEncerrando o programa...")
            break
            
        else:
            print("\nOpção inválida!")

if __name__ == "__main__":
    main()