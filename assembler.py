

def parseLabels():
    # If we want to have an editor that can handle loops and such
    # We'll need a way to parse for labels (i.e. ".loop", you look for the '.' character) 
    return

def instructionRead(filename):
    # Dictionary used to store register values for registers 1-7
    registers = {
        "R1": 0,
        "R2": 0,
        "R3": 0,
        "R4": 0,
        "R5": 0,
        "R6": 0,
        "R7": 0
    }

    # Tokenize line by splitting them on spaces and (maybe) commas
    # Properly assign each token to the right piece of an instruction

    # (If we're using a file and not entering instructions manually)
    # Start by reading the file line by line to tokenize and process them
    
    # An example instruction could be "LOAD R1 50"
    # The first token is the instruction, "LOAD"
    # The second token is the register we use to update the dictionary, i.e. "R1"
    # The third token is the value being loaded, "50"
    
    with open(filename) as file:
        for line in file:
            # Split line on spaces
            tok = line.split()

            # Big chunk of if/else statements reading tokens goes here
            if tok[0].upper() == "LOAD":
                # Process Load instruction here
                return
            elif tok[0].upper() == "STORE":
                # Process Store instruction here
                return
            elif tok[0].upper() == "ADD":
                # Process Add instruction here
                reg1 = tok[1]
                reg2 = tok[2]
                val = tok[3]
                registers[reg1] = registers[reg2] + val
                return
            elif tok[0].upper() == "ADDREG":
                # Process Add instruction here
                reg1 = tok[1]
                reg2 = tok[2]
                registers[reg1] += registers[reg2]
                return
            elif tok[0].upper() == "SUBTRACT":
                # Process Subtract instruction here
                reg1 = tok[1]
                reg2 = tok[2]
                val = tok[3]
                registers[reg1] = registers[reg2] - val
                return
            elif tok[0].upper() == "SUBTRACTREG":
                # Process Add instruction here
                reg1 = tok[1]
                reg2 = tok[2]
                registers[reg1] -= registers[reg2]
            elif tok[0].upper() == "COMPARE":
                # Process Compare instruction here
                return
            elif tok[0].upper() == "BRANCH":
                # Process Branch instruction here
                # Don't forget that there's 4 types of Branch
                return
            else:
                # Handle invalid instructions
                # If we include labels, need a way to skip over label lines to avoid
                print("Invalid instruction!")

    return












