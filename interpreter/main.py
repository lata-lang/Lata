def main():
    # get the file name
    fileName = input("Enter the file name: ")
    # open the file
    file = open(fileName, "r")
    # if it contains write, then print the words after write, and ignore the line if the line contains //
    for line in file:
        if "write" in line:
            print(line[line.find("write")+6:])
        if "//" in line:
            continue
        if "read" in line:
            input()
    # close the file
    file.close()


main()
