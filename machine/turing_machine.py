from dictionary import generateDictionary
'''
transition function delta: dictionary {(q0, r):(q1, w, D)}
q0 -> old state
q1 -> new state
r  -> read from tape
w  -> write on tape
D  -> direction to move (L / D / *)
'''

#state needs to be a string
def is_halt_state(state):
    if len(state) < 4:
        return False
    else:
        return state[0:4] == "halt" #starts with "halt"

def run(tape, machine, step_by_step):
    delta = generateDictionary(machine)
    current_state = "0"
    current_tape = list(tape)
    tape_position = 0
    steps = 0

    while not is_halt_state(current_state):
		print "State: %s\tTape: %s\tPosition: %d\tSteps: %d" % (current_state, "".join(current_tape), tape_position, steps),
		steps += 1
		
		if step_by_step:
			option = raw_input()
			if option.lower() == "end":
				step_by_step = False
		else:
			print ""
		try:
			if (current_state, current_tape[tape_position]) in delta:
				(q1, w, D) = delta[(current_state, current_tape[tape_position])]
			else:
				(q1, w, D) = delta[(current_state, '*')] # * is the wildcard

			if w != '*':
				current_tape[tape_position] = w
			if q1 != '*':
				current_state = q1

			if D == 'l':
				if tape_position > 0:
					tape_position -= 1
				else:
					current_tape.insert(0, '_') #increase tape at start, right shift
			elif D == 'r':
				tape_position += 1
				if tape_position == len(current_tape): #increase tape at the end
					current_tape.append('_')
			
		except KeyError:
			# Transition doesnt exist!!
			print "Error!"
			break

    print "\nState: %s  Tape: %s  Position: %d Steps: %d" % (current_state, "".join(current_tape), tape_position, steps)
    print "\nDone"
    print "Final State:", current_state
    print "Final Tape:", "".join(current_tape)
    print "Number of steps:", steps
