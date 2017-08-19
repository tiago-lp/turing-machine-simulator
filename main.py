# -*- coding: utf-8 -*-
# Turing Machine Simulator

from Tkinter import tkFileDialog

def main():
	print("")

if __name__ == "__main__":
	main()

while True:
	print("Choose an option:")
	print("[1] To submit your own machine")
	print("[2] To use some built-in machine")
	print("[3] Exit")

	option = raw_input()

	if (option == 1):
		# open file and process to build a machine

	elif (option == 2):
		# open a list of the machines built-in
		print("Choose one of these machines")

	elif (option == 3):
		break
	
	else:
		print("Something is wrong...)
		print("... maybe you must try choose one of valid options")