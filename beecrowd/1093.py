while True:
	ev1, ev2, at, d = map(int, input().split())
	op1, op2 = 0, 0
	if ev1 == ev2 == at == d == 0:
		break
	
	while(ev1 > 0):
		ev1 -= d
		op1 += 1
		
	while(ev2 > 0):
		ev2 -= d
		op2 += 1
		
	if(at == 3):
		print("{:.1f}".format((op1 / (op1+op2)) * 100))
	else:
		aux = 1 - (6-at) / 6
		aux = (1-aux) / aux
		print("{:.1f}".format((1 - aux**op1) / (1 - aux**(op1+op2)) * 100))
