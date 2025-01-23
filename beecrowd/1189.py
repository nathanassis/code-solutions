soma=0
op=input()

for i in range(6):
    for j in range(i):
        soma+=float(input())
    for j in range(12-i):
        input()

for i in range(5,0,-1):
    for j in range(i):
        soma+=float(input())
    for j in range(12-i):
        input()

for i in range(12):
    input()

print("{:.1f}".format(soma) if op == 'S' else "{:.1f}".format(soma/30))