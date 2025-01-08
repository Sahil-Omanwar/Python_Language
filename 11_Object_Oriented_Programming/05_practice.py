#create a class programmer for storing information of few programmer working in office

class Programmer:
    company="Microsoft"

    def __init__(self,name,majors,tech):
        self.name=name
        self.majors=majors
        self.tech=tech

    def getInfo(self):
        print(f"Company:{self.company} \nName:{self.name} \nMajors:{self.majors} \nTech Stack:{self.tech}")


sahil=Programmer("Sahil","information Technology","AIML")
sahil.getInfo()
pranav=Programmer("Pranav","Research","Research Field")
pranav.getInfo()