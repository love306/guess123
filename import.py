import random
r = random.randint(1, 100)
count = 0
while True:
	
	g = input('猜數字')
	g = int(g)
	count +=  1
	if g == r:
		print("猜對啦!賽耶!")
		print('猜', count,'次')
		break
	else:
		if g > r:
			print("比答案大")
		else:
			print("比答案小")
		print('猜', count,'次')
