import random


TARGET = 200


def initial_population(size):
    """
    Creates an initial randomly generated population based on the given
    size.
    """

    population = []

    for index in range(size):
        population.append(random.randint(0, 0xffffffff))

    return population

def decode(chromosome):
    """
    Takes each individual from the population and decodes their value.
    """

    first_value = chromosome & 0xff
    second_value = (chromosome & 0xFF00) >> 8
    third_value = (chromosome & 0xFF0000) >> 16
    fourth_value = (chromosome & 0xFF000000) >> 24

    decoded_value = first_value + second_value + third_value + fourth_value

    return decoded_value

def evalutate_fitness(individual):
    """
    Returns the fitness rating of an individual from a population.
    """
    difference = abs(TARGET - decode(individual))
    fitness = 1000 - difference
    return fitness

def crossover(mother, father):
    first_half = mother & 0xFF00
    second_half = father & 0xFF000000
    child = (first_half | second_half)
    return child

def mutate(chromosome):
    altered_bit_position = random.randrange(0, 31)
    mutation = x ^ (1 << altered_bit_position)
    return mutation

def selection(x):
    pass



population = initial_population(50)
x = crossover(population[0], population[1])
print x
y = mutate(x)
print bin(y)
for individual in population:

    fitness = evalutate_fitness(individual)

    #print fitness
