marks={
    "Sahil":90,
    "Pranav":100,
    "Humayun":95

}

#items
print(marks.items())

#keys
print(marks.keys())

#values
print(marks.values())

#update
marks.update({"Sahil":92})
print(marks)

marks.update({"Humayun":97,"Shubham":87})
print(marks)

#get
print(marks.get("Sahil"))#if not found then it gives error 
