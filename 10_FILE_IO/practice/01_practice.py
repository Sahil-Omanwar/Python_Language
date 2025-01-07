#programme to read file form poems.txt and find out whether it contains word twinkel

with open("poems.txt") as f:
    data=f.read()
    if("twinkle" in data):
        print("Yes word twinkle is present in poem")
    else:
        print("No such word present in poem")