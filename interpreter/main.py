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
            input()
        if ";" in line:
            print("Error: Contains semicolon")
            print("Hint: Don't use semicolons. It's not that hard.")
            print(" --------------------------------------------------")
            print("|  print(Hello, Latty!;                            |")
            print("|        _____________^_                           |")
            print("|       |EW. SEMICOLONS.|                          |")
            print("|       |_______________|                          |")
            print(" --------------------------------------------------")
            exit()
    # close the file
    file.close()


main()
