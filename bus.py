class Bus:

    def __init__(self,people,fare):
        self.people = people
        self.fare = fare

    def __str__(self):
        return f'จำนวนผู้โดยสาร :{self.people} คน, ค่าโดยสาร = {self.fare} บาท'
    
    def __lt__(self,rhs):
        return self.people*self.fare < rhs.people*rhs.fare
    
    def people_in(self,n):
        self.people += n

    def people_out(self,n):
        # self.people = self.people - n
        self.people = max(0,self.people - n)

    def change_fare(self,new_fare):
        self.fare = new_fare

b1 = Bus(10,5)
b2 = Bus(8,7)

if b1 < b2 :
    print(b1)
else :
    print(b2)

b1.people_in(3)
b1.people_out(6)
b1.change_fare(12)
print(b1)
b1.people_out(7)
print(b1)
b1.people_out(5)
print(b1)

