from random import randint

def simulate(simulations, swap, doors):
    wins = 0
    for i in range(simulations):
        door = randint(1, doors)
        choice = randint(1, doors)
        if swap:
            if door != choice:
                wins += 1
        else:
            if door == choice:
                wins += 1
    return (wins/iterations) * 100


doors = int(input("Number of doors: "))
simulations = int(input("Number of simutations: "))
print("Wins when swapping: " + str(simulate(simulations, True)) + " %")
print("Wins when not swapping: " + str(simulate(simulations, False)) + " %")

