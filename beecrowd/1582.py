while True:
	try:
		n = sorted(list(map(int, input().split())))
		msg = "tripla"
		if n[2]**2 == n[1]**2 + n[0]**2:
			msg += " pitagorica primitiva"
			aux = 2
			while aux <= n[0]:
				if n[2] % aux == 0 and n[1] % aux == 0 and n[1] % aux == 0:
					msg = msg.replace(" primitiva", "")
					break
				aux += 1

		print(msg)
	except EOFError:
		break
