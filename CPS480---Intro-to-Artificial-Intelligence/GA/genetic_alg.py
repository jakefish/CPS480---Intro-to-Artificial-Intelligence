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
    crossover_rate = 1
    if crossover_rate:
        first_half = mother & 0xFF00
        second_half = father & 0xFF000000
        child = (first_half | second_half)
    return child

def mutate(chromosome):
    altered_bit_position = random.randint(0, 31)
    mutation = chromosome ^ (1 << altered_bit_position)
    return mutation

def weighted_choice(population):
    weight_total = sum((fitness[1] for fitness in population))
    random_pick = random.uniform(0, weight_total)
    for indiviudal, fitness in population:
        if random_pick < fitness:
            return indiviudal
        random_pick = random_pick - fitness
    return indiviudal

def generation(MAX_GENERATIONS):

    population = initial_population(50)
    weighted_population = []
    temp_population = []
    for generation in range(MAX_GENERATIONS):
        print "Generation {0}".format(generation)
        for individual in population:
            fitness_value = evalutate_fitness(individual)
            weighted_population.append((individual, fitness_value))
        mother = weighted_choice(weighted_population)
        father = weighted_choice(weighted_population)
        child = crossover(mother, father)
        mutate(child)
        population.append(child)
        print "Average Fitness: {0}".format(calculate_average_fitness(weighted_population))
        max_fit = evalutate_fitness(population[0])
        max_fit_individual = population[0]
        for individual in population:
            fitness_val = evalutate_fitness(individual)
            if fitness_val > max_fit:
                max_fit = fitness_val
                max_fit_individual = individual
        print "Max Fitness for current generation {0}".format(max_fit)

def calculate_average_fitness(population):
    fitness_length = len(population)
    total_fitness = sum((fitness[1] for fitness in population))
    return total_fitness/fitness_length



generation(500)
