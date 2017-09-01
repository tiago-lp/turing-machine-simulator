# Turing Machine Simulator

from os import sys
from machine import turing_machine
from utils import prints, files

sys.path.append("../")

'''
If necessary, run the step by step of machine
'''
def step_by_step(input_word, machine):
	if (prints.run_stepbystep()):
		turing_machine.run(input_word, machine, True)
	else:
		turing_machine.run(input_word, machine, False)	

'''
This option provides the user to send his own machine, 
if it has been described correctly in the syntax
'''
def option_one():
	machine = None

	if (files.has_machines()):
		files.my_machines()

		print("\nSelect your file number:\n")
		chosen_machine = raw_input()
		machine = files.open_file(chosen_machine)	
	else:
		prints.machines_not_found()

	if (machine):
		# The machine read a input and process.
		print("Enter the input string\n")
		input_word = raw_input()

		# If necessary, call the machine step by step.
		step_by_step(input_word, machine)	

'''
This option provides the user to choose one of built-in's machines
'''
def option_two():
	prints.examples_machines()

	chosen_example = raw_input()
	machine = ""

	if (chosen_example == '1'):
		# The machine process the file and the input.
		machine = files.open_binary_conversion()

	elif (chosen_example == '2'):
		# The machine process the file and the input.
		machine = files.open_palind_detector()

	else:
		prints.invalid_operation()

	# The machine read a input and process
	print("Enter the input string\n")
	input_word = raw_input()

	# If necessary, call the machine step by step.
	step_by_step(input_word, machine)

def main():
	while True:

		prints.menu()

		operation = raw_input()

		if (operation == '1'):
			option_one()
			if (prints.interrupted_execution()):
				break
		elif (operation == '2'):
			option_two()
			if (prints.interrupted_execution()):
				break
		elif (operation == '3'):
			break		
		else:
			prints.invalid_operation()

if __name__ == "__main__":
	main()