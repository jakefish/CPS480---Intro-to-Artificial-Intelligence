import random

x = 0xffffffff

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

    first_value = chromosone & 0xff
    second_value = (chromosone & 0xFF00) >> 8
    third_value = (chromosone & 0xFF0000) >> 16
    fourth_value = (chromosone & 0xFF000000) >> 24
    
    decoded_value = first_value + second_value + third_value + fourth_value

    return decoded_value



def evalutate_fitness(x):
    pass

def selection(x):
    pass

def crossover(x):
    pass

def mutate(x):
    pass

population = initial_population(50)

x = decode(population[0])
print x
