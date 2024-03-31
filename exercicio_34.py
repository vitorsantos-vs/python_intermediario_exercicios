print("Escreva um programa que resolva um sistema de equações lineares usando a regra de Cramer.\n")

import numpy as np

def regra_cremer(A, B):
    det_A = np.linalg.det(A)
    if det_A == 0:
        return "O sistema não tem solução única"
    else:
        n = len(A)
        x = np.zeros(n)
        for i in range(n):
            temp_A = A.copy()
            temp_A[:, i] = B
            x[i] = np.linalg.det(temp_A) / det_A
        return x
    
A = np.array([[2, -1], [5, 3]])
B = np.array([1, 9])

solucao = regra_cremer(A, B)
print(f"A solução do sistema é {solucao}")
