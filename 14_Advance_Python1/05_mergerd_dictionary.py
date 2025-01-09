##mergingn 2 dictionaries

dict1={
    'a':1,
    'b':2
}
dict2={
    'c':3,
    'b':5
}

mergerd1=dict1 | dict2
mergerd2=dict2 | dict1
print(mergerd1)
print(mergerd2)