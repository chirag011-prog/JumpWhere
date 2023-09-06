def gas_S(gas, cost, start):
    n= len(gas)
    remaining = 0
    i = start
    started= False
    while i != start or not started:
        started = True
        remaining += gas[i] - cost[i]
        if remaining < 0:
            return False
        i = (i+1)%n
    return True
gas = [1,5,3,3,5,3,1,3,4,5]
cost = [5,2,2,8,2,4,2,5,1,2]
start = 0
print(gas_S(gas, cost, start))