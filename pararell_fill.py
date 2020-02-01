from modelo_sticker import separar, encender, mezclar


def paralell_fill(tubo: list, A: list, f, p: int, r):
    t_tmp = tubo[:]
    for i in range(1, p):
        (t_pos, t_neg) = separar(t_tmp, i)
        for j in range(1, f(i)):
            bit = p + r + j + f(A[i-1])
            t_pos = encender(t_pos, bit)
        t_tmp = mezclar(t_pos, t_neg)
    return t_tmp[p]
