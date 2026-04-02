bank_details={ 543214321567 : "Siddharth"  ,  235627654321: "deekshith" , 987656785432 : "sai" ,  432216547822 : "harsha",  647839283767 : "nag"  }
User="admin"
Password="admin@123"
login_user=input("Enter user :")
password=input("Enter password:")
acct_no=int(input("Enter Acc No :"))
if login_user == User and password == Password :
	for x in bank_details :
		if acct_no == x :
			print("Acct No :",x,"Name :",bank_details[x])
else :
	print("Invalid user or password")










































































