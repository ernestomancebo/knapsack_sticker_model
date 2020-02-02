from cardinal_sort import cardinal_sort
from pararell_fill import paralell_fill
from modelo_sticker import fill_weight


def subset_sum(p, w, k):
    q_w = fill_weight(1, p)
    for i in range(1, p+1):
        q_w += w(i)
    t_0 = list()
    t_1 = paralell_fill(t_0, [], w, p, 0)
    t_out = cardinal_sort(t_1, p+1, p+q_w)[k]
    return t_out
