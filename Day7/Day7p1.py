#Day 7 part 1
import statistics
import math

data = open("DataDay7.txt", "r").read().split(",")
crabs = [int(crab) for crab in data]

#Get position
pos = statistics.median(crabs)

#Calculate fuelcost
fuelcost = []
for d in crabs:
    fuel = math.fabs(d-pos)
    fuelcost.append(fuel)
fuelcost_tot = sum(fuelcost)

print(f"The cheapest alternative for the crabs is position {pos}, and cost {fuelcost_tot} fuel")
