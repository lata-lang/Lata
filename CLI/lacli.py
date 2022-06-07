import os
import sys

class project:
    def new(template):
        if template == "d":
            print("Default Lata Template")

print("Lata CLI 0.0.1")
# get the command line arguments
args = sys.argv

if args[1] == "new":
    project.new(args[2])
    os.system("git clone https://github.com/lata-lang/Lata.git")