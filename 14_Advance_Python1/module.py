def myFunc():
    print("Hello Sahil")

##if module.py runs this function  the output will be main
if(__name__=="__main__"):#If this code is directly executed by running the file present in
    print("We are directly running this code")
    myFunc()

    print(__name__)