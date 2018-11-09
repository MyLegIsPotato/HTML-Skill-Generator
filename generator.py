try:
    file = open("output.txt", "a")
except:
    file = open("output.txt", "x")

while True:
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
