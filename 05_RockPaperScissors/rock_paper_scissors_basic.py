print("...ROCK...")
print("...PAPER...")
print("...SCISSORS...")

plr1_choice=input("Enter player 1 choice: ")
print("********NO CHEATING***************\n" * 27)
plr2_choice=input("Enter player 2 choice: ")

print("SHOOT")

if plr1_choice==plr2_choice:
	print("It's a draw")
elif plr1_choice=="ROCK" and plr2_choice=="PAPER":
	print("Player 2 wins!!!")
elif plr1_choice=="ROCK" and plr2_choice=="SCISSORS":
	print("Player 1 wins!!!")
elif plr1_choice=="PAPER" and plr2_choice=="SCISSORS":
	print("Player 2 wins!!!")
elif plr1_choice=="PAPER" and plr2_choice=="ROCK":
	print("Player 1 wins!!!")
elif plr1_choice=="SCISSORS" and plr2_choice=="ROCK":
	print("Player 2 wins!!!")
elif plr1_choice=="SCISSORS" and plr2_choice=="PAPER":
	print("Player 1 wins!!!")
else:
	print("Not a valid input!!!")



