# -*- coding: utf-8 -*-
# Turing Machine Simulator

from Tkinter import *

root = Tk()

def menu():
	print("Choose an option:")
	print("	[1] - Submit your own machine")
	print("	[2] - Use some built-in machine")
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

def main():
	while True:
		menu()
		option = int(raw_input())

		if (option == 1):
			# open file and process to build a machine
			print("option 1")

		elif (option == 2):
			examples_machines()	
			example = int(raw_input())

		elif (option == 3):
			break
	
		else:
			invalid_option()
			

if __name__ == "__main__":
	main()