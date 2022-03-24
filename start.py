def newGame():
    print("Hello! Welcome to Madlibs!\n")

    # Until player enters  1 or 2, keep asking player to select story
    while True:
        try:
            print("1. Short story")
            print("2. Medium story\n")
            storySelect = int(input("Select a story that you would like to use:"))
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
        "prompts in order to complete the story!")

    # Ask user for 3 of each category: nouns, adjectives, and verbs
    while x < 10:
        if x <= 3:
            noun_List[x] = input("Enter a noun: ")
        if x <= 6 and x > 3:
            adj_List[x] = input("Enter a adjective: ")
        if x <= 9 and x > 6:
            verb_List[x] = input("Enter a verb: ")
        x += 1

    #Printed out final story
    print(f"\nOur school cafeteria has really {adj_List[4]} food.")
    print(f"Just thinking about it makes my stomach {verb_List[7]}. The spaghetti ")
    print(f"is {adj_List[5]} and tastes like {noun_List[1]}. One day, I swear the meatballs")
    print(f"started to {verb_List[8]}! The turkey tacos are totally {adj_List[6]} and kind")
    print(f"of look like old {noun_List[2]}. Don't get me started on the hoagies, I")
    print(f"would rather {verb_List[9]} to {noun_List[3]} before taking a bite of one!")

def medStory():
    print("Medium story here.")

    noun_List = {} #There are 5 nouns
    adj_List = {} #There are 7 adjectives
    past_Verb = {} #There are 3 past verbs
    verb_List = {} #There are 3 verbs
    food = ""
    place = ""
    song = ""
    clothing = ""
    x = 1

    while x < 23:
        if x < 6:
            noun_List[x] = input("Enter a noun: ") # 1-5
        if x < 13 and x >= 6:
            adj_List[x] = input("Enter an adjective: ") # 6-12
        if x < 16 and x >= 13:
            verb_List[x] = input("Enter a verb: ") # 13-15
        if x < 19 and x >= 16:
            past_Verb[x] = input("Enter a verb in the past tense: ") # 16-18
        if x == 19:
            food = input("Enter favorite food item: ") 
        if x == 20:
            place = input("Enter a place: ")
        if x == 21:
            song = input("Enter the name of a song: ")
        if x == 22:
            clothing = input("Enter a piece of clothing (Ex: shirt): ")
        x += 1

    # TODO add story here

    print(f"\nIt was a {adj_List[6]} sunny day. {noun_List[1]} and I were excited to go camping at {place}.")
    print(f"It was my first time going there. I packed my favorite {clothing}. It is {adj_List[7]}")
    print(f"and {adj_List[8]}, perfect for camping! On the road we went in our {adj_List[9]} {adj_List[10]} van! We were")
    print(f"listening to {song} all the way down. The drive was about 5 hours but it was")
    print(f"so worth it. When we got there we unpacked the van. I could smell {food} being cooked.")
    print(f"It smelled {adj_List[11]}. I {past_Verb[16]} to the room I was staying in with my {noun_List[2]}. The next")
    print(f"thing I knew, {noun_List[3]} came and {past_Verb[17]} on the bed. I heard my mom scream, \"Get off the bed!\"")
    print(f"I {past_Verb[18]} outside. I saw {noun_List[4]}. It was {noun_List[5]}. Over the next few days I got to {verb_List[13]},")
    print(f"{verb_List[14]}, and {verb_List[15]}. My camping trip was {adj_List[12]}.")

newGame()