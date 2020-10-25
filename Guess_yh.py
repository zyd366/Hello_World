#使用random.randint(开始，结束)，生成随机整数#
import random
number = random.randint(1,99)
#利用函数input，提示用户输入数字#
message = "Please enter the number you guessed:\n"
message +="Enter 'quit' to end the program.\n"
print(message)
guess = 0
k = 0
while 1:
	userInput = input()
	k = k+1
	if userInput == 'quit':#输入quit结束游戏#
		break
	elif userInput.isnumeric():#判断是否为数字
		guess=int(userInput)#字符串的比较和int值类型不同
		if guess<1 or guess>99:#判断输入范围
			print ("Is not a valid value,Please enter the number you guessed from 1~99,or enter 'quit' to end the program.")
			continue
		elif guess > number:
			print ("Too big ,please try again.")
		elif guess < number:
			print ("Too small ,please try again.")
		else:
			print("Congratulations! You guessed right.\nYou've guessed " + str(k) +" times.")
			break
	else:
		print ("Is not a valid value,Please enter the number you guessed from 1~99,or enter 'quit' to end the program.")
