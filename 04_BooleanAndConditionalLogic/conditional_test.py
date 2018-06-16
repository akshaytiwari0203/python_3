
age_boy=int(input("Enter age of boy: "))
age_girl=int(input("Enter age of girl: "))


#Testing or
print("Checking if either of you is adult")
if age_girl>=18 or age_boy>=18:
	print("One of you is adult!!!")
else:
	print("You are not adults")


#Testing and
print("Checking if you are allowed to marry!!!")
if age_boy>=21 and age_girl>=18:
	print("You are allowed to marry each other")
elif age_boy>=21 and age_girl<18:
	print("Search another girl")
elif age_boy<21 and age_girl>=18:
	print("Search another boy")
else:
	print("You are not allowed to marry")
