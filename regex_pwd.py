import re 
while True:   
	password = input("Enter you password here : ")
	if (len(password)<8):
		print("Length of your password is less than 8")
	elif not re.search("[a-z]", password): 
		print("Atleast one lower case character is required")
	elif not re.search("[A-Z]", password): 
		print("Atleast one upper case character is required")
	elif not re.search("[0-9]", password): 
		print("Atleast one number is required")
	elif not re.search("[!@#$%^&*_]", password): 
		print("Atleast one special character frome '!@#$%^&*_' is required")
	elif re.search("\s", password): 
		print('White spaces not allowed')
	else: 
		print("Valid Password") 
		break
print("password checked successfully")