# -*- coding: utf-8 -*-
# Turing Machine Simulator

from tkFileDialog import askopenfile

def menu():
	print("Choose an option:")
	print("	[1] - Submit your own machine")
	print("	[2] - Load some built-in machine")
	print("	[3] - Exit")
	print("")

def examples_machines():
	print("Load an example program:")
	print("")
	print("[1] - Binary to decimal conversion")
	print("[2] - Palindrome detector")
	print("")

def invalid_operation():
	print("Something is wrong...")
	print("... maybe you must try again choosing one of valid options")
	print("")

def interrupted_execution():
	print("Do you want to choose another option? [Y/N]")
	interrupted = False

	operation = raw_input()
	
	if (operation.lower() == 'y'):
		run = True

	return interrupted

def run_step_by_step():
	print("You want see the step by step? [Y/N]")	
	run = False
	
	operation = raw_input()
	
	if (operation.lower() == 'y'):
		run = True

	return run

def optionOne():
	print("Choose the file corresponding to the machine!")
	machine = askopenfile()	


def optionTwo():
	examples_machines()
	example = int(raw_input())

	if (example == 1):
		# the machine process the file and the input
		arq_one = open('examples_machines/conversion_binary.txt', 'r')
		
		print("Enter the input string") # the machine read a input and process
		input_word = raw_input()

		if (run_step_by_step()):
			print("Step by Step") # call the machine step by step

	elif (example == 2):
		# the machine process the file and the input
		arq_two = open('examples_machines/palindrome_detector.txt', 'r')
		
		print("Enter the input string") # the machine read a input and process
		input_word = raw_input() 
		

		if (run_step_by_step()):
			print("Step by Step") # call the machine step by step
		
	else:
		invalid_operation()	

def main():
	while True:
		menu()
		operation = int(raw_input())

		if (operation == 1):
			# open file and process to build a machine		
			optionOne()
			if (interrupted_execution()):
				break

		elif (operation == 2):
			optionTwo()
			if (interrupted_execution()):
				break

		elif (operation == 3):
			break	

		else:
			invalid_operation()
			

if __name__ == "__main__":
	main()