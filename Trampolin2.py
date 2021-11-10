from sys import stdin, stdout


def main():
    casos = int(stdin.readline())
    for _ in range(0, casos):
        niños = int(stdin.readline())
        infoniños = []
        for _ in range(0, niños):
            infoniños.append({titulo: int(info) for titulo, info in zip(
                ['minuto', 'pataleta'], stdin.readline().strip().split())})
        infoniños.sort(reverse=True, key=lambda x: x['pataleta'])
        orden = [None for _ in range(0, niños)]
        minutosPataletas = 0
        for niño in infoniños:
            turno = niño['minuto']//10
            while True:
                if orden[turno] is not None:
                    turno -= 1
                else:
                    orden[turno] = niño
                    if turno < 0:
                        minutosPataletas += niño['pataleta']
                    break
        stdout.write(str(minutosPataletas)+'\n')


main()
