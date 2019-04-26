# code from @ani10030 on GitHub
a={'Name':'AAA','A/C':10,'Bal':100}
b={'Name':'BBB','A/C':11,'Bal':110}
c={'Name':'CCC','A/C':12,'Bal':120}
d={'Name':'DDD','A/C':13,'Bal':130}
e={'Name':'EEE','A/C':14,'Bal':140}
f={'Name':'FFF','A/C':15,'Bal':150}
g={'Name':'GGG','A/C':16,'Bal':160}
h={'Name':'HHH','A/C':17,'Bal':170}
i={'Name':'III','A/C':18,'Bal':180}
j={'Name':'JJJ','A/C':19,'Bal':190}

final={10:a,11:b,12:c,13:d,14:e,15:f,16:g,17:h,18:i,19:j}

x=True
y=True
z=False
print ('USERNAMES EXIST ONLY FROM 10-19')
print ('')
while x==True:
	try:
		usr=int (input("Enter your Username : "))
		pin=int (input("Enter your PIN : "))
		usr_no=int (final[usr]['A/C'])
		if (usr==usr_no & usr==pin):
			print("""
		Login Successful!""")
			y=True
			while y==True:
				print("""
		1. My Balance
		2. Make a Transfer
		3. Logout
		4. Logout and Exit
		""")
				try:
					login_option=int(input("Input one of the above options to proceed : "))
					if(login_option==1):
						print("""
		Current Available Balance : %d""" %(final[usr]['Bal']))

					elif(login_option==2):
						while y==True:
							transfer=int (input("Enter the amount of swipes to transfer : "))
							transfer_to=int (input("Enter the Username to whom amount has to be transferred : "))
							if(transfer_to not in final):
								print("""
		Invalid Username!""")
								continue
							if(transfer>int(final[usr]['Bal'])):
								print("""
		Not Enough Funds!
		Please try again...""")
								continue
							else:

								hello=final[usr]['Bal']-transfer
								hello2=final[transfer_to]['Bal']+transfer
								final[usr]['Bal']=hello
								final[transfer_to]['Bal']=hello2
								print("""
		TRANSACTION SUCCESSFUL!
		Your Available Swipes : %d""" %final[usr]['Bal'])
								break
					elif(login_option==3):
						print("""
		Successfully Logged out!
		Please Login Again
		""")		
						break
					elif(login_option==4):
						print("""
		Thank you and Good-Bye :)""")
						y=z
						x=z
				except:
					print("""
		Invalid Input! Please Try Again""")

		else:
			print("""
		Username and Password don't match!
			Please Try Again""")
	except:
		print("""
		x.Invalid Input! Please Try Again""")