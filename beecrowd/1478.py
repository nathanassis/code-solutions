while True:
    x = int(input())
    if x == 0:
        break

    for j in range(x):
        aux = False
        for k in range(j, 0, -1):
            if aux:
                print("{:>4}".format(k+1), end="")
            else:
                print("{:>3}".format(k+1), end="")
                aux = True
        for k in range(x-j):
            if aux:
                print("{:>4}".format(k+1), end="")
            else:
                print("{:>3}".format(k+1), end="")
                aux = True
        print()
    print()
