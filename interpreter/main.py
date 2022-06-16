import sys
import error

def main():
    # get the file name
    fileName = sys.argv[1]
    # open the file
    file = open(fileName, "r")
    # actual interpreter
    linfes = 0
    for line in file:

        if ";" in line:
            error.error("1semi")

        linfes += 1
        if "varstr" in line:
            # i guess declare a variable?
            varName = line.split(" ")[1]
            # get the value
            varValue = line.split(" ")[2]

            varRef = "<ref>" + varName + "</ref>"
            # this won't be able to be refrenced in future code 
            # so i'll leave it here for the future
       
        
        if "write" in line:
            if varRef in line:
                # this prints out the value of
                print(varValue)
            # this works much better
            print(line[line.find(".")+1:], end="")
            
        if "//" in line:
            continue
        if "read" in line:
            print(line[line.find(".")+1:], end="")
        if "@py" in line:
            # python interop
            exec(line[line.find("@py")+3:])
        # i'll have an error check in the future that runs before the interpreter
        # additional commands
        if "exit" in line:
            exit()


    # close the file
    file.close()


main()