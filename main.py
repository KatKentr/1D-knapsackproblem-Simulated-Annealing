#Author: Aikaterini Kentroti

from parser_knapsack import *
from functions import *


#reading data
data,n,capacity,profit,weight = read_inputData("f10_l-d_kp_20_879", ' ',prints=False)

# sorting the profit and weight series according to the ratio p/w in descending order
profit_sorted = profit.sort_values(ascending=False, key=lambda x: x / weight)
weight_sorted = weight.sort_values(ascending=False, key=lambda x: profit / weight)


profit = profit_sorted.to_numpy()  # converting panda series to numpy arrays
weight = weight_sorted.to_numpy()

print(profit)
print(weight)

#Algorithm runs 5 inner iterations. Therefore if we wish to calculate for example 100 iterations in total,insert 20 as the first parameter.
#Second parameter: Initial temperature: 100
best, eval,totalWeight,iter = simulated_annealing(20, 100, profit, weight, capacity)
print("best solution: {}".format(best), "with value: {}".format(eval),"with weight: {}".format(totalWeight),"found at iteration: {}".format(iter))





