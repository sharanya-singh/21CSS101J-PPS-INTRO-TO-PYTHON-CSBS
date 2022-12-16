elif(game=='Hangman'):
    print("Below is a game of hangman")
    print("Enter the names of players")
    player1 = input("Player1: ")
    player2 = input("Player2: ")
    print(player1, " enter a word for ", player2, " to guess")
    ip = (input("Enter the word"))  # ip stores the word input by player1
    nchar = 0
    for char in ip:  # this for loop calculates the number of characters in the word
        nchar = nchar + 1
        print("The word has", nchar, " characters")

        print("Guess the characters: ")  # the guessing game starts here

        guesses = ''  # all the guesses are stored here
        chances = 12  # any number of turns can be used here

    while chances > 0:
        wchar = 0  # counts the number of times a wrong character is input
        for char in ip:  # comparing that character with the characters in guesses
            if char in guesses:
                print(char)
            else:
                print("_")
                wchar += 1  # for every wrong input wchar is incremented

        if wchar == 0:
            print("You Win")  # if there is no wrong input the player wins
            print("The word is: ", ip)  # this prints the correct input
            break

    # if player has input the wrong alphabet then it will ask the player to input again
        guess = input("guess a character: ")
        guesses += guess  # every input character will be stored in guesses
        if guess not in ip:  # check input with the character in word
            chances -= 1
            print("Wrong")  # if the character does not match , wrong is given as output
            print("You have", + chances, 'more chances')  # prints the number of chances left for the user
        if chances == 0:
            print("You Loose")
            print("The word is: ", ip)  # this prints the correct input
else:
    print("Invalid Try Again")
