#import random then use randint or 
from random import randint
class train:
    def __init__(self):
        print("welcome")
    def getstatus(self,trainno,fro,to):
        print(f"the train {trainno} is succesfully booked from {fro} to {to}")
    def getfare(self):
        print("the fare is ", randint(1000,3000))
suhaan=train()
suhaan.getstatus(1234,"jaipur","china")

#or
"""
from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(harry, fro, to):
        print(f"Ticket is booked in train no: {harry.trainNo} from {fro} to {to}") 

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time") 

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")  


t = Train(12399)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")
"""
    
        