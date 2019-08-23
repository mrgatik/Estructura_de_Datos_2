#Las Torres de Hanoi 
#origen, auxiliar, destino
def imprime_movimiento(origen, destino):
    print("mueve desde " + str(origen) + " a " + str(destino))

# origen: front, destino, auxiliar
def torres(n, origen, destino, auxiliar):
    if n == 1:
        imprime_movimiento(origen, destino)
    else:
        torres(n-1, origen, auxiliar, destino)
        torres(1, origen, destino, auxiliar)
        torres(n-1, auxiliar, destino, origen)

torres(5, "o", "d", "a");
