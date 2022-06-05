import sys



def main():
    # get the file name
    fileName = sys.argv[1]
    # open the file
    file = open(fileName, "r")
    # actual interpreter
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
