#class train which has methods to book a ticket ,get status(no of seats) and fare info of running train
import random


class Railway:


    def __init__(self,trainNo):
        self.trainNo=trainNo
    def book(self,fro,to):
        print(f"Ticket is book in train no : {self.trainNo} from {fro} to {to}")
    def getStatus(self):
        print(f"train no : {self.trainNo} is running on time ")

    def getFare(self,fro,to):
        print(f"Ticket fare in train no : {self.trainNo} from {fro} to {to} is {random.randint(1000,5000)}")



t=Railway(12020)
t.book("Pusad","Pune")
t.getStatus()
t.getFare("Pusad","Pune")