n, s = map(int, input().split())
m = s

while n > 0:
	s += int(input())
	if s < m:
		m = s
	n -= 1
	
print(m)
