# 1. Basic File Read & Write
# ● Create a text file and write multiple lines into it
# ● Read the contents of the file and display them on the screen
# ● Handle the case where the file does not exist using try-except

try:
    with open("q1.txt", "w") as f:
        f.write("This is the first line.\n")
        f.write("Yo arko line ho.\n")
        f.write("Ye doosra line hai.\n")

    with open("q1.txt", "r") as f:
        lines = f.readlines()
    for i in lines:
        print(i)

except FileNotFoundError:
    print("File not found")