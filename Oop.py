import os

myDic = {
    "employees": 
    [
        {"name": "Jacob", "age":24, "income":4500},
        {"name": "Justin", "age":23, "income":4200},
        {"name": "Austin", "age":29, "income":5200},
        {"name": "Rabo", "age":28, "income":5000},
        {"name": "Cheryl", "age":40, "income":9000},
        {"name": "Cindel", "age":35, "income":7500},
        {"name": "Alex", "age":39, "income":8500},
        {"name": "Alv", "age":58, "income":19500}
    ],
    "students": 
    [   
        {"name": "Jacob", "age":17, "major":"CS"},
        {"name": "Peter", "age":16, "major":"CS"},
        {"name": "Antony", "age":18, "major":"EC"},
        {"name": "Rex", "age":19, "major":"EC"},
        {"name": "Cheryl", "age":22, "major":"EC"},
        {"name": "Wiss", "age":17, "major":"EC"},
        {"name": "Jack", "age":18, "major":"CS"},
        {"name": "Annie", "age":21, "major":"EC"}
    ],
    "series": 
    [   
        {"name": "Jacob", "age":3, "major":"CS"},
        {"name": "Peter", "age":6, "major":"CS"},
        {"name": "Antony", "age":12, "major":"EC"},
        {"name": "Rex", "age":24, "major":"EC"},
        {"name": "Wiss", "age":96, "major":"EC"}
    ]
}

# Encapsulation - properties and methods inside a class
class infoDetail:

    def __init__(self, dic):
        self.dic = dic

    def totalEmployees(self):
        return len(myDic["employees"])
    
    def totalStudents(self):
        return len(myDic["students"])
    
    def totalSeries(self):
        return len(myDic["series"])
    
    def findOddFunction(self):
        oddAgeArr = []
        for i in range(self.totalEmployees()):
            if (self.dic["employees"][i]["age"] % 2) != 0:
                oddAgeArr.append(self.dic["employees"][i]["age"])
        return oddAgeArr
    
    def findSeriesFunction(self):
        serNumbers = [0] * 6
        serNumbers[0] = self.dic["series"][0]["age"]
        for i in range(1, self.totalSeries()):
            if(self.dic["series"][i]["age"] - self.dic["series"][i-1]["age"] != self.dic["series"][i-1]["age"]):
                serNumbers[i] = self.dic["series"][i-1]["age"] * 2
                serNumbers[i+1] = self.dic["series"][i]["age"]
            else:
                serNumbers[i] = self.dic["series"][i]["age"]
        return serNumbers
    
    def findPrimeFunction(self):
        iflag = True
        primeNumArr = [0] * 3
        x = 0
        for i in range(self.totalStudents()):
            for j in range(2, self.dic["students"][i]["age"]):
                if self.dic["students"][i]["age"] % j == 0:
                    iflag = False
                    break
            if iflag == True:
                primeNumArr[x] = self.dic["students"][i]["age"]
                x += 1
            iflag = True
        return primeNumArr
    
    def giveNumber(self):
        print("Number 1")

# inheritance and polymorphism
class baseClass(infoDetail):
    def giveNumber(self):
        print("Number 2")

if __name__ == "__main__":
    print("Initial ...")

    myInstance = infoDetail(myDic)
    print("totalEmployees: " + str(myInstance.totalEmployees()))
    print("totalStudents: " + str(myInstance.totalStudents()))
    print("totalSeries: " + str(myInstance.totalSeries()))
    print("oddAge: " + str(myInstance.findOddFunction()))
    print("seriesNumber: " + str(myInstance.findSeriesFunction()))
    print("primeNumber: " + str(myInstance.findPrimeFunction()))

    num = baseClass(myDic)
    num.giveNumber()

###
#$ python Oop.py 
#Initial ...
#totalEmployees: 8
#totalStudents: 8
#totalSeries: 5
#oddAge: [23, 29, 35, 39]
#seriesNumber: [3, 6, 12, 24, 48, 96]
#primeNumber: [17, 19, 17]
#Number 2
###