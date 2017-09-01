# Encapsulates console prints.

''' 
Shows the principal menu.
'''
def menu():
	print("\nChoose an option:")
	print("	[1] - Use your own machine")
	print("	[2] - Load some built-in machine")
	print("	[3] - Exit\n")

'''
Shows the menu of chooses of the built-in machines.
'''
def examples_machines():
	print("\nLoad an example program:")
	print("")
	print("[1] - Binary to decimal conversion")
	print("[2] - Palindrome detector\n")

'''
Indicates what the user attempted to choose an invalid operation
'''
def invalid_operation():
	print("\nSomething is wrong...")
	print("... maybe you must try again choosing one of valid options\n")

'''
Ask if the user wants sees the step by step of a turing machine running
'''
def run_stepbystep():
	print("\nYou want see the step by step? [Y/N]")	
	
	run = False
	operation = raw_input()

	if (operation.lower() == 'y'):
		run = True
		print("\nType END to skip step by step \n")
		print("Running step-by-step...\n")

	return run

def machines_not_found():
	print "\nOps!! No machines here. \nFor more information see README.md"

'''
Ask to the user if it's time to close the program
'''
def interrupted_execution():
	print("\nDo you want to choose another option? [Y/N]")
	interrupted = True

	operation = raw_input()

	if (operation.lower() == 'y'):
		interrupted = False

	if (interrupted == True):
		print("End of execution!")

	return interrupted
