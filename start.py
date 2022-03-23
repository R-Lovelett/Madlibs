def newGame():
    print("Hello! Welcome to Madlibs!\n")

    while True:
        try:
            print("1. Short story")
            print("2. Medium story")
            storySelect = int(input("Select a story that you would like to use:"))
        except ValueError:
            print("Sorry, I didn't understand that. Please try again.")
            continue
    
        if storySelect == 1:
            print("Num 1")
            break
        elif storySelect == 2:
            print("Num 2")
            break

newGame()