def colorear(i: int, colorCandidato: int):
    global adyacentes, paises, n

    for adyacente in adyacentes[i]:
        if paises[adyacente] == colorCandidato:
            return False
    return True


def pintarMapa(coloresDisponibles: int, i: int = 1):
    global paises

    for col in range(1, coloresDisponibles+1):
        if colorear(i, col):
            paises[i] = col

            if i == n-1:
                return True
            else:
                if pintarMapa(coloresDisponibles, i+1):
                    return True

    paises[i] = 0
    return False


casos = int(input())

for _ in range(casos):
    adyacentes = []
    fronterasMaximas = 0

    n = int(input())

    for i in range(n):
        listaAdyacentes = []
        linea = input().split()

        for j in range(0, i, 1):
            if linea[j] == '1':
                listaAdyacentes.append(j)

        adyacentes.append(listaAdyacentes)

        if fronterasMaximas < len(listaAdyacentes):
            fronterasMaximas = len(listaAdyacentes)

    if fronterasMaximas > 0:
        paises = [1]
        paises.extend([0]*(n-1))

        for colores in range(2, n+1):
            if pintarMapa(colores):
                print(colores)
                break
    else:
        print(1)
