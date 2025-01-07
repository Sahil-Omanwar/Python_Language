#similar to question 4 .but here we are provided list
words=["Donkey","gande","gade"]


with open("Donkey_word.txt","r") as f:
    content=f.read()
for word in words:
     content=content.replace(word,"#"*len(word))

with open("Donkey_word.txt","w")as f:
    f.write(content)