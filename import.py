import random
start = input('請決定最小值')
end = input('請決定最大值')
start = int(start)
end = int(end)
r = random.randint(start, end)
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
