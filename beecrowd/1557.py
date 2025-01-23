while True:
    x = int(input())
    if x == 0:
        break
    
    t1 = len(str(2 ** (2 * (x-1))))
    for i in range(x):
        for j in range(x):
            t2 = len(str(2**(i+j)))
            for k in range(t1 - t2):
                print(end=" ")
            if j != x-1:
                print(2**(i+j), end=" ")
            else:
                print(2**(i+j), end="")
        print()
    print()