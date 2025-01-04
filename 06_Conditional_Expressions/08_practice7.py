p1="Make a lot of Money"
p2="buy now"
p3="subscribe this"
p4="click this"

message =input("Pls eneter your message : ")

if (p1 in message)or(p2 in message) or(p3 in message) or(p4 in message):
    print("This message is probable scam")
else:
    print("This is not a scam message")