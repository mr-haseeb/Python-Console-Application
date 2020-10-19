import subprocess
#subprocess.run(["ls", "-l"])
#subprocess.run(["sudo","su"])

#while True:
#    if keyboard.read_key() == "p":
#        print("You pressed p")
#        break

"""
This is Main Function for running file
two options to select here
"""

def main():
	print("*"*100)
	print("\t\t\t\t\tWelcome To My Project\n")
	print("\t\t 1) For Basic \n")
	print("\t\t 2) For Grocery Shoping\n")
	selection=int(input("Enter Your Selection Here_:"))
	print("*"*100)
	if(selection==1):
		basic_operations()
			
	elif(selection==2):
		print("your selection is second number")
			

def basic_operations():
	try:
		subprocess.run(["clear"])
		print("*"*100)
		print("\t\t\t\t\tWelcome To Basic Operations Section\n")
		print("\t\t 1) Check Type \n")
		print("\t\t 2) For Grocery Shoping\n")
		print("\t\t 3) For Basic \n")
		print("\t\t 4) For Grocery Shoping\n")
		print("\t\t 5) For Basic \n")
		print("\t\t 6) For Grocery Shoping\n")
		print("\t\t 7) For Basic \n")
		print("\t\t 8) For Grocery Shoping\n")
		print("\t\t 9) For Basic \n")
		print("\t\t 10) For Grocery Shoping\n")
		print("\t\t 11) For Basic \n")
		print("\t\t 12) For Grocery Shoping\n")
		
		selection=int(input("Enter Your Selection Here_:"))
		option_handler(selection)
	except:
		print("Wrong Selection Please Try Again")
		basic_operations()



def option_handler(selection):
	if selection==1:
	
		print(type(selection))
		print("Select Another Option ")
		char=input("Y or N___")
		if char=="y" or char=="Y":
			basic_operations()
			
		if char=="N" or char=="n":
		        pass
			
	
if __name__=='__main__':
	main()

