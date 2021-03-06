import sys


def main():
    # get the file name
    fileName = sys.argv[1]
    # open the file
    file = open(fileName, "r")
    # actual interpreter
    linfes = 0
    for line in file:
        linfes += 1
        if "write" in line:
            print(line[line.find("write")+6:])
        if "//" in line:
            continue
        if "read" in line:
            input(line[line.find("read")+5:])
        if "@py" in line:
            # python interop
            exec(line[line.find("@py")+3:])
        if ";" in line:
            print("Error: Contains semicolon")
            print("on line: " + str(linfes))
            print(" --------------------------------------------------")
            print("|  print(Hello, Latty!;                            |")
            print("|              _______^_                           |")
            print("|             |Semicolon|                          |")
            print("|             |_________|                          |")
            print(" --------------------------------------------------")
            exit()
    # close the file
    file.close()


main()
