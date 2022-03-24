light = "\033[96;4m" # Highlight user input text
end= "\033[0;0m" #Remove highlight

def newGame():
    print("Hello! Welcome to Madlibs!\n")

    # Until player enters  1 or 2, keep asking player to select story
    while True:
        try:
            print("1. Short story")
            print("2. Medium story\n")
            storySelect = int(input("Select a story that you would like to use (#): "))
        except ValueError: # If somehow the input isnt recognized, loop again
            print("Sorry, I didn't understand that. Please try again.")
            continue

        #Select corresponding story based on user input
        if storySelect == 1:
            shortStory()
            break
        elif storySelect == 2:
            medStory()
            break

def shortStory():
    noun_List = {}
    adj_List = {}
    verb_List = {}
    x = 1

    print("Time for a short story!\nPlease answer the following "
        "prompts in order to complete the story!\n")

    # Ask user for 3 of each category: nouns, adjectives, and verbs
    while x < 10:
        if x <= 3:
            noun_List[x] = input("Enter a noun: ").upper()
        if x <= 6 and x > 3:
            adj_List[x] = input("Enter a adjective: ").upper()
        if x <= 9 and x > 6:
            verb_List[x] = input("Enter a verb: ").upper()
        x += 1

    #Printed out final story
    print(f"\nOur school cafeteria has really {light}{adj_List[4]}{end} food.")
    print(f"Just thinking about it makes my stomach {light}{verb_List[7]}{end}. The spaghetti ")
    print(f"is {light}{adj_List[5]}{end} and tastes like {light}{noun_List[1]}{end}. One day, I swear the meatballs")
    print(f"started to {light}{verb_List[8]}{end}! The turkey tacos are totally {light}{adj_List[6]}{end} and kind")
    print(f"of look like old {light}{noun_List[2]}{end}. Don't get me started on the hoagies, I")
    print(f"would rather {light}{verb_List[9]}{end} to {light}{noun_List[3]}{end} before taking a bite of one!")

    while True:
        try: 
            response = input("\nDo you want to play again? ").lower()
        except ValueError:
            print("Sorry, I didn't understand that. Please try again.")
            continue

        if response == "y" or response == "yes":
            newGame()
            break
        elif response == "n" or response == "no":
            break

def medStory():
    noun_List = {} #There are 5 nouns
    adj_List = {} #There are 7 adjectives
    past_Verb = {} #There are 3 past verbs
    verb_List = {} #There are 3 verbs
    food = ""
    place = ""
    song = ""
    clothing = ""
    x = 1

    print("\nTime for a medium story!\nPlease answer the following "
        "prompts in order to complete the story!\nThere will "
        "be some more unique prompts in this one!\n")

    while x < 23:
        if x < 6:
            noun_List[x] = input("Enter a noun: ").upper() # Keys: 1-5
        if x < 13 and x >= 6:
            adj_List[x] = input("Enter an adjective: ").upper() # Keys: 6-12
        if x < 16 and x >= 13:
            verb_List[x] = input("Enter a verb: ").upper() # Keys: 13-15
        if x < 19 and x >= 16:
            past_Verb[x] = input("Enter a verb in the past tense: ").upper() # Keys: 16-18
        if x == 19:
            food = input("Enter favorite food item: ").upper() 
        if x == 20:
            place = input("Enter a place: ").upper()
        if x == 21:
            song = input("Enter the name of a song: ").upper()
        if x == 22:
            clothing = input("Enter a piece of clothing (Ex: shirt): ").upper()
        x += 1

    print(f"\nIt was a {light}{adj_List[6]}{end} sunny day. {light}{noun_List[1]}{end} and I were excited to go camping at {light}{place}{end}.")
    print(f"It was my first time going there. I packed my favorite {light}{clothing}{end}. It is {light}{adj_List[7]}{end}")
    print(f"and {light}{adj_List[8]}{end}, perfect for camping! On the road we went in our {light}{adj_List[9]}{end} {light}{adj_List[10]}{end} van! We were")
    print(f"listening to {light}{song}{end} all the way down. The drive was about 5 hours but it was")
    print(f"so worth it. When we got there we unpacked the van. I could smell {light}{food}{end} being cooked.")
    print(f"It smelled {light}{adj_List[11]}{end}. I {light}{past_Verb[16]}{end} to the room I was staying in with my {light}{noun_List[2]}{end}. The next")
    print(f"thing I knew, {light}{noun_List[3]}{end} came and {light}{past_Verb[17]}{end} on the bed. I heard my mom scream, \"Get off the bed!\"")
    print(f"I {light}{past_Verb[18]}{end} outside. I saw {light}{noun_List[4]}{end}. It was {noun_List[5]}. Over the next few days I got to {light}{verb_List[13]}{end},")
    print(f"{light}{verb_List[14]}{end}, and {light}{verb_List[15]}{end}. My camping trip was {light}{adj_List[12]}{end}.")

    while True:
        try: 
            response = input("\nDo you want to play again? ").lower()
        except ValueError:
            print("Sorry, I didn't understand that. Please try again.")
            continue

        if response == "y" or response == "yes":
            newGame()
            break
        elif response == "n" or response == "no":
            break

newGame()