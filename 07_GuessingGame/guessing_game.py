from random import randint

selected_num=randint(1,10)


answer = None;

while True :
	answer = input("Guess the number. Enter q to quit: ")
	if answer == 'q':
		print("You lost")
		break
	else:
		answer = int(answer)
		if answer == selected_num:
			print("Correct")
			break
		elif answer > selected_num:
			print("Your guess is on higher side")
		else:
			print("Your guess is on lower side")
