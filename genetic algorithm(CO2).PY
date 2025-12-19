import random

population_size = 6
generations = 10

population = [random.randint(0, 31) for _ in range(population_size)]

def fitness(x):
    return x * x

for g in range(generations):
    population = sorted(population, key=fitness, reverse=True)
    parents = population[:2]

    children = []
    for _ in range(population_size - 2):
        child = random.choice(parents)
        if random.random() < 0.1:   # mutation
            child = random.randint(0, 31)
        children.append(child)

    population = parents + children

print("Best Solution:", population[0])
