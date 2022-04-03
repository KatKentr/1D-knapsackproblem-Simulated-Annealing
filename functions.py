#Author: Aikaterini Kentroti

import numpy as np
import random
import math
import matplotlib.pyplot as plt


# Objective function
def Objfun(solution, profit, weight, prints=False):
    """Calculates the objective function value and total weight of a solution. Returns the objective function value for a solution"""
    objfun_value = 0
    totalWeight = 0
    for i in range(len(solution)):
        objfun_value += profit[i] * solution[i]
        totalWeight += weight[i] * solution[i]
    if prints == True:
        print("The objective function value for the solution {}".format(solution), " is {}".format(objfun_value))
    return objfun_value

def totWeight(solution,weight):
    """Calculates the total weight of a solution"""
    totalWeight = 0
    for i in range(len(solution)):
        totalWeight += weight[i] * solution[i]
    return totalWeight

def initial_Solution(profit, weight, capacity):
    """returns an initial solution for the 1-D knapsack problem"""
    #construction of an initial solution: the first three items with the highest profit/weight ratio
    #Prerequisite: profit and weight arrays are sorted in descending order according to the ratio p/w

    ini_solution = np.zeros(len(profit), dtype=int)
    currentTotalWeight = 0
    finalTotalWeight = 0

    for i in range (5):
        finalTotalWeight=currentTotalWeight
        if weight[i] > capacity:
            ini_solution[i] = 0
        else:
            currentTotalWeight += weight[i]
            if (currentTotalWeight <=capacity):
                ini_solution[i] = 1

    z = Objfun(ini_solution, profit, weight)

    print("initial_solution: {}".format(ini_solution), "Total weight: {}".format(finalTotalWeight), "Total profit: {}".format(z))
    return ini_solution


def initialSolution_MartelloToth(profit, weight, capacity):
    # construction of an initial solution. Implementation based on Martello and Toth book: Knapsack problems, Algorithms and Computer Implementations (1990)

    """Calculates and returns an initial solution for the 1-D knapsack problem, implementation of a greedy algorithm"""
    #Prerequisite: profit and weight arrays are sorted in descending order according to the ratio p/w

    item = 0
    best_pr = profit[0]
    ini_solution = np.zeros(len(profit), dtype=int)
    currentTotalWeight = 0
    finalTotalWeight = 0
    i = 0
    while currentTotalWeight <= capacity:
        finalTotalWeight=currentTotalWeight
        if weight[i] > capacity:
            ini_solution[i] = 0
        else:
             currentTotalWeight += weight[i]
             if (currentTotalWeight <=capacity):
                  ini_solution[i] = 1

             if profit[i] > best_pr:
                item = i
                best_pr = profit[i]

        i += 1

    z = Objfun(ini_solution, profit, weight)

    if best_pr > z:
        z = best_pr
        for i in range(len(ini_solution)):
            ini_solution[i] = 0
        ini_solution[item] = 1

    print("initial_solution: {}".format(ini_solution), "Total weight: {}".format(finalTotalWeight), "Total profit: {}".format(z))
    return ini_solution


# generate new solutions
def flip(solution):
    """  takes a solution as input parameter, inverts the value in one random position and returns the new solution"""

    index1 = random.randint(0, len(solution) - 1)

    if solution[index1] == 0:
        solution[index1] = 1
    else:
        solution[index1] = 0

    new_solution = solution

    return new_solution


def simulated_annealing(iterations, ini_temp, profit, weight, capacity):
    temperature = ini_temp  # initialize temperature
    ini_sol = initial_Solution(profit, weight, capacity)  # calculate initial solution
    best_solution = ini_sol.copy()  # initialization of best solution
    curr_solution = ini_sol.copy()  # initialization of current solution
    best_profit = Objfun(ini_sol, profit, weight, prints=False)
    totalWeight=totWeight(ini_sol,weight)         #total weight of the initial solution
    bests = []
    iteration=[]
    iter=0;          #the iteration at which the best solution was found

    bests.append(best_profit)               #store the initial best solution and best profit
    iteration.append(iter);

    coeffa = 0.93  # coefficient, cooling scheme


    k = 0  # counter for inner iterations
    for i in range(iterations):

        for j in range(5):

            # print("best solution is: {}".format(best_solution))

            # print(k, "current solution: {}".format(curr_solution))
            zo = Objfun(curr_solution, profit, weight, prints=False)
            # print(k, "zo of current solution: {}".format(zo))

            while True:
                neighbor_sol = flip(curr_solution.copy())

                z= Objfun(neighbor_sol, profit, weight,
                      prints=False)
                w=totWeight(neighbor_sol,weight)
                if (w <= capacity):
                    break;
            # print(k, "neighbor solution: {}".format(z))

            if z > best_profit:                             #keeps the best solution found
                best_solution = neighbor_sol.copy()
                best_profit = Objfun(best_solution, profit, weight, prints=False);
                totalWeight=totWeight(best_solution,weight)
                iter=k;

                bests.append(best_profit)               #keeps best profits found and the iterations that there were found to plot results
                iteration.append(iter);


            diff = z - zo
            u = random.random()
            calc = np.exp(diff / temperature)


            if diff > 0 or calc > u:
                # print("neighbor solution accepted as current")
                curr_solution = neighbor_sol.copy()

            # print("end of iteration")
            k += 1

        temperature = ini_temp * (coeffa ** k)  #cooling scheme

    plot_result(iteration,bests)  #plots the best profits,graph is stored in Output folder

    return best_solution, best_profit,totalWeight,iter  # return best solution , objective function value, total weight, iteration found

#plotting function
def plot_result(x, y):

    fig, ax1 = plt.subplots()

    ax1.set_xlabel('# Iteration')
    ax1.set_ylabel('Best total profit')
    ax1.plot(x, y, 'o', ls='-', label='Best total profit')


    plt.legend()
    # plt.xticks(range(min(x), max(x)+1))
    fig.savefig('Output/graph.png')
    # plt.show()

