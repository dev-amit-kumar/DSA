file = open("file.txt", "r")

listOfLines = file.readlines()

for line in listOfLines:
    print(line, end="")
file.close()
