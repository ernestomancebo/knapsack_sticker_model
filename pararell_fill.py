from modelo_sticker import separar, encender, mezclar


def paralell_fill(tubo: list, A: list, f, p: int, r: int):
    t_tmp = tubo[:]
    for i in range(1, p + 1):
        (t_pos, t_neg) = separar(t_tmp[i], i)
        for j in range(1, f(i)):
            r_i = p + r + f(A[i-1]) + j
            t_pos = encender(t_pos, r_i)
        t_tmp[i] = mezclar(t_pos, t_neg)
    return t_tmp


def f_a(n: int):
    if n == 0:
        return 0
    return n + f_a(n - 1)


print(f_a(4))
