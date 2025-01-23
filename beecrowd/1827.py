while True:
    try:
        tam = int(input())
        
        matriz = []
        for i in range(tam):
            matriz.append([0] * tam)
            matriz[i][i] = 2
            matriz[i][tam-i-1] = 3
        
        for i in range(int(tam/3), tam-int(tam/3)):
            for j in range(int(tam/3), tam-int(tam/3)):
                matriz[i][j] = 1
        
        matriz[int(tam/2)][int(tam/2)] = 4
        for i in range(tam):
            for j in range(tam):
                print(matriz[i][j], end="")
            print()
        print()
    except EOFError:
        break
