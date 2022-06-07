import os
import sys

# don't know why i put it in a class
class project:
    def new(template):
        if template == "d":
            os.system("git clone https://github.com/lata-lang/Lata.git")
            # folders related to the github repo be die
            os.system("rm -rf Lata/.git")
            os.system("rm -rf Lata/CLI")
            os.system("rm -rf Lata/.gitignore")

print("Lata CLI 0.0.1")
# get the command line arguments
args = sys.argv

# if the user wants to create a new project, then create it
if args[1] == "new":
    project.new(args[2])
    # if the user specifies they use vscode, then use it 
    if args[3] == "vscode":
        os.system("code Lata")