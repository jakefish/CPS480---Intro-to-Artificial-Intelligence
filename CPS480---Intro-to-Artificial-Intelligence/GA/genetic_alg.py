import random


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



def evalutate_fitness(population):

    for individual in population:
        curr_value = decode(individual)
        difference = abs(curr_value - 200)





def selection(x):
    pass

def crossover(x):
    pass

def mutate(x):
    pass

population = initial_population(50)
evalutate_fitness(population)
