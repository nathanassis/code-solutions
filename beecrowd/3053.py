n, pos = int(input()), input()

while n > 0:
	x = int(input())
	if x == 1:
		if pos == "A":
			pos = "B"
		elif pos == "B":
			pos = "A"
	elif x == 2:
		if pos == "B":
			pos = "C"
		elif pos == "C":
			pos = "B"
	else:
		if pos == "A":
			pos = "C"
		elif pos == "C":
			pos = "A"
	n -= 1
	
print(pos)
