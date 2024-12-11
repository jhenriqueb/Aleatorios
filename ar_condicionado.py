class ar_condicionado:
    def __init__(self, temp_min=16, temp_max=30, vel_min=1, vel_max=3):
        self._temp_min = temp_min
        self._temp_max = temp_max
        self._vel_min = vel_min
        self._vel_max = vel_max
        self._temperatura = temp_min
        self._velocidade = vel_min
        self._modo = 'automático'
        self._ligado = False

    # Métodos getters e setters
    @property
    def temp_min(self):
        return self._temp_min

    @property
    def temp_max(self):
        return self._temp_max

    @property
    def vel_min(self):
        return self._vel_min

    @property
    def vel_max(self):
        return self._vel_max

    @property
    def temperatura(self):
        return self._temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if self._temp_min <= valor <= self._temp_max:
            self._temperatura = valor

    @property
    def velocidade(self):
        return self._velocidade

    @velocidade.setter
    def velocidade(self, valor):
        if self._vel_min <= valor <= self._vel_max:
            self._velocidade = valor

    @property
    def modo(self):
        return self._modo

    @modo.setter
    def modo(self, valor):
        if valor in ['automático', 'frio', 'ventilar']:
            self._modo = valor
            if valor == 'automático':
                self._velocidade = self._vel_min

    @property
    def ligado(self):
        return self._ligado

    def ligar(self):
        self._ligado = True

    def desligar(self):
        self._ligado = False

    def aumentar_temperatura(self):
        if not self._ligado:
            return 'AR DESLIGADO'
        if self._temperatura < self._temp_max:
            self._temperatura += 1

    def diminuir_temperatura(self):
        if not self._ligado:
            return 'AR DESLIGADO'
        if self._temperatura > self._temp_min:
            self._temperatura -= 1

    def aumentar_velocidade(self):
        if not self._ligado:
            return 'AR DESLIGADO'
        if self._modo != 'automático' and self._velocidade < self._vel_max:
            self._velocidade += 1

    def diminuir_velocidade(self):
        if not self._ligado:
            return 'AR DESLIGADO'
        if self._modo != 'automático' and self._velocidade > self._vel_min:
            self._velocidade -= 1

    def mudar_modo(self, modo):
        self.modo = modo

    def __str__(self):
        estado = (
            f"Ligado: {'Sim' if self._ligado else 'Não'}\n"
            f"Temperatura: {self._temperatura}\n"
            f"Velocidade: {self._velocidade}\n"
            f"Modo: {self._modo}"
        )
        return estado

#---------------------------------------------------------------------------------------------------------------

# Testes dos métodos

def testar_metodos():
    ar = ar_condicionado()

    print("Teste 1: Estado inicial")
    print(ar)

    print("\nTeste 2: Ligar o ar-condicionado")
    ar.ligar()
    print(ar)

    print("\nTeste 3: Aumentar temperatura")
    resultado = ar.aumentar_temperatura()
    if resultado:
        print(resultado)
    print(ar)

    print("\nTeste 4: Diminuir temperatura")
    resultado = ar.diminuir_temperatura()
    if resultado:
        print(resultado)
    print(ar)

    print("\nTeste 5: Mudar para modo 'frio'")
    ar.mudar_modo('frio')
    print(ar)

    print("\nTeste 6: Aumentar velocidade")
    resultado = ar.aumentar_velocidade()
    if resultado:
        print(resultado)
    print(ar)

    print("\nTeste 7: Desligar o ar-condicionado")
    ar.desligar()
    print(ar)

# Executar testes
if __name__ == "__main__":
    testar_metodos()
