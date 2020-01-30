from modelo_sticker import generar_conjuntos, separar, mezclar
from random import randint

(A, B, F) = generar_conjuntos(randint(0, 10))


def cardinal_sort(tubo, B: set):
    t_0 = tubo[:]
    b_l = list(B)
    s = len(B)
    for i in range(1, s + 1):
        separar(t_0, b_l[i])
        for j in range(0, i):
            separar()
            mezclar()
        # T_i
    return t_0
