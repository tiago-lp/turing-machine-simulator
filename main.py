# -*- coding: utf-8 -*-
# Turing Machine Simulator

import sys
sys.path.append("../")
from tkFileDialog import askopenfile
from Tkinter import Tk
from os import environ
from machine import turing_machine

''' Shows the principal menu.'''
def menu():
	print("\nChoose an option:")
	print("	[1] - Submit your own machine")
	print("	[2] - Load some built-in machine")
	print("	[3] - Exit\n")

'''Shows the menu of chooses of the built-in machines.'''
def examples_machines():
	print("\nLoad an example program:")
	print("")
	print("[1] - Binary to decimal conversion")
	print("[2] - Palindrome detector\n")

'''Indicates what the user attempted to choose an invalid operation'''
def invalid_operation():
	print("\nSomething is wrong...")
	print("... maybe you must try again choosing one of valid options\n")

'''Ask the user if it is time to close the program.'''
def interrupted_execution():
	print("\nDo you want to choose another option? [Y/N]")
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

	file = askopenfile(initialdir = environ["HOME"], parent=main_window,
				filetypes=[("Text Files", "*.txt")])
	if file != None:
		data = file.read()
		file.close()
		return data
	else:
		print("Canceled")
		return None

'''This option provides the user to send his own machine, if it has been described correctly in the syntax
'''
def option_one():
	# Open a dialog box to choose of the corresponding machine
	print("Choose the file corresponding to the machine!")
	machine = openfile()

	if machine:
		# The machine read a input and process.
		print("Enter the input string")
		input_word = raw_input()

		"""
		TODO: nessa opcao um e na dois esse mesmo trecho de codigo se repete.
		Modularizar isso.
		Tambem implementar o rodar passo a passo, por hora ele ta executando de uma vez.
		"""
		# If necessary, call the machine step by step.
		if (run_step_by_step()):
				print("Running step-by-step")
				turing_machine.run(input_word, machine)
		else:
			turing_machine.run(input_word, machine)
			

'''This option provides the user to choose one of built-in's machines'''
def option_two():

	examples_machines()

	chosen_example = raw_input()
	machine = ""

	if (chosen_example == '1'):
		# The machine process the file and the input.
		machine = open('examples_machines/conversion_binary.txt', 'r').read()

	elif (chosen_example == '2'):
		# The machine process the file and the input.
		machine = open('examples_machines/palindrome_detector.txt', 'r').read()

	else:
		invalid_operation()

	# The machine read a input and process
	print("Enter the input string")
	input_word = raw_input()

	if (run_step_by_step()):
			print("Running step-by-step")
			turing_machine.run(input_word, machine)
	else:
		turing_machine.run(input_word, machine)

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
