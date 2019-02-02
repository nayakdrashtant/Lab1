def totalcost(price,discount,firstcost,othercost,copies):
    price = float(price)
    discount = int(discount)/100
    firstcost = int(firstcost)
    othercost = float(othercost)
    copies = int(copies)
 #   checkdiscount = float(price - float(price * discount))
    a_disc = float(price * discount / 100)
    a_disc = price - a_disc
    firstcopy = float(a_disc + firstcost)
    othercopies = int(copies - 1)
    total =  a_disc * othercopies
    total = total + firstcopy   
 #   total = firstcopy + int(checkdiscount) * int(othercost)
    return total

price = input("enter price:")
discount = input("enter discount:")
firstcost = input("enter shipping cost for first copy:")
othercost = input("enter shipping cost for other copies:")
copies = input("enter no of copies:")
print(totalcost(price,discount,firstcost,othercost,copies))
