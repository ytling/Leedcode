# -*- coding: utf-8 -*-
"""
Assignment 1 problem 3. Determine the effiency of given precinct.

Created on Mon Jan 22 2018

@author: LeoZ
"""
from __future__ import division
from pyomo.environ import *
# Parameters declaring
pin = {'p1': [200, 60], 'p2': [300, 90], 'p3': [400, 120]}
pout = {'p1': [6, 8], 'p2': [8, 9.5], 'p3': [10, 11]}
inPrice = list(pin.values())
outValues = list(pout.values())
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
for k in range(3):
    m.limits.add(sum(m.y[i]*inPrice[k][i] for i in m.inind) -
                 sum(m.x[j]*outValues[k][j] for j in m.outind) >= 0)

# Objective constrain
m.rescale = Constraint(expr=sum(m.y[i]*inPrice[2][i] for i in m.inind) == 1)

# Objective function
m.obj = Objective(expr=sum(outValues[2][i]*m.x[i] for i in m.outind),
                  sense=maximize)

'''
Optimization results:
    Precinct 1's efficiency = 1.0
    Precinct 2's efficiency = 0.8888888
    Precinct 3's efficiency = 0.8333333
Therefore, only precinct 1 is efficient and the rest are inefficient.
'''