soma=0
op=input()

for i in range(84):
    input()

for i in range(5,0,-1):
    for j in range(i):
        input()
        
    for j in range(12 - i*2):
        soma+=float(input())
    
    for j in range(i):
        input()



print("{:.1f}".format(soma) if op == 'S' else "{:.1f}".format(soma/30))