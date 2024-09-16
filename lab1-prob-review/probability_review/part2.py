#!/usr/bin/env python3

"""Module defining code for part2 of probability review lab assignment.

Functions to be implemented: 
evaluate_joint_pdf - evaluate the pmf of a given random variable pair.
expected_value - calculate the expected value of a pair of random vars.
covariance - calculate the covariance matrix for a 2 jointly distributed
    random variables.

Main function (script operation):
main - evaluate and output the pmf, expected value, and covariance 
    matrix for several joint random variables pairs.

"""

import matplotlib.pyplot as plt
import numpy as np

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
import probability_review.discrete_probability_core as dpc
from probability_review.part1 import TwoDiceRoll
from probability_review.part1 import two_dice_sum
from probability_review.part1 import two_dice_sum_plus_one
from probability_review.part1 import weighted_two_dice_sum
from probability_review.part1 import two_dice_difference
from probability_review.part1 import two_dice_true_difference
from probability_review.part1 import doubles_rolled

__author__ = "Joshua Mangelson"
__copyright__ = "Copyright 2020, Joshua Mangelson, Brigham Young University"
__license__ = "MIT License"
__maintainer__ = "Joshua Mangelson"

###########################################################################
# TODO: Complete the following function to evaluate the joint probability
# mass function of two specified random variables under a given experiment
#
# Ex: evaluate_joint_pmf(TwoDiceRoll, two_dice_sum, two_dice_difference)
# should return a dictionary that represents the joint pmf of both the sum
# and difference of a roll of two six-sided dice, as well as two arrays
# enumerating all possible values the random variables can take on.
# These objects can then be passed into the constructor of the
# JointProbabilityMassFunction class to create an object that can do various
# actions such as plot the pmf.
#
# Don't forget to check if the probabilities assigned to the outcomes of
# the experiment passed into the function are valid.
#
# Note: In python, classes and functions can be passed as arguments by
# using the name of the function.
###########################################################################


def evaluate_joint_pmf(experiment_initializer, random_var1, random_var2, dice_sides=6):
    """Evaluate the joint PMF of two random variables for a given experiment.

    Parameters:
    experiment_initializer: Class constructor (derived from DiscreteExperiment)
        that constructs an experiment object for enumerating the possible
        experiment outcomes.
    random_var1: A function object for random variable one that takes an 
        experiment outcome and maps it to a real-number value.
    random_var2: A function object for random variable two that takes an 
        experiment outcome and maps it to a real-number value.


    Returns:
    values_var1: A numpy array of the possible values var1 can take.
    values_var2: A numpy array of the possible values var2 can take.
    probabilities (dic): A dictionary mapping all possible pairs of
          values the two random variables can take on (stored as a two element
          tuple with the value of the 1st random variable 1st) to the associated 
          probability that the specified pair of possible values will occur.

    Exceptions:
    ValueError("Outcomes with negative probabilities recieved."): This function
      raises a ValueError exception with the above message if any of the
      probability values returned by the experiment are negative.
    ValueError("Probabilties do not sum to one."): This function returns a
      value error with the above message if the probabilities for all outcomes
      of the experiment do not sum to one.

    """
    experiment = experiment_initializer(dice_sides)
    values_var1 = []
    values_var2 = []
    probabilities = {}

    ###################################
    # Finish this implementation here
    outcomes = experiment.enumerate_outcomes()
    # print(f"DEBUG outcomes: {outcomes}")

    for outcome in outcomes:
        if outcome[1] < 0.0:
            raise ValueError("evaluate_joint_pmf: Outcomes with negative probabilities received.")

        var1 = random_var1(outcome[0])
        var2 = random_var2(outcome[0])

        if var1 not in values_var1:
            values_var1.append(var1)
        if var2 not in values_var2:
            values_var2.append(var2)

        key = (var1, var2)
        if key not in probabilities.keys():
            probabilities[key] = outcome[1]
        else:
            probabilities[key] += outcome[1]

    if not np.isclose(sum(probabilities.values()), 1.0):
        raise ValueError("evaluate_joint_pmf: Probabilities do not sum to one.")
    ###################################
    return values_var1, values_var2, probabilities


###########################################################################
# TODO: Implement the following function to evaluate the expected value
# of two jointly distributed random variables.
###########################################################################


def expected_value(joint_pmf):
    """Evaluate the expected value for a pair of jointly distributed variables.

    Parameters:
    joint_pmf: The PMF of the specified random variable.

    Returns:
    e_value: The expected value of the given random variable represented 
      using a numpy array composed of the expected value of each individual
      random variable.

    Exceptions:
    ValueError("PMF with negative probabilities recieved."): This function
      raises a ValueError exception with the above message if any of the
      probability values in the passed in pmf are negative.
    ValueError("Probabilties do not sum to one."): This function raises a
      ValueError with the above message if the passed in probabilities do
      not sum to one.
    ValueError("Empty pmf."): This function raises a ValueError with the
      above message if the passed in pmf has zero values.

    """
    if not joint_pmf:
        raise ValueError("expected_value: Empty pmf.")

    pmf = {}

    # if a PMF object was passed in get the internal dictionary
    if(isinstance(joint_pmf, dpc.JointProbabilityMassFunction)):
        pmf = joint_pmf.probabilities
    else:
        pmf = joint_pmf

    e_value = np.zeros(2)

    ##################################
    # Finish Implementation Here
    # multiply each joint probability by its corresponding X and Y values
    
    if not np.isclose(sum(pmf.values()), 1.0):
        raise ValueError("expected_value: Probabilities do not sum to one.")
    
    for key in pmf:
        if pmf[key] < 0.0:
            raise ValueError("expected_value: Outcomes with negative probabilities received.")
        e_value[0] += (key[0] * pmf[key])
        e_value[1] += (key[1] * pmf[key])
    #################################

    return e_value

###########################################################################
# TODO: Implement the following function to evaluate the covariance of two
# jointly distributed random variables.
###########################################################################


def covariance(joint_pmf):
    """Evaluate the covariance of a pair of jointly distributed variables.

    Parameters:
    joint_pmf: The PMF of the specified random variable.

    Returns:
    sigma: The covariance matrix for the given pair of random variables.

    Exceptions:
    ValueError("PMF with negative probabilities recieved."): This function
      raises a ValueError exception with the above message if any of the
      probability values in the passed in pmf are negative.
    ValueError("Probabilties do not sum to one."): This function raises a
      ValueError with the above message if the passed in probabilities do
      not sum to one.
    ValueError("Empty pmf."): This function raises a ValueError with the
      above message if the passed in pmf has zero values.

    """
    pmf = {}

    # if a PMF object was passed in get the internal dictionary
    if(isinstance(joint_pmf, dpc.JointProbabilityMassFunction)):
        pmf = joint_pmf.probabilities
    else:
        pmf = joint_pmf

    sigma = np.zeros([2,2])

    ###################################
    # Finish Implementation Here
    # sigma should be of the form: [[COVxx, COVxy][COVyx, COVyy]]
    # COVxx, COVyy: variances of the individual random variables
    # COVxy, COVyx: covariances, or how "correlated".
        # > 0 : if one goes up, the other goes up
        # 0 : uncorrelated

    if not pmf:
        raise ValueError("covariance: Empty pmf.")

    if not np.isclose(sum(pmf.values()), 1.0):
        raise ValueError("covariance: Probabilities do not sum to one.")

    exp_val = expected_value(pmf)
    exp_x = exp_val[0]
    exp_y = exp_val[1]

    def expected_value_single(temp_pmf):
        e_value = 0.0
        for value in temp_pmf:
            e_value += (value * temp_pmf[value])
        return e_value
    
    # def variance_single(temp_pmf, temp_exp_val):
    #     dev = {} # squared deviations
    #     for key in temp_pmf:
    #         if temp_pmf[key] < 0:
    #             raise ValueError("variance_single: Outcomes with negative probabilities received.")
    #         # deviation^2
    #         temp = pow(key-temp_exp_val,2)
    #         # If squared deviation is not in the key of the dictionary,
    #         # create a new key and assign it the pmf probability
    #         # otherwise, add the pmf probability to that key's value.
    #         if temp not in dev.keys():
    #             dev[temp] = temp_pmf[key]
    #         else:
    #             dev[temp] += temp_pmf[key]
    #     return expected_value_single(dev)

    marginal_x = {}
    marginal_y = {}
    exp_xy = 0.0
    for key in pmf:
        if pmf[key] < 0.0:
            raise ValueError("covariance: Outcomes with negative probabilities received.")
        exp_xy += key[0]*pmf[key]*key[1]

        x_2 = pow(key[0], 2)
        if x_2 not in marginal_x.keys():
            marginal_x[x_2] = pmf[key]
        else:
            marginal_x[x_2] += pmf[key]

        y_2 = pow(key[1], 2)
        if y_2 not in marginal_y.keys():
            marginal_y[y_2] = pmf[key]
        else:
            marginal_y[y_2] += pmf[key]

    # COV[X,Y] = E[XY] - E[X]E[Y]
    cov_xy = exp_xy - (exp_x * exp_y)

    # COV[X,X] = E[X^2] - E[X]^2
    exp_x_2 = expected_value_single(marginal_x)
    print(f"DEBUG exp_x_2: {exp_x_2}")
    cov_xx = exp_x_2 - pow(exp_x, 2)

    # COV[Y,Y] = E[Y^2] - E[Y]^2
    exp_y_2 = expected_value_single(marginal_y)
    print(f"DEBUG exp_y_2: {exp_y_2}")
    cov_yy = exp_y_2 - pow(exp_y, 2)

    sigma = [[cov_xx, cov_xy],[cov_xy, cov_yy]]

    ###################################

    return sigma


def main():
    """Evaluate Joint PMF, expected value, and covariance for various RVs."""

    num_dice_sides = 6
    #Evaluate Joint PMF for the sum and difference of two six-sided dice
    sum_vals, diff_vals, sumdiff_pmf_dic = evaluate_joint_pmf(
        TwoDiceRoll, two_dice_sum, two_dice_difference, dice_sides=num_dice_sides)
    sumdiff_pmf = dpc.JointProbabilityMassFunction(
        sum_vals,
        diff_vals,
        sumdiff_pmf_dic,
        "Sum",
        "Diff ({0}-sided Dice)".format(num_dice_sides))

    fig, ax = sumdiff_pmf.plot_pmf()

    e_value = expected_value(sumdiff_pmf)
    print('Expected value (Joint of sum/diff) with {0}-sided Dice:'.format(num_dice_sides), e_value)
    sigma = covariance(sumdiff_pmf)
    print('Covariance (Joint of sum/diff) with {0}-sided Dice:'.format(num_dice_sides), sigma)

    # #Evaluate Joint PMF for the absolute diff. and diff. of two six-sided dice
    # abs_diff_vals, diff_vals, abs_diff_diff_pmf_dic = evaluate_joint_pmf(
    #     TwoDiceRoll, two_dice_difference, two_dice_true_difference)
    # abs_diff_diff_pmf = dpc.JointProbabilityMassFunction(
    #     abs_diff_vals,
    #     diff_vals,
    #     abs_diff_diff_pmf_dic,
    #     "Absolute Difference",
    #     "True Difference (roll1 - roll0)")

    # fig, ax = abs_diff_diff_pmf.plot_pmf()

    # e_value = expected_value(abs_diff_diff_pmf)
    # print('Expected value (Joint of abs diff/diff):', e_value)
    # sigma = covariance(abs_diff_diff_pmf)
    # print('Covariance (Joint of abs diff/diff):', sigma)
    
    #Evaluate Joint PMF for the sum and (sum+1) of two six-sided dice
    sum_vals, sum_plus_one_vals, sumsum_plus_one_pmf_dic = evaluate_joint_pmf(
        TwoDiceRoll, two_dice_sum, two_dice_sum_plus_one, dice_sides=num_dice_sides)
    sumsum_plus_one_pmf = dpc.JointProbabilityMassFunction(
        sum_vals,
        sum_plus_one_vals,
        sumsum_plus_one_pmf_dic,
        "Sum",
        "Sum Plus One ({0}-sided Dice)".format(num_dice_sides))

    fig, ax = sumsum_plus_one_pmf.plot_pmf()

    e_value = expected_value(sumsum_plus_one_pmf)
    print('Expected value (Joint of sum/sum_plus_one) with {0}-sided Dice:'.format(num_dice_sides), e_value)
    sigma = covariance(sumsum_plus_one_pmf)
    print('Covariance (Joint of sum/sum_plus_one) with {0}-sided Dice:'.format(num_dice_sides), sigma)

    #Evaluate Joint PMF for the sum and (weighted sum of two six-sided dice
    sum_vals, weighted_sum_vals, sumweightedsum_pmf_dic = evaluate_joint_pmf(
        TwoDiceRoll, two_dice_sum, weighted_two_dice_sum, dice_sides=num_dice_sides)
    sumweightedsum_pmf = dpc.JointProbabilityMassFunction(
        sum_vals,
        weighted_sum_vals,
        sumweightedsum_pmf_dic,
        "Sum",
        "Weighted Sum ({0}-sided Dice)".format(num_dice_sides))

    fig, ax = sumweightedsum_pmf.plot_pmf()

    e_value = expected_value(sumweightedsum_pmf)
    print('Expected value (Joint of sum/weightedsum) with {0}-sided Dice:'.format(num_dice_sides), e_value)
    sigma = covariance(sumweightedsum_pmf)
    print('Covariance (Joint of sum/weightedsum) with {0}-sided Dice:'.format(num_dice_sides), sigma)
    

    # #Evaluate Joint PMF for the sum and (sum+some) of two six-sided dice
    # sum_vals, sum_plus_some_vals, sumsum_plus_some_pmf_dic = evaluate_joint_pmf(
    #     TwoDiceRoll, two_dice_sum, two_dice_sum_plus_some)
    # sumsum_plus_some_pmf = dpc.JointProbabilityMassFunction(
    #     sum_vals,
    #     sum_plus_some_vals,
    #     sumsum_plus_some_pmf_dic,
    #     "Sum",
    #     "Sum Plus Some")

    # fig, ax = sumsum_plus_some_pmf.plot_pmf()

    # e_value = expected_value(sumsum_plus_some_pmf)
    # print('Expected value (Joint of sum/sum_plus_some):', e_value)
    # sigma = covariance(sumsum_plus_some_pmf)
    # print('Covariance (Joint of sum/sum_plus_some):', sigma)
    
    
    # #Evaluate Joint PMF for the sum of two six-sided dice and the indicator
    # #random variable for rolling doubles
    # sum_vals, doubles_vals, sumdoubles_pmf_dic = evaluate_joint_pmf(
    #     TwoDiceRoll, two_dice_sum, doubles_rolled)
    # sumdoubles_pmf = dpc.JointProbabilityMassFunction(
    #     sum_vals,
    #     doubles_vals,
    #     sumdoubles_pmf_dic,
    #     "Sum",
    #     "Doubles Rolled")
    
    # fig, ax = sumdoubles_pmf.plot_pmf()

    # e_value = expected_value(sumdoubles_pmf)
    # print('Expected Value (Joint of sum/doubles rolled):', e_value)
    # sigma = covariance(sumdiff_pmf)
    # print('Covariance (Joint of sum/doubles rolled):', sigma)
    
    
    # vals1 = [2, 3, 6]
    # vals2 = [1, 2, 3]
    # prob = {}
    # prob[(2,1)] = 0.2
    # prob[(2,2)] = 0.1
    # prob[(2,3)] = 0.3
    # prob[(3,1)] = 0.2
    # prob[(6,2)] = 0.2

    # pmf = dpc.JointProbabilityMassFunction(vals1, vals2, prob)
    # pmf.plot_pmf()
    plt.show()

    

if __name__ == "__main__":
    main()
