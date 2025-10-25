

def parseLabels(filename):
    # If we want to have an editor that can handle loops and such
    # We'll need a way to parse for labels (i.e. ".loop", you look for the '.' character)

    labels = {}
    lineN = 0

    try:    
        with open(filename) as file:
            for line in file:
                line = line.replace('\n', '').replace('\r', '')
                if line[0] == '#':
                    # Allows comments
                    continue

                if line[0] == '.':
                    # Save the address of the label
                    labels[line[1:]] = lineN*4
                    print("Label found: ", + line[1:] + " on " + format(lineN * 4, '#04x'))
                else:
                    lineN += 1
    except:
        print("Error: File not found")
                

    return labels

def instructionRead(filename, labels):
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
    
    try:    
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
                elif tok[0].upper() == "MOVE":
                    reg1 = tok[1]
                    reg2 = tok[2]
                    registers[reg1] = registers[reg2]

                    by = [0x30, tok[1][1], 0, tok[2][1]]
                    print("opcode: " + format(by[0], '#04x') + ", Register: " + by[1] + ", Data Hi: " + by[2] + ", Data Lo: " + by[3])
                    print("Memory content for register " + tok[1][1] + ": " + registers[reg1])
                elif tok[0].upper() == "ADD":
                    # Process Add instruction here
                    reg1 = tok[1]
                    val = int(tok[2])
                    registers[reg1] += val
                    by = [0x40, tok[1][1], val >> 8, val & 0xFF]
                    print("opcode: " + format(by[0], '#04x') + ", Register: " + by[1] + ", Data Hi: " + by[2] + ", Data Lo: " + by[3])
                    print("Memory content for register " + tok[1][1] + ": " + registers[reg1])
                elif tok[0].upper() == "ADDREG":
                    # Process Add instruction here
                    reg1 = tok[1]
                    reg2 = tok[2]
                    registers[reg1] += registers[reg2]
                    by = [0x41, tok[1][1], 0, tok[2][1]]
                    print("opcode: " + format(by[0], '#04x') + ", Register: " + by[1] + ", Data Hi: " + by[2] + ", Data Lo: " + by[3])
                    print("Memory content for register " + tok[1][1] + ": " + registers[reg1])
                elif tok[0].upper() == "SUBTRACT":
                    # Process Subtract instruction here
                    reg1 = tok[1]
                    val = int(tok[2])
                    registers[reg1] -= val
                    by = [0x42, tok[1][1], val >> 8, val & 0xFF]
                    print("opcode: " + format(by[0], '#04x') + ", Register: " + by[1] + ", Data Hi: " + by[2] + ", Data Lo: " + by[3])
                    print("Memory content for register " + tok[1][1] + ": " + registers[reg1])
                elif tok[0].upper() == "SUBTRACTREG":
                    # Process Add instruction here
                    reg1 = tok[1]
                    reg2 = tok[2]
                    registers[reg1] -= registers[reg2]
                    by = [0x43, tok[1][1], 0, tok[2][1]]
                    print("opcode: " + format(by[0], '#04x') + ", Register: " + by[1] + ", Data Hi: " + by[2] + ", Data Lo: " + by[3])
                    print("Memory content for register " + tok[1][1] + ": " + registers[reg1])
                elif tok[0].upper() == "MULTIPLY":
                    # Process Multiply instruction here
                    reg1 = tok[1]
                    val = int(tok[2])
                    registers[reg1] *= val
                    by = [0x44, tok[1][1], val >> 8, val & 0xFF]
                    print("opcode: ", format(by[0], '#04x') + ", Register: " + by[1] + ", Data Hi: " + by[2] + ", Data Lo: " + by[3])
                    print("Memory content for register " + tok[1][1] + ": " + registers[reg1])
                elif tok[0].upper() == "MULTIPLYREG":
                    # Process Multiply instruction here
                    reg1 = tok[1]
                    reg2 = tok[2]
                    registers[reg1] *= registers[reg2]
                    by = [0x45, tok[1][1], 0, tok[2][1]]
                    print("opcode: " + format(by[0], '#04x') + ", Register: " + by[1] + ", Data Hi: " + by[2] + ", Data Lo: " + by[3])
                    print("Memory content for register " + tok[1][1] + ": " + registers[reg1])
                elif tok[0].upper() == "DIVISION":
                    # Process Dividision instruction here
                    reg1 = tok[1]
                    val = int(tok[2])
                    if val == 0:
                        print("Error: can't divide by zero")
                        break
                    registers[reg1] *= val
                    by = [0x46, tok[1][1], val >> 8, val & 0xFF]
                    print("opcode: " + format(by[0], '#04x') + ", Register: " + by[1] + ", Data Hi: " + by[2] + ", Data Lo: " + by[3])
                    print("Memory content for register " + tok[1][1] + ": " + registers[reg1])
                elif tok[0].upper() == "DIVISIONREG":
                    # Process Division instruction here
                    reg1 = tok[1]
                    reg2 = tok[2]
                    if reg2 == 0:
                        print("Error: can't divide by zero")
                        break
                    registers[reg1] *= registers[reg2]
                    by = [0x47, tok[1][1], 0, tok[2][1]]
                    print("opcode: " + format(by[0], '#04x') + ", Register: " + by[1] + ", Data Hi: " + by[2] + ", Data Lo: " + by[3])
                    print("Memory content for register " + tok[1][1] + ": " + registers[reg1])
                elif tok[0].upper() == "COMPARE":
                    # Process Compare instruction here
                    return
                elif tok[0].upper() == "BRANCHEQR":
                    # Process Branch If Equal (Register Comparison) instruction here
                    # Don't forget that there's 4 types of Branch
                    reg1 = tok[1]
                    reg2 = tok[2]
                    label = tok[3]

                    if label not in labels:
                        print("Error: Invalid label provided")
                        break
                    elif registers[reg1] == registers[reg2]:
                        # Do... something, not a continue statement
                        continue
                    else:
                        # Continue reading lines in order
                        continue
                    return
                else:
                    # Handle invalid instructions
                    # If we include labels, need a way to skip over label lines to avoid
                    print("Invalid instruction!")
    except:
        print("Error: file not found")

    return



if __name__ == "__main__":
    filen = input('Enter a file name: ')
    labels = parseLabels(filen)
    instructionRead(filen, labels)








