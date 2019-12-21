import random

r = random.randint(1,100)
while True:
	ge = input('請猜數字: ')
	ge = int(ge)
	if r == ge:
		print('恭喜猜對')
		break
	elif r > ge:
		print('比答案小')
	elif r < ge:
		print('比答案大')
	else:
		print('猜錯')