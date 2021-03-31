# -*- coding: utf-8 -*-
"""
Assignment 1 problem 2. Determine the effiency of given schools.

Created on Mon Jan 22 2018

@author: LeoZ
"""
from __future__ import division
from pyomo.environ import *
# Parameters declaring
bin = {'b1': [15, 20, 50], 'b2': [14, 23, 51], 'b3': [16, 19, 51]}
bout = {'b1': [200, 15, 35], 'b2': [220, 18, 45], 'b3': [210, 17, 20]}
inPrice = list(bin.values())
outValues = list(bout.values())
m = ConcreteModel()
m.inind = range(3)
m.outind = range(3)
# Variables
m.x = Var(m.inind, within=PositiveReals)
m.y = Var(m.outind, within=PositiveReals)
# Setting up constrains
# Constant constrains
m.limits = ConstraintList()
for k in range(3):
    m.limits.add(sum(m.y[i]*inPrice[k][i] for i in m.inind) -
                 sum(m.x[j]*outValues[k][j] for j in m.outind) >= 0)

# Objective constrain
m.rescale = Constraint(expr=sum(m.y[i]*inPrice[0][i] for i in m.inind) == 1)

# Objective function
m.obj = Objective(expr=sum(outValues[0][i]*m.x[i] for i in m.outind),
                  sense=maximize)

'''
Optimization results:
    Branch 1's efficiency: 1.0000000
    Branch 2's efficiency: 0.9999999
    Branch 3's efficiency: 0.9999999
Therefore, DEA could not determine which branch is inefficient.
'''