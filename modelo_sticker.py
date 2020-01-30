from random import randint


def mezclar(tubo_1, tubo_2):
    return tubo_1[:] + tubo_2[:]


def separar(tubo, indice):
    t_pos = tubo[:]
    t_neg = tubo[:]

    encender(t_pos, indice)
    apagar(t_neg, indice)

    return (t_pos, t_neg)


def manipular_sticker(tubo: list, indice: int, val: int):
    t_tmp = tubo[:]
    for m_complex in t_tmp:
        m_complex[indice] = val
    return t_tmp


def encender(tubo, indice):
    return manipular_sticker(tubo, indice, 1)


def apagar(tubo, indice):
    return manipular_sticker(tubo, indice, 0)


def leer(tubo):
    return tubo


def generar_conjuntos(p):
    # Tamaño de A. Incrementa en 1 pues la función
    # range es exclusiva respecto al límite superior.
    A = [x for x in range(0, p + 1)]

    # Tamaño de B, aleatoria pero dentro del dominio de A
    s = randint(1, p)
    B = set()
    for _ in range(s):
        B.add(A[randint(0, p)])

    # Tamaño de la famila de conjuntos de F
    t = p//2 or 1
    # Tamaño máximo de cada conjunto de F
    t_c = randint(1, t)

    F = list()
    for _ in range(t):
        s_i = set()
        for _ in range(randint(1, t_c)):
            s_i.add(A[randint(0, p)])
        F.append(s_i)
    return (A, B, F)


def encode_tube(A: list, F: list):
    tube_0 = list()
    a_range = range(0, len(A))
    for d in F:
        mem_complex = [0 for _ in a_range]
        mem_complex = x_d(mem_complex, d)
        tube_0.append(mem_complex)

    return tube_0


def x_d(mem_complex: list, d: list):
    for i in d:
        mem_complex[i] = 1
    return mem_complex
