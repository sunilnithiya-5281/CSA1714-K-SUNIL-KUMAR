
import random

N = 8
POPULATION_SIZE = 10

# Generate a random chromosome
def create_chromosome():
    return random.sample(range(N), N)

# Calculate fitness value
def fitness(chromosome):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if abs(chromosome[i] - chromosome[j]) == j - i:
                conflicts += 1

    return 28 - conflicts

# Crossover operation
def crossover(parent1, parent2):
    point = random.randint(1, N - 1)

    child = parent1[:point] + [
        x for x in parent2 if x not in parent1[:point]
    ]

    return child

# Mutation operation
def mutation(chromosome):
    i, j = random.sample(range(N), 2)
    chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome

# Display chessboard
def display(chromosome):
    for row in range(N):
        for col in range(N):
            if chromosome[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

# Genetic Algorithm
population = [
    create_chromosome() for _ in range(POPULATION_SIZE)
]

generation = 0

while True:
    population.sort(key=fitness, reverse=True)

    best = population[0]

    print("\nGeneration:", generation)
    print("Chromosome:", best)
    print("Fitness:", fitness(best))

    if fitness(best) == 28:
        print("\nSolution Found!")
        display(best)
        break

    new_population = [best]

    while len(new_population) < POPULATION_SIZE:
        parent1 = random.choice(population[:5])
        parent2 = random.choice(population[:5])

        child = crossover(parent1, parent2)

        print("Crossover:", child)

        if random.random() < 0.3:
            child = mutation(child)
            print("Mutation:", child)

        new_population.append(child)

    population = new_population
    generation += 1
