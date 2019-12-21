import random
start = input("請決定開始範圍： ")
end = input("請決定結束範圍： ")
start = int(start)
end = int(end)

num = 0
num = int(num)
r = random.randint(start,end)
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
