while True:
	try:
		qt, msg = int(input()), ""
		n = input().split(" + ")
		
		for i in range(qt):
			l = list(map(int, n[i].split("x")))
			msg += str(l[0]*l[1]) + "x"
			if l[1] - 1 != 1:
				msg += str(l[1]-1)
			if i < qt - 1:
				msg += " + "
		
		print(msg)
		
	except EOFError:
		break
