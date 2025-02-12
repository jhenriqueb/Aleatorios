from restaurante import Restaurante, Cliente, Prato, Bebida, TamanhoBebida

def main():
    # Criando o restaurante
    restaurante = Restaurante()
    
    # Cadastrando mesas no restaurante
    mesa5 = restaurante.adicionar_mesa(5)  # Adiciona a mesa de número 5
    mesa7 = restaurante.adicionar_mesa(7)  # Adiciona a mesa de número 7
    
    # Criando pedidos para a mesa 5
    joao = Cliente("João")  # Cria um cliente chamado João
    hamburguer = Prato("Hambúrguer", 25.0, 15)  # Cria um prato Hambúrguer com preço 25.0 e tempo de preparo 15 minutos
    refrigerante = Bebida("Refrigerante", 8.0, TamanhoBebida.G)  # Cria uma bebida Refrigerante tamanho G com preço 8.0
    mesa5.registrar_pedido(joao, [hamburguer, refrigerante])  # Registra o pedido de João na mesa 5

    maria = Cliente("Maria")  # Cria uma cliente chamada Maria
    salada = Prato("Salada Caesar", 22.0, 10)  # Cria um prato Salada Caesar com preço 22.0 e tempo de preparo 10 minutos
    suco = Bebida("Suco Natural", 10.0, TamanhoBebida.M)  # Cria uma bebida Suco Natural tamanho M com preço 10.0
    mesa5.registrar_pedido(maria, [salada, suco])  # Registra o pedido de Maria na mesa 5
    
    # Criando pedido para a mesa 7
    pedro = Cliente("Pedro")  # Cria um cliente chamado Pedro
    file = Prato("Filé Mignon", 55.0, 30)  # Cria um prato Filé Mignon com preço 55.0 e tempo de preparo 30 minutos
    vinho = Bebida("Vinho Tinto", 40.0, TamanhoBebida.G)  # Cria uma bebida Vinho Tinto tamanho G com preço 40.0
    mesa7.registrar_pedido(pedro, [file, vinho])  # Registra o pedido de Pedro na mesa 7
    
    # Imprimindo contas das mesas
    print("\nCalculando total da conta...")
    print(mesa5.imprimir_conta())  # Imprime a conta da mesa 5
    print(mesa7.imprimir_conta())  # Imprime a conta da mesa 7

if __name__ == "__main__":
    main()  # Executa a função principal
