def start_adventure():
    """Starts the text-based adventure."""

    print("Welcome to your adventure!")
    print("You find yourself standing at a crossroads.")
    print("To your left, you see a dark forest.")
    print("To your right, you see a sparkling river.")

    choice = input("Do you go left or right? (left/right): ")

    if choice.lower() == "left":
        go_to_forest()
    elif choice.lower() == "right":
        go_to_river()
    else:
        print("Invalid choice. You stand there, confused.")

def go_to_forest():
    """The adventure in the forest."""

    print("You enter the dark forest. It's very spooky!")
    print("You hear a rustling sound in the bushes.")

    choice = input("Do you investigate or run? (investigate/run): ")

    if choice.lower() == "investigate":
        print("You find a friendly squirrel! It gives you a nut.")
    elif choice.lower() == "run":
        print("You run away and trip over a root. Ouch!")
    else:
        print("You just stand there, unsure what to do.")

def go_to_river():
    """The adventure by the river."""

    print("You walk along the sparkling river. It's very peaceful.")
    print("You see a shiny object in the water.")

    choice = input("Do you pick it up or leave it? (pick/leave): ")

    if choice.lower() == "pick":
        print("You find a magic coin! It sparkles in your hand.")
    elif choice.lower() == "leave":
        print("You decide to leave it. Maybe it's not safe.")
    else:
        print("You stand there, staring at the river.")

start_adventure()