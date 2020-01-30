from random import randint
from modelo_sticker import generar_conjuntos, encode_tube
import pprint
import json

pp = pprint.PrettyPrinter(indent=4)
(A, B, F) = generar_conjuntos(randint(1, 12))
t_0 = encode_tube(A, F)

print(" A: {0} \n B: {1} \n F: {2} \n t_0: {3}".format(
    A, B, F, pp.pformat(t_0)))
