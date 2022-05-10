
import json
import sys
import pandas as pd
import numpy  as np



filePLRes  = 'soccerPythagPrem.xlsx'
xlsPremRes = pd.ExcelFile(filePLRes)
plYears = xlsPremRes.sheet_names # list containing all the sheet names
# Yearly competition goes in reverse order Most recent entry first
