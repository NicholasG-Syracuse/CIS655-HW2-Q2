import os

def parseLabels(filename):
    # If we want to have an editor that can handle loops and such
    # We'll need a way to parse for labels (i.e. ".loop", you look for the '.' character)

    labels = {}
    lineN = 0

        
    with open(filename) as file:
        # Read the file and split it into each line, remove any newline characters and empty lines
        fileR = file.readlines()
        lineS = [line.rstrip('\n') for line in fileR if line.strip()]
        
        # Process lines in order
        for line in lineS:
            if line[0] == '#':
                # Allows comments
                continue

            if line[0] == '.':
                # Save the address of the label
                labels[line[1:]] = lineN
                print("Label found: " + line[1:] + " on line #" + str(lineN))
                lineN += 1
            else:
                lineN += 1
                

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
    memory = {}

    # Create list of all lines in the file in order
    f = open(filename)
    lines = f.readlines()
    # Strip any newline characters from lines in list
    lineS = [line.rstrip('\n') for line in lines if line.strip()]
    f.close()

    
    # Tokenize line by splitting them on spaces and (maybe) commas
    # Properly assign each token to the right piece of an instruction

    # (If we're using a file and not entering instructions manually)
    # Start by reading line by line to tokenize and process them
    
    # An example instruction could be "LOAD R1 50"
    # The first token is the instruction, "LOAD"
    # The second token is the register we use to update the dictionary, i.e. "R1"
    # The third token is the value being loaded, "50"
        
    # While loop allows us to move around to specific lines as needed for branch instructions
    # initialize counter variable
    lineCounter = 0
    while lineCounter != len(lineS):
        # Split line on spaces
        tok = lineS[lineCounter].split()

        # Big chunk of if/else statements reading tokens goes here
        if tok[0].upper() == "LOAD":
            # Process Load instruction here
            #print("Processing LOAD instructions:")
            #  Extract register (reg) and value (val)
            if len(tok) >= 3:
                reg = tok[1].upper()
                val = int(tok[2])

                registers[reg] = val
                by = [0x10, tok[1][1], val >> 8, val & 0xFF]
                print("opcode: " + format(by[0], '#04x') + ", Register: " + str(by[1]) + ", Data Hi: " + str(by[2]) + ", Data Lo: " + str(by[3]))
                print("Memory content for register " + str(tok[1][1]) + ": " + str(registers[reg]))
                lineCounter += 1
            else:
                print("Error Loading instruction")
        elif tok[0].upper() == "LOADMEM":
            # Process Load from Memory instruction here
            #  Extract register (reg) and memory address (memaddr)
            if len(tok) >= 3:
                reg = tok[1].upper()
                memaddr = int(tok[2])

                if memaddr in memory:
                    registers[reg] = memory[memaddr]
                    by = [0x11, tok[1][1], val >> 8, val & 0xFF]
                    print("opcode: " + format(by[0], '#04x') + ", Register: " + str(by[1]) + ", Data Hi: " + str(by[2]) + ", Data Lo: " + str(by[3]))
                    print("Memory content for register " + str(tok[1][1]) + ": " + str(registers[reg]))
                    lineCounter += 1
                else:
                    print("Invalid memory address")
                    break
            else:
                print("Error Loading instruction")                     
        elif tok[0].upper() == "STORE":
            # Process Store instruction here
            if len(tok) >= 3:
                reg = tok[1].upper()
                addr = int(tok[2])

                memory[addr] = registers[reg]
                by = [0x20, tok[1][1], addr >> 8, addr & 0xFF]
                print("opcode: " + format(by[0], '#04x') + ", Register: " + str(by[1]) + ", Addr Hi: " + str(
                    by[2]) + ", Addr Lo: " + str(by[3]))
                print("Stored value " + str(registers[reg]) + " from register " + str(
                    tok[1][1]) + " to memory address " + str(addr))
                lineCounter += 1
            else:
                print("Error: STORE requires register and memory address")
                break
            continue
        elif tok[0].upper() == "MOVE":
            reg1 = tok[1].upper()
            reg2 = tok[2].upper()
            registers[reg1] = registers[reg2]

            by = [0x30, tok[1][1], 0, tok[2][1]]
            print("opcode: " + format(by[0], '#04x') + ", Register: " + str(by[1]) + ", Data Hi: " + str(by[2]) + ", Data Lo: " + str(by[3]))
            print("Memory content for register " + str(tok[1][1]) + ": " + str(registers[reg1]))
            lineCounter += 1
        elif tok[0].upper() == "ADD":
            # Process Add instruction here
            reg1 = tok[1].upper()
            val = int(tok[2])
            registers[reg1] += val
            by = [0x40, tok[1][1], val >> 8, val & 0xFF]
            print("opcode: " + format(by[0], '#04x') + ", Register: " + str(by[1]) + ", Data Hi: " + str(by[2]) + ", Data Lo: " + str(by[3]))
            print("Memory content for register " + str(tok[1][1]) + ": " + str(registers[reg1]))
            lineCounter += 1
        elif tok[0].upper() == "ADDREG":
            # Process Add instruction here
            reg1 = tok[1].upper()
            reg2 = tok[2].upper()
            registers[reg1] += registers[reg2]
            by = [0x41, tok[1][1], 0, tok[2][1]]
            print("opcode: " + format(by[0], '#04x') + ", Register: " + str(by[1]) + ", Data Hi: " + str(by[2]) + ", Data Lo: " + str(by[3]))
            print("Memory content for register " + str(tok[1][1]) + ": " + str(registers[reg1]))
            lineCounter += 1
        elif tok[0].upper() == "SUBTRACT":
            # Process Subtract instruction here
            reg1 = tok[1].upper()
            val = int(tok[2])
            registers[reg1] -= val
            by = [0x42, tok[1][1], val >> 8, val & 0xFF]
            print("opcode: " + format(by[0], '#04x') + ", Register: " + str(by[1]) + ", Data Hi: " + str(by[2]) + ", Data Lo: " + str(by[3]))
            print("Memory content for register " + str(tok[1][1]) + ": " + str(registers[reg1]))
            lineCounter += 1
        elif tok[0].upper() == "SUBTRACTREG":
            # Process Add instruction here
            reg1 = tok[1].upper()
            reg2 = tok[2].upper()
            registers[reg1] -= registers[reg2]
            by = [0x43, tok[1][1], 0, tok[2][1]]
            print("opcode: " + format(by[0], '#04x') + ", Register: " + str(by[1]) + ", Data Hi: " + str(by[2]) + ", Data Lo: " + str(by[3]))
            print("Memory content for register " + str(tok[1][1]) + ": " + str(registers[reg1]))
            lineCounter += 1
        elif tok[0].upper() == "MULTIPLY":
            # Process Multiply instruction here
            reg1 = tok[1].upper()
            val = int(tok[2])
            registers[reg1] *= val
            by = [0x44, tok[1][1], val >> 8, val & 0xFF]
            print("opcode: ", format(by[0], '#04x') + ", Register: " + str(by[1]) + ", Data Hi: " + str(by[2]) + ", Data Lo: " + str(by[3]))
            print("Memory content for register " + str(tok[1][1]) + ": " + str(registers[reg1]))
            lineCounter += 1
        elif tok[0].upper() == "MULTIPLYREG":
            # Process Multiply instruction here
            reg1 = tok[1].upper()
            reg2 = tok[2].upper()
            registers[reg1] *= registers[reg2]
            by = [0x45, tok[1][1], 0, tok[2][1]]
            print("opcode: " + format(by[0], '#04x') + ", Register: " + str(by[1]) + ", Data Hi: " + str(by[2]) + ", Data Lo: " + str(by[3]))
            print("Memory content for register " + str(tok[1][1]) + ": " + str(registers[reg1]))
            lineCounter += 1
        elif tok[0].upper() == "DIVISION":
            # Process Dividision instruction here
            reg1 = tok[1].upper()
            val = int(tok[2])
            if val == 0:
                print("Error: can't divide by zero")
                break
            registers[reg1] /= val
            by = [0x46, tok[1][1], val >> 8, val & 0xFF]
            print("opcode: " + format(by[0], '#04x') + ", Register: " + str(by[1]) + ", Data Hi: " + str(by[2]) + ", Data Lo: " + str(by[3]))
            print("Memory content for register " + str(tok[1][1]) + ": " + str(registers[reg1]))
            lineCounter += 1
        elif tok[0].upper() == "DIVISIONREG":
            # Process Division instruction here
            reg1 = tok[1].upper()
            reg2 = tok[2].upper()
            if reg2 == 0:
                print("Error: can't divide by zero")
                break
            registers[reg1] /= registers[reg2]
            by = [0x47, tok[1][1], 0, tok[2][1]]
            print("opcode: " + format(by[0], '#04x') + ", Register: " + str(by[1]) + ", Data Hi: " + str(by[2]) + ", Data Lo: " + str(by[3]))
            print("Memory content for register " + str(tok[1][1]) + ": " + str(registers[reg1]))
            lineCounter += 1
        elif tok[0].upper() == "COMPARELT":
            # Process Compare Less Than instruction here
            reg1 = tok[1].upper()
            reg2 = tok[2].upper()
            val = int(tok[3])

            if registers[reg2] < val:
                registers[reg1] = 1
                by = [0x50, tok[1][1], val >> 8, val & 0xFF]
                print("opcode: " + format(by[0], '#04x') + ", Register: " + str(by[1]) + ", Data Hi: " + str(by[2]) + ", Data Lo: " + str(by[3]))
                print("Memory content for register " + str(tok[1][1]) + ": " + str(registers[reg1]))
                lineCounter += 1
            else:
                registers[reg1] = 0
                by = [0x50, tok[1][1], val >> 8, val & 0xFF]
                print("opcode: " + format(by[0], '#04x') + ", Register: " + str(by[1]) + ", Data Hi: " + str(by[2]) + ", Data Lo: " + str(by[3]))
                print("Memory content for register " + str(tok[1][1]) + ": " + str(registers[reg1]))
                lineCounter += 1
        elif tok[0].upper() == "BRANCHEQ":
            # Process Branch If Equal (Register/Value Comparison) instruction here
            # Don't forget that there's 4 types of Branch
            reg1 = tok[1].upper()
            val = int(tok[2])
            label = tok[3]

            if label not in labels:
                print("Error: Invalid label provided")
                break
            elif registers[reg1] == val:
                # Set the line counter variable to the line after the label you want to branch to 
                lineCounter = labels[label] + 1
                by = [0x60, tok[1][1], val >> 8, val & 0xFF]
                print("opcode: " + format(by[0], '#04x') + ", Register: " + str(by[1]) + ", Data Hi: " + str(by[2]) + ", Data Lo: " + str(by[3]))
                continue
            else:
                # Continue reading lines in order
                lineCounter += 1
                continue
        elif tok[0].upper() == "BRANCHNE":
            # Process Branch If Not Equal (Register/Value Comparison) instruction here
            # Don't forget that there's 4 types of Branch
            reg1 = tok[1].upper()
            val = int(tok[2])
            label = tok[3]

            if label not in labels:
                print("Error: Invalid label provided")
                break
            elif registers[reg1] != val:
                # Set the line counter variable to the line after the label you want to branch to 
                lineCounter = labels[label] + 1
                by = [0x61, tok[1][1], val >> 8, val & 0xFF]
                print("opcode: " + format(by[0], '#04x') + ", Register: " + str(by[1]) + ", Data Hi: " + str(by[2]) + ", Data Lo: " + str(by[3]))
                continue
            else:
                # Continue reading lines in order
                lineCounter += 1
                continue
        elif tok[0].upper() == "BRANCHGT":
            # Process Branch If Greater Than (Register/Value Comparison) instruction here
            # Don't forget that there's 4 types of Branch
            reg1 = tok[1].upper()
            val = int(tok[2])
            label = tok[3]

            if label not in labels:
                print("Error: Invalid label provided")
                break
            elif registers[reg1] > val:
                # Set the line counter variable to the line after the label you want to branch to 
                lineCounter = labels[label] + 1
                by = [0x62, tok[1][1], val >> 8, val & 0xFF]
                print("opcode: " + format(by[0], '#04x') + ", Register: " + str(by[1]) + ", Data Hi: " + str(by[2]) + ", Data Lo: " + str(by[3]))
                continue
            else:
                # Continue reading lines in order
                lineCounter += 1
                continue
        elif tok[0].upper() == "BRANCHLT":
            # Process Branch If Less Than (Register/Value Comparison) instruction here
            # Don't forget that there's 4 types of Branch
            reg1 = tok[1].upper()
            val = int(tok[2])
            label = tok[3]

            if label not in labels:
                print("Error: Invalid label provided")
                break
            elif registers[reg1] < val:
                # Set the line counter variable to the line after the label you want to branch to 
                lineCounter = labels[label] + 1
                by = [0x63, tok[1][1], val >> 8, val & 0xFF]
                print("opcode: " + format(by[0], '#04x') + ", Register: " + str(by[1]) + ", Data Hi: " + str(by[2]) + ", Data Lo: " + str(by[3]))
                continue
            else:
                # Continue reading lines in order
                lineCounter += 1
                continue
        else:
            # Handle invalid instructions
            # If we include labels, need a way to skip over label lines to avoid
            if tok[0][1:] in labels:
                lineCounter += 1
                continue
            else:
                print("Invalid instruction!")
                break



if __name__ == "__main__":
    # Get file name from user and process it
    fileAsk = input('Enter a file name: ')
    here = os.path.dirname(os.path.abspath(__file__))
    filen = os.path.join(here, fileAsk)

    labels = parseLabels(filen)
    instructionRead(filen, labels)








