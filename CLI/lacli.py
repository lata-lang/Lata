import os
import sys

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

if args[1] == "new":
    project.new(args[2])
    if args[3] == "vscode":
        os.system("code Lata")