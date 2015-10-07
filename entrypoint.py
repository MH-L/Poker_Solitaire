__author__ = 'Minghao'
INVALID_CHOICE_CONSTANT = 0

def main():
    print "The Poker Game is starting."
    print "Please enter 1 for normal game, 2 for hearts game,\n" \
          "and 3 for UPLevel game."
    choice = raw_input("Please enter your choice.")
    try:
        choice = int(choice)
    except ValueError:
        choice = INVALID_CHOICE_CONSTANT
    while choice not in [1,2,3]:
        choice = raw_input("Invalid option. Please enter again.")
        try:
            choice = int(choice)
        except ValueError:
            choice = INVALID_CHOICE_CONSTANT

    if choice == 1:
        startNormalGame()
    elif choice == 2:
        startHeartGame()
    else:
        startUPLevelGame()

def startNormalGame():
    pass

def startHeartGame():
    pass

def startUPLevelGame():
    pass

if __name__ == "__main__":
    main()
