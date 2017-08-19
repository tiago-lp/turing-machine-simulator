# -*- coding: utf-8 -*-
# Turing Machine Simulator

from Tkinter import *

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

def invalid_option():
	print("Something is wrong...")
	print("... maybe you must try again choosing one of valid options")
	print("")

def optionOne():
	pass

def optionTwo():
	examples_machines()
	example = int(raw_input())

	if (example == 1):
		arq_one = open('examples_machines/conversion_binary.txt', 'r')
		machine_one = arq_one.read()			

	elif (example == 2):
		arq_two = open('examples_machines/palindrome_detector.txt', 'r')
		machine_two = arq_two.read()					

	else:
		invalid_option()	

def main():
	while True:
		menu()
		option = int(raw_input())

		if (option == 1):
			# open file and process to build a machine		
			optionOne()
			break	

		elif (option == 2):
			optionTwo()
			break

		elif (option == 3):
			break
	
		else:
			invalid_option()
			

if __name__ == "__main__":
	main()