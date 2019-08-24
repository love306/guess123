import random
r = random.randint(1, 100)

while True:
	
	g = input('猜數字')
	g = int(g)
	if g == r:
		print("猜對啦!賽耶!")
		break
	else:
		if g > r:
			print("比答案大")
		else:
			print("比答案小")
