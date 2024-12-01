import time

def print_pause(message, delay=1):
    print(message)
    time.sleep(delay)

def intro():
    print_pause("You are Detective Holmes, renowned for solving the toughest mysteries.")
    print_pause("Tonight, you've been called to a grand medieval mansion in the UK.")
    print_pause("A murder has taken place, and it's up to you to solve it.")
    print_pause("You arrive at the mansion and are greeted by the butler, who escorts you inside.")

def get_choice(options):
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    choice = input("What would you like to do? ")
    while choice not in [str(i) for i in range(1, len(options) + 1)]:
        choice = input("Please choose a valid option: ")
    return int(choice) - 1

def foyer():
    print_pause("You are in the foyer.")
    print_pause("There are doors leading to the library, the dining room, and upstairs to the bedrooms.")
    if "confront" not in clues:
        options = ["Investigate the library", "Investigate the dining room", "Go upstairs to the bedrooms", "Confront the suspects"]
    else:
        options = ["Investigate the library", "Investigate the dining room", "Go upstairs to the bedrooms"]
    choice = get_choice(options)
    if choice == 0:
        library()
    elif choice == 1:
        dining_room()
    elif choice == 2:
        upstairs()
    elif choice == 3:
        confrontation()

def library():
    print_pause("You enter the library. Rows of ancient books line the walls.")
    print_pause("There is a desk with a letter opener and a half-written letter.")
    options = ["Examine the letter opener", "Read the letter", "Go back to the foyer"]
    choice = get_choice(options)
    if choice == 0:
        print_pause("The letter opener is stained with something dark. Could it be blood?")
        print_pause("You decide to bag it as evidence.")
        clues.append("blood-stained letter opener")
    elif choice == 1:
        print_pause("The letter is an unfinished note addressed to someone named 'Eliza'. It mentions a secret meeting.")
        clues.append("letter to Eliza")
    foyer()

def dining_room():
    print_pause("You enter the dining room. A grand table is set, but there are signs of a struggle.")
    print_pause("There is a shattered glass and a suspicious-looking stain on the carpet.")
    options = ["Examine the broken glass", "Examine the stain", "Go back to the foyer"]
    choice = get_choice(options)
    if choice == 0:
        print_pause("The glass is shattered, but you notice a small piece of cloth caught in the shards.")
        print_pause("Could it be from the suspect's clothing?")
        clues.append("piece of cloth")
    elif choice == 1:
        print_pause("The stain appears to be wine, but mixed with something else... perhaps a drug?")
        clues.append("drugged wine stain")
    foyer()

def upstairs():
    print_pause("You go upstairs. There are three rooms: the master bedroom, a guest room, and the study.")
    options = ["Investigate the master bedroom", "Investigate the guest room", "Investigate the study", "Go back to the foyer"]
    choice = get_choice(options)
    if choice == 0:
        master_bedroom()
    elif choice == 1:
        guest_room()
    elif choice == 2:
        study()
    elif choice == 3:
        foyer()

def master_bedroom():
    print_pause("You enter the master bedroom. It is lavishly decorated, but something feels off.")
    print_pause("There is a safe partially hidden behind a painting.")
    options = ["Try to open the safe", "Look under the bed", "Go back to the upstairs hall"]
    choice = get_choice(options)
    if choice == 0:
        print_pause("You find a combination lock. You try the numbers from the letter in the library... and it opens!")
        print_pause("Inside, you find documents implicating the butler in a series of crimes.")
        clues.append("documents implicating the butler")
    elif choice == 1:
        print_pause("Under the bed, you find a diary. It contains notes about a blackmail plot.")
        clues.append("blackmail diary")
    upstairs()

def guest_room():
    print_pause("You enter the guest room. It appears someone was staying here recently.")
    print_pause("There is a suitcase open on the bed, with clothes strewn about.")
    options = ["Examine the suitcase", "Check the closet", "Go back to the upstairs hall"]
    choice = get_choice(options)
    if choice == 0:
        print_pause("You find a hidden compartment in the suitcase, with a vial of poison inside.")
        clues.append("vial of poison")
    elif choice == 1:
        print_pause("In the closet, you find a set of servant's clothes. Could someone have been disguised?")
        clues.append("servant's clothes")
    upstairs()

def study():
    print_pause("You enter the study. Papers are scattered everywhere, and a window is open.")
    print_pause("There is a map on the desk, marked with several locations.")
    options = ["Examine the map", "Look out the window", "Go back to the upstairs hall"]
    choice = get_choice(options)
    if choice == 0:
        print_pause("The map shows the locations of various meetings. It seems the victim was investigating something important.")
        clues.append("meeting map")
    elif choice == 1:
        print_pause("Looking out the window, you see footprints leading away from the mansion.")
        clues.append("footprints outside window")
    upstairs()

def confrontation():
    print_pause("You have gathered enough evidence to confront the murderer.")
    print_pause("You gather everyone in the foyer to reveal the truth.")
    if "blood-stained letter opener" in clues and "documents implicating the butler" in clues:
        print_pause("All clues point to the butler being the murderer!")
        print_pause("The butler confesses to the crime, stating he was blackmailed by 'Eliza'.")
        print_pause("Congratulations, Detective Holmes! You solved the mystery.")
    else:
        print_pause("You confront the suspects, but something doesn't add up.")
        print_pause("You need more evidence to solve the case. The murderer remains at large.")
    print_pause("Thank you for playing the Detective Mystery Game.")

def main():
    global clues
    clues = []
    intro()
    while True:
        foyer()
        break

main()
