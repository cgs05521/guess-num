import random
num = 0
num = int(num)
r = random.randint(1,100)
while True:
	ge = input('請猜數字: ')
	ge = int(ge)
	num += 1
	if r == ge:
		print('恭喜猜對,總共猜',num,'次')
		break
	elif r > ge:
		print('比答案小')
	elif r < ge:
		print('比答案大')
	else:
		print('猜錯')
	print('這是你猜的第',num,'次')
