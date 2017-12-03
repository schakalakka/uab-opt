import numpy as np
import csv

from genetic_algorithm import config
from genetic_algorithm.main import main

runs = 5
field_sizes = [4]
number_of_organisms = [100]  # [50, 100, 200, 500]

# SELECTION
selection_methods = ['random', 'tournament', 'truncation', 'roulette']  # TODO fast is missing
truncation_thresholds = np.linspace(0.1, 0.9, 9)
tournament_competitors = [3, 5, 10, 15, 20, 25, 30, 40, 50]
copy_thresholds = [0.1]  # [0, 0.1, 0.2, 0.3]

# CROSSOVER
crossover_methods = ['one_point', 'uniform', 'random']  # TODO pmx is still missing
crossover_probabilities = [0.8]  # [0.6, 0.7, 0.8, 0.9, 1]

# MUTATION
mutation_methods = ['random', 'exchange', 'scramble', 'single', 'displacement', 'insertion', 'inversion',
                    'displacement_inversion']
mutation_probabilities = [0.001]  # [0.001, 0.01, 0.1, 0.2, 0.3]
adapt_mutabilities = [True]  # [False, True]

benchmark_list = []
counter = 0
for config.field_size in field_sizes:
    print(f'Field Sizes: {config.field_size}')
    for config.number_of_organisms in number_of_organisms:
        print(f'Population Size: {config.number_of_organisms}')
        for config.parent_selection_method in selection_methods:
            for config.copy_threshold in copy_thresholds:
                for config.crossover_method in crossover_methods:
                    for config.crossover_probability in crossover_probabilities:
                        for config.mutation_method in mutation_methods:
                            for config.mutation_probability in mutation_probabilities:
                                for config.adapt_mutability in adapt_mutabilities:
                                    for _ in range(runs):
                                        counter += 1
                                        print(counter)
                                        current_row = {}
                                        iterations, time, fitness, average_fitness = main()
                                        current_row['field_size'] = config.field_size
                                        current_row['population_size'] = config.number_of_organisms
                                        current_row['selection_method'] = config.parent_selection_method
                                        current_row['copy_threshold'] = config.copy_threshold
                                        current_row['crossover_method'] = config.crossover_method
                                        current_row['crossover_probability'] = config.crossover_probability
                                        current_row['mutation_method'] = config.mutation_method
                                        current_row['mutation_probability'] = config.mutation_probability
                                        current_row['adapt_mutability'] = config.adapt_mutability
                                        current_row['iterations'] = iterations
                                        current_row['time'] = time
                                        current_row['fitness'] = fitness
                                        current_row['average_fitness'] = average_fitness
                                        benchmark_list.append(current_row)
    with open(f'benchmark_{config.field_size}.csv', 'w') as f:
        csv_f = csv.DictWriter(f, delimiter='|', fieldnames=benchmark_list[0].keys())
        csv_f.writeheader()
        csv_f.writerows(benchmark_list)
