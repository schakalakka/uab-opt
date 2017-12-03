# configuration
# default parameters for the whole algorithm

field_size = 30 # determines the field size nxn and the therefore the number of queens, the problem should be solvable for n>3
number_of_organisms = 100  # number of individuals, i.e. population size

# SELECTION PARAMETERS
parent_selection_method = 'random'  # possible options: 'random', 'fast', 'tournament', 'truncation', 'roulette'
truncation_threshold = 0.5  # truncation of population, only for truncation method
tournament_competitors = 10  # number of competitors in a selection tournament
copy_threshold = 0.1  # parameter for copying a percentage from the old population to the new one

# CROSSOVER PARAMETERS
crossover_method = 'random'  # possible options: 'one_point', 'uniform', 'random'
crossover_probability = 0.8  # usually between 0.6 and 1

# MUTATION PARAMETERS
mutation_method = 'random'  # 'random', 'exchange', 'scramble', 'single', 'displacement', 'insertion', 'inversion', 'displacement_inversion'
mutation_probability = 0.01
