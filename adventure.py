locations = ["sewer", "ditch", "sidewalk"]
sewerItems = ["stick", "diaper", "lighter"]
ditchItems = ["band-aid"]
generalResponses = ["pick up"]
sewerResponses = ["forward", "wait"]
status = {"location": locations[0], "inventory": [sewerItems[1]], "responses": sewerResponses, "action": lambda: None}
nearbyItems = [sewerItems[0]]
response = ""
def doAction():
    status["action"]
def checkItems():
    print("You have:")
    for item in status["inventory"]:
        print(item + " ")
    read()
def checkLocation():
    print("Your location is: " + status["location"])
    read()
def checkNearbyItems():
    print("You see: ")
    for item in nearbyItems:
        print(item + " ")
    read()
def checkOptions():
    global status
    print("Your current abilities are: ")
    print(",".join(generalResponses) + ", " + ",".join(status["responses"]))
def read():
    global response
    response = input()
    if response == "items":
        checkItems()
    elif response == "location":
        checkLocation()
    elif response == "nearby":
        checkNearbyItems()
    elif response == "pick up":
        pickupItem()
    elif response == "help":
        checkOptions()
    else:
        doAction()
def pickupItem():
    global status
    global nearbyItems
    print("what would you like to pick up?")
    print(",".join(nearbyItems))
    item = input()
    if item in nearbyItems:
        status["inventory"].append(item)
    else:
        print("I don't see that item...")
        read()
def showOptions():
    global status
    print("You can: ")
    print(",".join(status["responses"]))
def enterDitch():
    global nearbyItems
    global status
    nearbyItems = ditchItems
    print("You find yourself soaked standing in a ditch now.")
    showOptions()
    read()
def checkSewer():
    global status
    read()
    if response == status["responses"][0]:
        print("You stepped in a puddle")
        status["action"] = sewerAction
        showOptions()
        read()
    elif response == status["responses"][1]:
        print("You wait for a minute")
        print("A giant rush of water washes you away.")
        enterDitch()
    else:
        print("I'm sorry, I didn't catch that? (This ditch has an awful echo)...")
        doAction()
def sewerAction():
    print("")
def enterSewer():
    global nearbyItems
    global status
    nearbyItems = sewerItems
    status["location"] = locations[0]
    status["responses"] = sewerResponses
    status["action"] = checkSewer
    print("You are in a sewer. It is pitch black. Would you like to go forward, or wait?")
    showOptions()
    checkSewer()

print("Super adventure!")
enterSewer()