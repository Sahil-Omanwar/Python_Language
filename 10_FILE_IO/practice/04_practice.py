#A file contain "Donkey" word multiple times  You need to write program which replace thsi word in #####
# by updating same file

word="Donkey"

with open("Donkey_word.txt","r") as f:
    content=f.read()
    content_new=content.replace(word,"####")

with open("Donkey_word.txt","w")as f:
    f.write(content_new)
