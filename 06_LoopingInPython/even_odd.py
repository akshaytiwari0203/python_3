upperbound=int(input("Enter upperbound: "))


for i in range(1,upperbound):
	if i == 4 or i == 13:
		print(f"{i} is lucky" )
	elif i % 2 == 0 :
		print(f"{i} is even")
	else:
		print(f"{i} is odd")