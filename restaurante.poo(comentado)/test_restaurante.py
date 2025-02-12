import pytest
from restaurante import Restaurante, Cliente, Prato, Bebida, TamanhoBebida

def test_criar_pedido():
    restaurante = Restaurante()  # Cria uma instância do restaurante
    mesa5 = restaurante.adicionar_mesa(5)  # Adiciona uma mesa de número 5 ao restaurante
    
    # Cria um cliente e itens para o pedido
    joao = Cliente("João")  # Cria um cliente chamado João
    hamburguer = Prato("Hambúrguer", 25.0, 15)  # Cria um prato Hambúrguer com preço 25.0 e tempo de preparo 15 minutos
    refrigerante = Bebida("Refrigerante", 8.0, TamanhoBebida.G)  # Cria uma bebida Refrigerante tamanho G com preço 8.0
    
    # Registra o pedido na mesa 5
    mesa5.registrar_pedido(joao, [hamburguer, refrigerante])
    
    # Verificações para garantir que o pedido foi registrado corretamente
    assert len(mesa5.pedidos) == 1  # Verifica se há um pedido registrado
    assert mesa5.calcular_total() == 37.0  # Verifica se o total da conta é 37.0 (25.0 + 8.0 * 1.5)

def test_multiplos_pedidos_mesma_mesa():
    restaurante = Restaurante()  # Cria uma instância do restaurante
    mesa5 = restaurante.adicionar_mesa(5)  # Adiciona uma mesa de número 5 ao restaurante
    
    # Primeiro cliente faz um pedido
    joao = Cliente("João")  # Cria um cliente chamado João
    hamburguer = Prato("Hambúrguer", 25.0, 15)  # Cria um prato Hambúrguer com preço 25.0 e tempo de preparo 15 minutos
    refrigerante = Bebida("Refrigerante", 8.0, TamanhoBebida.G)  # Cria uma bebida Refrigerante tamanho G com preço 8.0
    mesa5.registrar_pedido(joao, [hamburguer, refrigerante])  # Registra o pedido de João na mesa 5
    
    # Segundo cliente faz um pedido
    maria = Cliente("Maria")  # Cria uma cliente chamada Maria
    salada = Prato("Salada Caesar", 22.0, 10)  # Cria um prato Salada Caesar com preço 22.0 e tempo de preparo 10 minutos
    suco = Bebida("Suco Natural", 10.0, TamanhoBebida.M)  # Cria uma bebida Suco Natural tamanho M com preço 10.0
    mesa5.registrar_pedido(maria, [salada, suco])  # Registra o pedido de Maria na mesa 5
    
    # Verificações para garantir que ambos os pedidos foram registrados corretamente
    assert len(mesa5.pedidos) == 2  # Verifica se há dois pedidos registrados
    assert mesa5.calcular_total() == 72.0  # Verifica se o total da conta é 72.0 (25.0 + 8.0*1.5 + 22.0 + 10.0*1.3)

def test_bebida_diferentes_tamanhos():
    suco = Bebida("Suco", 10.0, TamanhoBebida.P)  # Cria uma bebida Suco tamanho P com preço 10.0
    assert suco.calcular_preco() == 10.0  # Verifica se o preço da bebida é 10.0
    
    suco_medio = Bebida("Suco", 10.0, TamanhoBebida.M)  # Cria uma bebida Suco tamanho M com preço 10.0
    assert suco_medio.calcular_preco() == 13.0  # Verifica se o preço da bebida é 13.0
    
    suco_grande = Bebida("Suco", 10.0, TamanhoBebida.G)  # Cria uma bebida Suco tamanho G com preço 10.0
    assert suco_grande.calcular_preco() == 15.0  # Verifica se o preço da bebida é 15.0

def test_listar_mesas_ocupadas():
    restaurante = Restaurante()  # Cria uma instância do restaurante
    mesa1 = restaurante.adicionar_mesa(1)  # Adiciona uma mesa de número 1 ao restaurante
    mesa2 = restaurante.adicionar_mesa(2)  # Adiciona uma mesa de número 2 ao restaurante
    
    joao = Cliente("João")  # Cria um cliente chamado João
    hamburguer = Prato("Hambúrguer", 25.0, 15)  # Cria um prato Hambúrguer com preço 25.0 e tempo de preparo 15 minutos
    mesa1.registrar_pedido(joao, [hamburguer])  # Registra o pedido de João na mesa 1
    
    mesas_ocupadas = restaurante.listar_mesas_ocupadas()  # Obtém a lista de mesas ocupadas
    assert len(mesas_ocupadas) == 1  # Verifica se há uma mesa ocupada
    assert mesas_ocupadas[0].numero == 1  # Verifica se a mesa ocupada é a mesa de número 1
