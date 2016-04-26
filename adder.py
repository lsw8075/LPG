
while True: 

	a = int(input("Input 1st number:"))
	b = int(input("Input 2nd number:"))
 	
	if a == 0 and b == 0:
		break
	
	print(a, "+", b, "=", a+b)
	print(a, "-", b, "=", a-b)
	print(a, "*", b, "=", a*b)
	if b != 0 :
		print(a, "/", b, "=", a/b)
		print(a, "%", b, "=", a%b)
	print(a, "**", b, "=", a**b)


