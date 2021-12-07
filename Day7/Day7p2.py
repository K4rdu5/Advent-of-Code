#Day 7 part 2
import statistics
import math

data = open("DataDay7.txt", "r").read().split(",")
crabs = [int(crab) for crab in data]

#Get position
mean = statistics.mean(crabs)
pos = round(statistics.mean(crabs))

#Solved my problem, but I'm not certain it will work for any data set.
fraction, whole = math.modf(mean)
if fraction >= .5:
    pos = round(pos-1)

#Calculate fuelcost
fuelcost = []
for d in crabs:
    distance = int(math.fabs(d-pos))
    fuelreq = sum(range(distance+1))
    # print(f"Fuel required: {fuelreq} distance: {distance}")
    fuelcost.append(fuelreq)
fuelcost_tot = sum(fuelcost)

print(f"The cheapest alternative for the crabs is position {pos}, and cost {fuelcost_tot} fuel")
