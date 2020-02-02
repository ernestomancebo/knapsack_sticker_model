from modelo_sticker import fill_weight, mezclar
from cardinal_sort import cardinal_sort
from pararell_fill import paralell_fill


def bounded_knapsack(p, w, phi, k, k_1):
    q_w = fill_weight(1, p)
    q_phi = fill_weight(1, p, phi)
    t_0 = []  # build library
    t_0 = paralell_fill(t_0, [], None, p + 1, p + q_w)
    t_0 = cardinal_sort(t_0, p+1, p+q_w)
    t_1 = []

    for i in range(1, k+1):
        t_1 = mezclar(t_1, cardinal_sort(t_0, p+1, q+qw)[i])

    t_0 = paralell_fill(t_1, phi, p, q_w)
    t_0 = cardinal_sort(t_0, p+q_w + 1, p+q_w, q_phi)
    t_1 = []
    for i in range(k_1, q_phi + 1):
        t_1 = mezclar(t_1, cardinal_sort(t_0, p + q_w + 1, p+q_w + q_phi)[i])

    return t_1
