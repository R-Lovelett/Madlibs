def newGame():
	print("Hello! Welcome to Madlibs!\n")

	while True: # Until player enters number for story selection, keep asking player to select story
		try:
			print("1. Short story")
			print("2. Medium story\n")
			storySelect = int(input("Select a story that you would like to use:"))
		except ValueError: # If somehow the input isnt recognized, loop again
			print("Sorry, I didn't understand that. Please try again.")
			continue

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

	while x < 10:
		if x <= 3:
			noun_List[x] = input("Enter a noun: ")
		if x <= 6 and x > 3:
			adj_List[x] = input("Enter a adjective: ")
		if x <= 9 and x > 6:
			verb_List[x] = input("Enter a verb: ")
		x += 1

	print(f"\nOur school cafeteria has really {adj_List[4]} food.")
	print(f"Just thinking about it makes my stomach {verb_List[7]}. The spaghetti ")
	print(f"is {adj_List[5]} and tastes like {noun_List[1]}. One day, I swear the meatballs")
	print(f"started to {verb_List[8]}! The turkey tacos are totally {adj_List[6]} and kind")
	print(f"of look like old {noun_List[2]}. Don't get me started on the hoagies, I")
	print(f"would rather {verb_List[9]} to {noun_List[3]} before taking a bite of one!")

def medStory():
	print("Medium story here.")

newGame()