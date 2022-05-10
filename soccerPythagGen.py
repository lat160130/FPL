# Fantasy Premier League 

# Create a governing concept.  Create a regression model of f(goalsAllowed, goalsScored) = Win Percentage

# == Import Block =================================================================================
import json
import sys
import math as m
import pandas as pd
import numpy  as np
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import pandas_profiling as pp
from sklearn import linear_model

# =================================================================================================

# == Constants ===
exp = 1
entries = 49
# ================

# == Import PL Results by year ====================================================================
filePL  = 'allTimePrem.xlsx'
dfPL = pd.read_excel(filePL)

dfPL['R'] = dfPL['GF'] / dfPL['GA']
dfPL['Ratio ^ exp'] = pow(dfPL['R'], exp) 

dfPL['WP'] = dfPL['W'] / dfPL['Pld']
dfPL['NotWin%'] = 1 - dfPL['WP']
dfPL['LP'] = dfPL['L'] / dfPL['Pld']

# goalsScored^2 / (goalsScored^2 + goalsAllowed^2) - Rewards a more offensive team
dfPL['predWPgoalsFor'] = (dfPL['Ratio ^ exp'] * dfPL['Ratio ^ exp']) / (  (dfPL['Ratio ^ exp'] * dfPL['Ratio ^ exp']) + 1   )

# goalsAllowed^2 / (goalsScored^2 + goalsAllowed^2)
dfPL['predWPgoalsAllowed'] = (dfPL['GA'] * dfPL['GA']) / (  (dfPL['GF'] * dfPL['GF']) + (dfPL['GA'] * dfPL['GA'])   )

# factor * WP = predWP
dfPL['factorGF'] = dfPL['predWPgoalsFor'] / dfPL['WP']


dfPL['predError'] = np.sqrt(pow(dfPL['WP'], 2) + pow(dfPL['predWPgoalsFor'], 2) )
print(dfPL)


errPl = dfPL['predError'].sum()
errAvg = errPl / entries

print(errAvg)

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.scatter(dfPL['GF'], dfPL['GA'], dfPL['WP'])
ax.set_xlabel('Goals For')
ax.set_ylabel('Goals Allowed')
ax.set_zlabel('Win Percentage')

X = dfPL[['GF', 'GA']]
y = dfPL['WP']
ols = linear_model.LinearRegression()
model = ols.fit(X,y)

print(model.coef_)
print(model.intercept_)
print(model.score(X,y))

plt.show()
""" profile = pp.ProfileReport(dfPL)
profile.to_file("PL_alltime_correl.html") """
# =================================================================================================




