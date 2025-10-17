

def parseLabels():
    # If we want to have an editor that can handle loops and such
    # We'll need a way to parse for labels (i.e. ".loop", you look for the '.' character) 
    return

def instructionRead(filename):
    # Tokenize line by splitting them on spaces and (maybe) commas
    # Properly assign each token to the right piece of an instruction

    # (If we're using a file and not entering instructions manually)
    # Start by reading the file line by line to tokenize and process them
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
                return
            elif tok[0].upper() == "SUBTRACT":
                # Process Subtract instruction here
                return
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












