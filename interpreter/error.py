def error(calliD):
    print("Error: " + calliD)
    if calliD == "1semi":
        print("You can't have semicolons.")
        print("Example of bad code:")
        print("----------------------------")
        print("|   varstr var1 = coffin;  |") 
        print("----------------------------")
        print("Good code:")
        print("----------------------------")
        print("|   varstr var1 = coffin   |")
        print("----------------------------")
    exit()
    # this is the error function

