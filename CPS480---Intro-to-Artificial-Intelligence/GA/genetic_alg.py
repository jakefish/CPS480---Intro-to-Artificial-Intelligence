import random

x = 0xffffffff

def create_population(size):
    population = []

    for index in range(size):
        population.append(random.randint(0, 0xffffffff))

    return population

def evalutate(x):
    pass

def selection(x):
    pass

def crossover(x):
    pass

def mutate(x):
    pass
