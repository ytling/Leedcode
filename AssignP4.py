# -*- coding: utf-8 -*-
"""
Assignment 1 problem 4. Determine the relative efficiency of four
degree-granting units Business; Education; Arts and Sciences; and Health,
Physical Education, and Recreation (HPER).

NOTE:
    I. Due to the given information is unclear, I decide to discard the data
       of faculty. This problem does not provide any explanation to the number
       that its provide for faculty.
    II. I decide to view the number of staff supported and supply budget as
        price, while consider credit hours and research publications(RP) as
        produced value.

Created on Mon Jan 22 16:53:39 2018

@author: LeoZ
"""
from __future__ import division
from pyomo.environ import *
# Parameters declaring
din = {'Business': [70, 5], 'Education': [20, 3], 'Arts and Sciences': 
       [140, 20], 'HPER': [15, 1]}
dout = {'Business': [15, 225], 'Education': [5.4, 70], 'Arts and Sciences': 
       [56, 1300], 'HPER': [2.1, 40]}
inPrice = list(din.values())
outValues = list(dout.values())
# Declaring model.
m = ConcreteModel()
m.inind = range(2)
m.outind = range(2)
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
    Department of Business's efficiency = 1.0000000
    Department of Education's efficiency = 0.675
    Department of Arts and Sciences's efficiency = 1.0000000
    Department of HPER's efficiency = 0.7246376811594201
Therefore, Business and Arts and Sciences deparment are efficient but the rest
are inefficient.
'''
