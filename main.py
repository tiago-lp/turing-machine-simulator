# -*- coding: utf-8 -*-
# Turing Machine Simulator

from tkFileDialog import askopenfile
from Tkinter import Tk
from os import environ

''' Shows the principal menu.'''
def menu():
	print("Choose an option:")
	print("	[1] - Submit your own machine")
	print("	[2] - Load some built-in machine")
	print("	[3] - Exit")
	print("")

'''Shows the menu of chooses of the built-in machines.'''
def examples_machines():
	print("Load an example program:")
	print("")
	print("[1] - Binary to decimal conversion")
	print("[2] - Palindrome detector")
	print("")

'''Indicates what the user attempted to choose an invalid operation'''
def invalid_operation():
	print("Something is wrong...")
	print("... maybe you must try again choosing one of valid options")
	print("")

'''Ask the user if it is time to close the program.'''
def interrupted_execution():
	print("Do you want to choose another option? [Y/N]")
	interrupted = True

	operation = raw_input()

	if (operation.lower() == 'y'):
		interrupted = False

	if (interrupted == True):
		print("End of execution!")

	return interrupted

'''Ask the user if he wants sees the step by step of a turing machine running'''
def run_step_by_step():
	print("You want see the step by step? [Y/N]")
	run = False

	operation = raw_input()

	if (operation.lower() == 'y'):
		run = True

	return run

'''Opens a window asking the user the machine file'''
def openfile():
	main_window = Tk()
	main_window.withdraw()

	file = askopenfile(initialdir = environ["HOME"], parent=main_window)
	if file != None:
    		data = file.read()

    	file.close()
    	return data

'''This option provides the user to send his own machine, if it has been described correctly in the syntax
'''
def option_one():
	# Open a dialog box to choose of the corresponding machine
	print("Choose the file corresponding to the machine!")
	machine = openfile()

	# The machine read a input and process.
	print("Enter the input string")
	input_word = raw_input()

	# If necessary, call the machine step by step.
	if (run_step_by_step()):
			print("Running step-by-step")

'''This option provides the user to choose one of built-in's machines'''
def option_two():

	examples_machines()

	chosen_example = raw_input()

	if (chosen_example == '1'):
		# The machine process the file and the input.
		arq_one = open('examples_machines/conversion_binary.txt', 'r')

		# The machine read a input and process
		print("Enter the input string")
		input_word = raw_input()

		# If necessary, call the machine step by step.
		if (run_step_by_step()):
			print(arq_one.read())
			print("Step by Step")

	elif (chosen_example == '2'):
		# The machine process the file and the input.
		arq_two = open('examples_machines/palindrome_detector.txt', 'r')

		# The machine read a input and process.
		print("Enter the input string")
		input_word = raw_input()

		# If necessary, call the machine step by step.
		if (run_step_by_step()):
			print("Running step-by-step")

	else:
		invalid_operation()

def main():
	while True:

		menu()

		operation = raw_input()

		if (operation == '1'):
			option_one()
			if (interrupted_execution()):
				break

		elif (operation == '2'):
			option_two()
			if (interrupted_execution()):
				break


		elif (operation == '3'):
			break

		else:
			invalid_operation()


if __name__ == "__main__":
	main()
