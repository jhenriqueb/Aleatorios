from typing import List
from dataclasses import dataclass
from enum import Enum

# Definimos um Enum para representar tamanhos de bebida
class TamanhoBebida(Enum):
    P = "P"
    M = "M"
    G = "G"

# Classe base para os itens do menu
class ItemMenu:
    def __init__(self, nome: str, preco_base: float):
        # Inicializa o nome e o preço base do item
        self.nome = nome
        self.preco_base = preco_base

    def calcular_preco(self) -> float:
        # Retorna o preço base do item
        return self.preco_base

# Classe para representar pratos, herdando de ItemMenu
class Prato(ItemMenu):
    def __init__(self, nome: str, preco_base: float, tempo_preparo: int):
        # Inicializa o prato com nome, preço base e tempo de preparo
        super().__init__(nome, preco_base)
        self.tempo_preparo = tempo_preparo

    def calcular_preco(self) -> float:
        # Poderia adicionar lógica específica para cálculo de preço de pratos
        return self.preco_base

# Classe para representar bebidas, herdando de ItemMenu
class Bebida(ItemMenu):
    def __init__(self, nome: str, preco_base: float, tamanho: TamanhoBebida):
        # Inicializa a bebida com nome, preço base e tamanho
        super().__init__(nome, preco_base)
        self.tamanho = tamanho

    def calcular_preco(self) -> float:
        # Ajusta o preço baseado no tamanho da bebida
        multiplicadores = {
            TamanhoBebida.P: 1.0,  # Sem ajuste para tamanho P
            TamanhoBebida.M: 1.3,  # Ajuste de 30% para tamanho M
            TamanhoBebida.G: 1.5   # Ajuste de 50% para tamanho G
        }
        return self.preco_base * multiplicadores[self.tamanho]

# Classe para representar clientes usando dataclass para simplificar a criação da classe
@dataclass
class Cliente:
    nome: str

# Classe para representar pedidos feitos pelos clientes
class Pedido:
    def __init__(self, cliente: Cliente, itens: List[ItemMenu]):
        # Inicializa o pedido com o cliente e a lista de itens do menu
        self.cliente = cliente
        self.itens = itens

    def calcular_total(self) -> float:
        # Calcula o total do pedido somando os preços de todos os itens
        return sum(item.calcular_preco() for item in self.itens)

    def exibir_itens(self) -> str:
        # Cria uma string para exibir os itens do pedido
        resultado = f"\nCliente {self.cliente.nome} fez um pedido:"
        for item in self.itens:
            if isinstance(item, Prato):
                resultado += f"\n- Prato: {item.nome} (Tempo de preparo: {item.tempo_preparo} min) - R$ {item.calcular_preco():.2f}"
            elif isinstance(item, Bebida):
                resultado += f"\n- Bebida: {item.nome} (Tamanho: {item.tamanho.value}) - R$ {item.calcular_preco():.2f}"
        return resultado

# Classe para representar mesas no restaurante
class Mesa:
    def __init__(self, numero: int):
        # Inicializa a mesa com um número e uma lista vazia de pedidos
        self.numero = numero
        self.pedidos: List[Pedido] = []

    def registrar_pedido(self, cliente: Cliente, itens: List[ItemMenu]):
        # Registra um novo pedido para a mesa e adiciona à lista de pedidos
        pedido = Pedido(cliente, itens)
        self.pedidos.append(pedido)
        print(pedido.exibir_itens())

    def calcular_total(self) -> float:
        # Calcula o total de todos os pedidos na mesa
        return sum(pedido.calcular_total() for pedido in self.pedidos)

    def imprimir_conta(self) -> str:
        # Cria uma string para exibir a conta da mesa
        resultado = f"\nResumo da mesa {self.numero}:"
        for pedido in self.pedidos:
            resultado += f"\n- {pedido.cliente.nome}: "
            itens_desc = []
            for item in pedido.itens:
                if isinstance(item, Prato):
                    itens_desc.append(f"{item.nome} (R$ {item.calcular_preco():.2f})")
                elif isinstance(item, Bebida):
                    itens_desc.append(f"{item.nome} {item.tamanho.value} (R$ {item.calcular_preco():.2f})")
            resultado += ", ".join(itens_desc)
        resultado += f"\nTotal: R$ {self.calcular_total():.2f}"
        return resultado

# Classe para representar o restaurante
class Restaurante:
    def __init__(self):
        # Inicializa o restaurante com uma lista vazia de mesas
        self.mesas: List[Mesa] = []

    def adicionar_mesa(self, numero: int):
        # Adiciona uma nova mesa ao restaurante
        mesa = Mesa(numero)
        self.mesas.append(mesa)
        print(f"Cadastrando mesa {numero}...")
        return mesa

    def listar_mesas_ocupadas(self) -> List[Mesa]:
        # Retorna uma lista de mesas que têm pedidos
        return [mesa for mesa in self.mesas if mesa.pedidos]
