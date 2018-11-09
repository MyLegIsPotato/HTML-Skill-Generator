try:
    file = open("output.txt", "a")
except:
    file = open("output.txt", "x")

mode = input("Select mode ('a' for advanced, 'b' for basic, 'h' for help): ")

if mode == "help":
    print("--------------------------")
    print("Advanced mode means that you are prompt for both 'full star' and 'empty star' symbol (Or whatever else you type in) and also your max. skill points count.")
    print("Basic mode means that generated code will contain simple empty/full star rating.")
    print("--------------------------")
elif mode == "a":
    starOff = input("'Empty star': ")
    starOn = input("'Full star': ")

while mode == "a":
    print("Type 'exit' to close program.")
    name = input("Skill name: ")
    if name == "exit":
        exit(0)
        file.close()
    maxSkill = input("Max. symbols count: ")
    msg = "Rating (1-" + str(maxSkill) + "): "
    level = input(msg)
    
    output = name + " "
    for x in range(0, int(maxSkill)+1):
        if x <= int(level):
            output += starOn
        elif x > int(level) and x < int(maxSkill):
            output += starOff
        elif x == int(maxSkill):
            output += "<br/>" + "\n"
        
    file.write(str(output))

while mode == "b":
    print("Type 'exit' to close program.")
    name = input("Skill name: ")
    if name == "exit":
        exit(0)
        file.close()


    level = int(input("Rating (1-3): "))
    if level == 1:
        output = name + " " + "&#9733;" + "&#9734;" + "&#9734;" + "<br/>" + "\n"
    elif level == 2:
        output = name + " " + "&#9733;" + "&#9733;" + "&#9734;" + "<br/>" + "\n"
    elif level == 3:
        output = name + " " + "&#9733;" + "&#9733;" + "&#9733;" + "<br/>" + "\n"
    else:
        print("Invalid rating number")
    file.write(str(output))
