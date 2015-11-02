A genetic algorithm that learns how to find 4 numbers that add up to 200.  The
four numbers in this algorithm are taken from 32 bits formatted as a long.  7 times
out of 10 this algorithm will find a solution, however just to be safe I am going
to say that 1000 generations is needed for me to be confident in my algorithm.
I choose a population size of 50 just to increase the chance of finding a solution.
With a bigger sample size there is more to choose from which from my understanding
increase the chance of finding a solution.  I chose to mutate every time just to
give the population more diversity, and I just think it is cool to mutate.

To run under the GA directory type the following:
  ```$ python genetic_alg.py ```
