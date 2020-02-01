import pprint
from random import randint

from cardinal_sort import cardinal_sort
from modelo_sticker import encode_tube, generar_conjuntos

pp = pprint.PrettyPrinter(indent=4)

(A, B, F) = generar_conjuntos(randint(0, 10))

tube = encode_tube(A, F)
t_salida = cardinal_sort(tube, list(B))

print(" A: {0} \n B: {1} \n F: {2}".format(A, B, F))

print("t_0:")
pp.pprint(tube)

print("t_salida:")
pp.pprint(t_salida)
"""
worked

A: [0, 1] 
 B: {1} 
 F: [{0}] 
 t_0: [[1, 0]] 
 t_salida: [[[1, 0]], []]

test/traza

# A = [x for x in range(0, 7)]
# B = set()
# B.add(1)
# B.add(2)
# B.add(4)
# F = [[2, 6], [3], [4], [2, 4]]

# A = [x for x in range(0, 2)]
# B = set()
# B.add(0)
# F = [[0]]
"""
