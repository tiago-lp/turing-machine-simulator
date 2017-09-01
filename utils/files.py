# Encapsulates operations with files.
import os

def open_file(machine_number):
	for i in range(len(list_machines())):
		if (i + 1) == int(machine_number):
			file_name = list_machines()[i]	

	file = ""
	try:
		file = open(path_machines()+file_name,'r').read()
	except IOError:
		iof_err()
	return file

def path_machines():
	return os.getcwd()+'/my_machines/'

def list_machines():
	return os.listdir(path_machines())

def has_machines():
	has = True
	if (len(list_machines()) == 0):		
		has = False	
	return has
	
def my_machines():
	machines = list_machines()
	print 	
	for i in range(len(machines)):
		print str(i+1) + " - " + machines[i]	

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