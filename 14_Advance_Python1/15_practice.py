#write a programme to open three files 1.txt 2.txt 3.txt if anu files are no tpresent ,a messsage without exiting the must be printed prompting the same

try:
    with open("1.txt") as f1, open("2.txt") as f2, open("3.txt") as f3:
        print(f1.read())
        print(f2.read())
        print(f3.read())
except FileNotFoundError as e:
    print(f"Error: {e.filename} not found.")