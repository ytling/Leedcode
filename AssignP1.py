# -*- coding: utf-8 -*-
"""
Assignment 1 problem 1. Determine the effiency of given schools.

Created on Mon Jan 22 2018

@author: LeoZ
"""
from __future__ import division
from pyomo.environ import *
# Parameters declaring
sin = {'s1': [13, 4, 0.05], 's2': [14, 5, 0.05], 's3': [11, 6, 0.06], 's4':
       [15, 8, 0.08]}
sout = {'s1': [9, 7, 6], 's2': [10, 8, 7], 's3': [11, 7, 8], 's4':
        [9, 9, 9]}
inPrice = list(sin.values())
outValues = list(sout.values())
# Declaring model.
m = ConcreteModel()
m.inind = range(3)
m.outind = range(3)

# Variables
m.x = Var(m.inind, within=PositiveReals)
m.y = Var(m.outind, within=PositiveReals)
# Setting up constrains
# Constant constrains
m.limits = ConstraintList()
for k in range(4):
    m.limits.add(sum(m.y[i]*inPrice[k][i] for i in m.inind) -
                 sum(m.x[j]*outValues[k][j] for j in m.outind) >= 0)

# Objective constrain
m.rescale = Constraint(expr=sum(m.y[i]*inPrice[3][i] for i in m.inind) == 1)

# Objective function
m.obj = Objective(expr=sum(outValues[3][i]*m.x[i] for i in m.outind),
                  sense=maximize)
'''
Optimization results:
    School 1's efficiency: 1.0000000
    School 2's efficiency: 1.0
    School 3's efficiency: 0.9999999
    School 4's efficiency: 0.9490909
Therefore, School 4 is inefficient and the rest schools are efficient.
Unsolved problem:
    I have to run the program manually each time I change the school.
    Is there any methods that could avoid it except creating AbstractModel()?
'''
