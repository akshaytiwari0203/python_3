from random import randint
print("...ROCK...")
print("...PAPER...")
print("...SCISSORS...")

plr1_choice=input("Enter your choice: ")

comp_choice_int=randint(0,2)

if comp_choice_int == 0:
	comp_choice = "ROCK"
elif comp_choice_int == 1:
	comp_choice = "PAPER"
elif comp_choice_int == 2:
	comp_choice = "SCISSORS"
else:
	print("System Error...")

print(f"Computer choice is {comp_choice}")

print("SHOOT")

if plr1_choice==comp_choice:
	print("It's a draw")
elif plr1_choice=="ROCK" and comp_choice=="PAPER":
	print("Computer wins!!!")
elif plr1_choice=="ROCK" and comp_choice=="SCISSORS":
	print("Player 1 wins!!!")
elif plr1_choice=="PAPER" and comp_choice=="SCISSORS":
	print("Computer wins!!!")
elif plr1_choice=="PAPER" and comp_choice=="ROCK":
	print("Player 1 wins!!!")
elif plr1_choice=="SCISSORS" and comp_choice=="ROCK":
	print("Computer wins!!!")
elif plr1_choice=="SCISSORS" and comp_choice=="PAPER":
	print("Player 1 wins!!!")
else:
	print("Not a valid input!!!")



