n = list(map(int, input().split()))

if n[0]*3 + n[1] > n[3]*3 + n[4] or n[0]*3 + n[1] == n[3]*3 + n[4] and n[2] > n[5]:
	print("C")
elif n[0]*3 + n[1] < n[3]*3 + n[4] or n[0]*3 + n[1] == n[3]*3 + n[4] and n[2] < n[5]:
	print("F")
else:
	print("=")
