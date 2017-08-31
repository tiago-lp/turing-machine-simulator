# Encapsulates operations with files.

def open_file(path):
	file = ""
	try:
		file = open(path,'r').read()
	except IOError:
		iof_err()

	return file

def open_binary_conversion():
	file = ""

	try:
		file = open('examples_machines/conversion_binary.txt', 'r').read()
	except IOError:
		iof_err()

	return file

def open_palind_detector():
	file = ""

	try:
		file = open('examples_machines/palindrome_detector.txt', 'r').read()
	except IOError:
		iof_err()

	return file

def iof_err():
	print("\nFile not found. Verify if the path is correct.")