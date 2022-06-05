def main():
    # get the file name
    fileName = input("Enter the file name: ")
    # open the file
    file = open(fileName, "r")
    # check lines and shit
    for line in file:
        if line.find("//") != -1:
            line = line.replace("//", "#")
        if line.find("@python") != -1:
            line = line.replace("@python", "")
        if line.find("@") != -1:
            line = line.replace("@", "")
        if line.find("\n") != -1:
            line = line.replace("\n", "")
        print("lata. " + line)

    # rename the file extension to .py
    fileName = fileName.replace(".lata", ".py")
    # close the file
    file.close()
