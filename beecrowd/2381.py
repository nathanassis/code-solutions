n, k = map(int, input().split())
nome = []

while n > 0:
	nome.append(input())
	n -= 1

nome.sort()
print(nome[k-1])
