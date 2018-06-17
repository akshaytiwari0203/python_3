exp_password = "hello"
input_password=input("Enter password: ")

wrong_password_limit = 3
wrong_password_count = 0


while input_password != exp_password:
	print("Wrong password!!!")
	wrong_password_count+=1
	if wrong_password_count == wrong_password_limit:
		break
	else:
		input_password = input("Enter password: ")


if wrong_password_count != wrong_password_limit:
	print("Correct password")