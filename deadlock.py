def detectar_deadlock(E, A, C, R):
    num_processos = len(C)
    num_recursos = len(E)
    A_temp = A.copy()
    marcados = [False] * num_processos

    while True:
        progresso_feito = False

        for i in range(num_processos):
            if not marcados[i] and all(R[i][j] <= A_temp[j] for j in range(num_recursos)):
                # Atualiza recursos disponíveis com os recursos alocados pelo processo
                A_temp = [A_temp[j] + C[i][j] for j in range(num_recursos)]
                marcados[i] = True
                progresso_feito = True
                break

        if not progresso_feito:
            break

    if all(marcados):
        print("O sistema está em um estado seguro.")
    else:
        print("O sistema está em deadlock.")

# Exemplo de uso
E = [4, 2, 3, 1]  # Recursos existentes
A = [2, 1, 0, 0]  # Recursos disponíveis
C = [
    [0, 0, 1, 0],  # Alocação do Processo 0
    [2, 0, 0, 1],  # Alocação do Processo 1
    [1, 0, 1, 0]   # Alocação do Processo 2
]
R = [
    [2, 0, 0, 0],  # Necessidade do Processo 0
    [1, 0, 1, 0],  # Necessidade do Processo 1
    [2, 1, 0, 0]   # Necessidade do Processo 2
]

detectar_deadlock(E, A, C, R)
