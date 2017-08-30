from dictionary import generateDictionary
'''
transition function delta: dictionary {(q0, r):(q1, w, D)}
q0 -> old state
q1 -> new state
r  -> read from tape
w  -> write on tape
D  -> direction to move (L / D / *)
'''

delta = {}
q_start = "0"
tape = []

#state needs to be a string
def is_halt_state(state):
    if len(state) < 4:
        return False
    else:
        return state[0:4] == "halt" #starts with "halt"


''' apenas para testar. PODE APAGAR DEPOIS
 a intencao eh q dps do front-end estar codado, essa funcao seja apagada
 e o delta{} e tape[] sejam preenchidos automaticamente '''
def simula():
    global tape
    global delta

    #tape precisa ser uma lista de caracteres
    #por exemplo tape = ['a', 'a', 'Z', 'b', '_', '*']
    # tape = list("aaaaab")
    #tape para bynary to decimal e delta para binary to decimal
    # tape = list('1110101') # result == 117
    # delta = generateDictionary(open('./../examples_machines/binary_decimal.txt', 'r'))

    #tape para palindrome
    tape = list('110011') # result == true
    delta = generateDictionary(open('./../examples_machines/palindrome_detector.txt', 'r'))

    #delta precisa assumir esse formato (descrito no inicio do codigo)
    #delta[(estado, leitura)] = (novo_estado, escrita, direcao_movimento)
    # delta[("0", 'a')] = ("*", 'c', 'r')
    # delta[("0", 'b')] = ("voltando", 'd', 'l')
    # delta[("voltando", 'c')] = ("*", '*', 'l')
    # delta[("voltando", '_')] = ("halt-deubom", 'e', 'r')
    #

    # print(test())

def run():
    current_state = q_start
    current_tape = tape
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

    ## apos finalizar a saida no terminal, apagar estes prints
    print "Done"
    print "Final State:", current_state
    print "Final Tape:", "".join(current_tape)

if __name__ == "__main__":
    simula() ## PODE APAGAR DEPOIS
    run()
