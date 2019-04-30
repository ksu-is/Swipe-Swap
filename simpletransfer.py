# code from @ani10030 on GitHub
a={'Bethany':'AAA','A/C':173401,'Bal':100}
b={'Tatum':'BBB','A/C':123456,'Bal':110}
c={'Kaylee':'CCC','A/C':899764,'Bal':120}
d={'Olivia':'DDD','A/C':987653,'Bal':130}
e={'Christian':'EEE','A/C':129867,'Bal':140}
f={'Garrett':'FFF','A/C':778354,'Bal':150}
g={'Carly':'GGG','A/C':111111,'Bal':160}
h={'David':'HHH','A/C':876309,'Bal':170}
i={'Emily':'III','A/C':585065,'Bal':180}
j={'Sydnee':'JJJ','A/C':790141,'Bal':190}

final={173401:a,123456:b,899764:c,987653:d,129867:e,778354:f,111111:g,876309:h,585065:i,790141:j}


#pulling from db here
#setting up variables
import sqlite3
conn=sqlite3.connect("ksustudents.db")
cur=conn.cursor()
cur.execute("SELECT * FROM Student ID")   #need to reformat table in sqlite maybe, getting error here
varID=cur.fetchall()
cur.execute("SELECT * FROM Student names")
varNames=cur.fetchall()
cur.execute("SELECT * FROM Available Swipes")
varSwipes=cur.fetchall()
cur.execute("SELECT * FROM Contact List")
varCL=cur.fetchall()
conn.close()	


x=True
y=True
z=False
print ('MUST BE A CURRENT STUDENT')
print ('')
while x==True:
	try:
		usr=int (input("Enter your KSU ID : "))
		pin=int (input("Enter your PIN: "))
		usr_no=int (final[usr]['A/C'])
		if (usr==usr_no & usr==pin):
			print("""
		Login Successful!""")
			y=True
			while y==True:
				print("""
		Hello KSU Owl! What would you like to do:		
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
		Thank you and Hooty Hoo ;)""")
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