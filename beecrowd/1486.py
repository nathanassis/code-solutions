def findToothpicks(list, size):
    cont, aux = 0, 0
    for i in list:
        if i == 1:
            aux += 1
            if aux == size:
                cont += 1
        else:
            aux = 0
    return cont
        

while True:
    points, meditions, minLength = list(map(int, input().split()))
    if points == meditions == minLength == 0:
        break

    am, cont = [], 0
    for i in range(meditions):
        am.append(list(map(int, input().split())))
    am = zip(*am)

    for i in am:
        cont += findToothpicks(i, minLength)
    
    print(cont)
    