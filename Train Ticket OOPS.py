class Passenger:
    def __init__(self,num,name,age):
        self.passengerId=num
        self.passengerName=name
        self.passengerAge=int(age)
        
    def __repr__(self):
        return f"************************\nPassenger Id: {self.passengerId}\nPassenger Name:{self.passengerName}\nPassenger Age:{self.passengerAge}\n************************"

class Ticket:   
    def __init__(self,tiktype,travtype,travdest,numbpass):
        global ticketId
        self.date="2020-12-09"    
        self.ticketType=tiktype
        self.travelType=travtype
        self.travelDest=travdest
        self.numberpassengers=numbpass
        self.value=0
        self.tikid=ticketId
        self.n=self.get_number()
        ticketId+=1

    def totalfare(self):
        global trainList
        global tainIdPriceTatkal
        global tainIdPriceGen
          
        if self.ticketType=="general":
            if self.travelType[0]=="o" or "O":
                self.value=tainIdPriceGen[self.n]*self.numberpassengers
                return f"{self.value}"
            else:
                self.value=tainIdPriceGen[self.n]*self.numberpassengers
                return f"{(self.value)*2}"

        else:
            if self.travelType[0]=="o" or "O":
                self.value=tainIdPriceTatkal[self.n]*self.numberpassengers
                return f"{self.value}"
            else:
                self.value=tainIdPriceTatkal[self.n]*self.numberpassengers
                return f"{(self.value)*2}"
         
    def get_number(self):
        global trainIdList
        for i in range(len(trainList)):
            if self.travelDest.upper()==trainList[i]:
                return i
            

    def passengerprint(self):
        for p in (globals()[f"passengersofticket{self.tikid}"]):
            print(globals()[p])
        
    def __repr__(self):
        global trainIdList
        if self.n is not None:
            return f"************************\nDate:{self.date}\nTicket ID:{self.tikid}\nTrain ID:{trainIdList[self.n]}\nTicket Type:{self.ticketType}\nTravel Type:{self.travelType}\nTravel Destination:{self.travelDest}\nTotal Fare:{self.totalfare()}\n************************"
        else:
            return "We cannot book tickets."            
ticketId=1
trainList=["MUM-GOA","DEL-MUM","LKO-KOL","MUM-DEL","GOA-MUM","KOL-LKO"]
trainIdList=[1221,2331,7654,5690,5463,9854]
tainIdPriceGen=[100,200,300,400,500,600]
tainIdPriceTatkal=[700,800,900,100,1100,1200]
ticket=[]

numberoforders=int(input())
for numoford in range(1,numberoforders+1):
    tikty=input()
    travty=input()
    dest=input()
    noftik=int(input())
    globals()[f"ticket{numoford}"]=Ticket(tikty,travty,dest,noftik)
    ticket.append(f"ticket{numoford}")
    globals()[f"passengersofticket{numoford}"]=[]

    for j in range(1,noftik+1):
        passid=int(input())
        passname=input()
        passage=int(input())
        globals()[f"passenger{numoford}{j}"]=Passenger(passid,passname,passage)
        (globals()[f"passengersofticket{numoford}"]).append(f"passenger{numoford}{j}")

for item in ticket:
    print((globals()[item]))
    (globals()[item]).passengerprint()



