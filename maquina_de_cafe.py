class MaquinaDeCafe:
    def __init__(self, capacidade_reservatorio=1000):
        self._nivel_agua = 0  # Inicialmente sem água
        self._capacidade_reservatorio = capacidade_reservatorio  # Capacidade máxima
        self._tipo_cafe = None  # Nenhum tipo selecionado
        self._temperatura = 25  # Temperatura ambiente inicial
        self._ligado = False

    # Encapsulamento dos atributos
    @property
    def nivel_agua(self):
        return self._nivel_agua

    @property
    def capacidade_reservatorio(self):
        return self._capacidade_reservatorio

    @property
    def tipo_cafe(self):
        return self._tipo_cafe

    @tipo_cafe.setter
    def tipo_cafe(self, tipo):
        if tipo in ["expresso", "cappuccino", "latte"]:
            self._tipo_cafe = tipo
        else:
            raise ValueError("Tipo de café inválido. Escolha entre expresso, cappuccino ou latte.")

    @property
    def temperatura(self):
        return self._temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if 70 <= valor <= 100:
            self._temperatura = valor
        else:
            raise ValueError("A temperatura deve estar entre 70 e 100 graus Celsius.")

    @property
    def ligado(self):
        return self._ligado

    # Métodos da máquina
    def ligar(self):
        self._ligado = True

    def desligar(self):
        self._ligado = False

    def adicionar_agua(self, quantidade):
        if quantidade < 0:
            raise ValueError("A quantidade de água não pode ser negativa.")
        if self._nivel_agua + quantidade <= self._capacidade_reservatorio:
            self._nivel_agua += quantidade
        else:
            self._nivel_agua = self._capacidade_reservatorio

    def aquecer_agua(self, temperatura):
        if not self._ligado:
            raise RuntimeError("A máquina deve estar ligada para aquecer a água.")
        self.temperatura = temperatura

    def selecionar_tipo(self, tipo):
        if not self._ligado:
            raise RuntimeError("A máquina deve estar ligada para selecionar o tipo de café.")
        self.tipo_cafe = tipo

    def preparar_cafe(self):
        if not self._ligado:
            return "A máquina está desligada. Ligue a máquina primeiro."
        if self._nivel_agua < 200:
            return "Água insuficiente para preparar o café."
        if self._temperatura < 70:
            return "A água não está quente o suficiente para preparar o café."
        if not self._tipo_cafe:
            return "Nenhum tipo de café foi selecionado."

        self._nivel_agua -= 200  # Consome 200ml de água para preparar o café
        return f"Seu {self._tipo_cafe} está pronto! Aproveite!"

    def estado_atual(self):
        estado = (
            f"Ligado: {'Sim' if self._ligado else 'Não'}\n"
            f"Nível de água: {self._nivel_agua}ml\n"
            f"Capacidade do reservatório: {self._capacidade_reservatorio}ml\n"
            f"Temperatura: {self._temperatura}°C\n"
            f"Tipo de café: {self._tipo_cafe if self._tipo_cafe else 'Nenhum'}\n"
        )
        return estado

# Testes da classe
if __name__ == "__main__":
    # Criação de objetos
    maquina1 = MaquinaDeCafe()
    maquina2 = MaquinaDeCafe(capacidade_reservatorio=1500)
    maquina3 = MaquinaDeCafe(capacidade_reservatorio=800)

    # Imprimir estados iniciais
    print("Estado inicial da Máquina 1:\n", maquina1.estado_atual())
    print("\nEstado inicial da Máquina 2:\n", maquina2.estado_atual())
    print("\nEstado inicial da Máquina 3:\n", maquina3.estado_atual())

    # Simular uso da máquina 1
    maquina1.ligar()
    maquina1.adicionar_agua(500)
    maquina1.aquecer_agua(90)
    maquina1.selecionar_tipo("expresso")
    print("\nPreparando café na Máquina 1:", maquina1.preparar_cafe())
    print(maquina1.estado_atual())

    # Simular uso da máquina 2
    maquina2.ligar()
    maquina2.adicionar_agua(1000)
    maquina2.aquecer_agua(95)
    maquina2.selecionar_tipo("cappuccino")
    print("\nPreparando café na Máquina 2:", maquina2.preparar_cafe())
    print(maquina2.estado_atual())

    # Simular uso da máquina 3
    maquina3.ligar()
    maquina3.adicionar_agua(200)
    maquina3.aquecer_agua(85)
    maquina3.selecionar_tipo("latte")
    print("\nPreparando café na Máquina 3:", maquina3.preparar_cafe())
    print(maquina3.estado_atual())
