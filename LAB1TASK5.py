def seperate():
    print("+","-","-","-","+","-","-","-","+")

def lines(row):
    for i in range(int(row)):
        print("|"," "," "," ","|"," "," "," ","|")

def grid(row):
    seperate()
    lines(row)
    seperate()
    lines(row)
    seperate()

grid(4)	
