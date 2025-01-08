class Student:
    name="sahil"
    prnNo=130
    className="it"

    def __init__(self,name,prn_no,class_name):
        self.name=name
        self.prnNo=prn_no
        self.className=class_name

    def get_Info(self):
        print(f"Youe name is {self.name} and your prn no is {self.prnNo} and your class is {self.className}")

    @staticmethod
    def greet():
        print("Hello how are you ")

sahil=Student("Sahil Omanwar",12345,"Information Technology")
sahil.get_Info()
sahil.greet()

pranav=Student("Pranav Revanwar",1010101,"Research")
pranav.get_Info()
pranav.greet()

