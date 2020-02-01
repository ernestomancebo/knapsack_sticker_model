from modelo_sticker import generar_conjuntos, mezclar, separar


def cardinal_sort(tubo, B: list):
    s = len(B)
    tubo_salida = [list()] * (s + 1)
    t_prime = tubo_salida[:]
    tubo_salida[0] = tubo[:]

    for i in range(1, s + 1):
        b_index = i - 1
        (tubo_salida[0], t_prime[0]) = separar(tubo_salida[0], B[b_index])
        for j in range(0, i):
            (t_prime[j+1], t_double) = separar(tubo_salida[j], B[b_index])
            tubo_salida[j] = mezclar(t_prime[j], t_double)

        tubo_salida[i] = t_prime[i]
    return tubo_salida
