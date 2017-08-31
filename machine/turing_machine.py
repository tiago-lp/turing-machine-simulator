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

def run(tape, machine):
    delta = generateDictionary(machine)
    current_state = "0"
    current_tape = list(tape)
    tape_position = 0

    while not is_halt_state(current_state):
        ## apos finalizar a saida no terminal, apagar este print
        print "State:", current_state, "  Tape:", "".join(current_tape), "  Position:", tape_position

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

    print "State:", current_state, " Tape:", "".join(current_state), " Position:", tape_position
    print "\nDone"
    print "Final State:", current_state
    print "Final Tape:", "".join(current_tape)
