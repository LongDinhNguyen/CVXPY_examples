from cvxpy import *
import cvxpy as cp
import numpy as np

x = Variable()
y = Variable()

obj = Maximize(5*x+3*y)
constraints = [1*x + 5*y <= 3, 0 <= x, x <= 2, 0 <= y, y <= 30]

prob = Problem(obj, constraints)

prob.solve(solver=ECOS, verbose=True)

print "Status: ", prob.status
print "Objective value: ", prob.value
print "x = ", x.value
print "y = ", y.value
