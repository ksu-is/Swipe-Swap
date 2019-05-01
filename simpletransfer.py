import sqlite3

#pulling from db here
#setting up variables
def getstudents():
	conn=sqlite3.connect("ksustudents.db")
	conn.row_factory = sqlite3.Row
	cur=conn.cursor()
	cur.execute("SELECT * FROM students")   #need to reformat table in sqlite maybe, getting error here
	#varStudents=cur.fetchall()
	varStudents = [dict(row) for row in cur.fetchall()]
	conn.close()
	return varStudents	
students = getstudents()

#print("Students[1] =",students[1])

def findName(name):
	for s in students:
		if s['name'].strip() == name:
			return s['ID']
	return "Not found."

def findID(ID):
	for s in students:
		if s['ID'] == int(ID):
			return s
	return "Not found."
#print("Carly = ",findID(111111))
#testName = input("Give a name of someone to find: ")
#print(findName(testName))
print(students)

x=True
z=False
print ('MUST BE A CURRENT STUDENT')
print ('')
while x==True:
	try:
		usrID = input("Enter your KSU ID: ")
		#print("ID received: >" + usrID + "<")
		student = findID(usrID)
		#print("Student is:",student)
		#pin=int (input("Enter your PIN: "))
		#usr_no=int (final[usr]['A/C'])
		if student != "Not found.":
			print("Login Successful, " + student["name"] + "!")
		
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
		Current Available Balance : %d""" (student[usrID]['Bal']))

					elif(login_option==2):
						while y==True:
							transfer=int (input("Enter the amount of swipes to transfer : "))
							transfer_to=int (input("Enter the Username to whom amount has to be transferred : "))
							if(transfer_to not in students):
								print("""
		Invalid Username!""")
								continue
							if(transfer>int(student['swipes'])):
								print("""
		Not Enough Funds!
		Please try again...""")
								continue
							else:

								hello=student[usrID]['Bal']-transfer
								hello2=student[transfer_to]['Bal']+transfer
								students[usr]['Bal']=hello
								students[transfer_to]['Bal']=hello2
								print("""
		TRANSACTION SUCCESSFUL!
		Your Available Swipes : %d""" (students[student]['Bal'])
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
		print("Invalid ID! Please Try Again.")
