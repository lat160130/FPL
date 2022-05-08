# Fantasy Premier League 

# == Import Block =================================================================================
import json
import sys
import pandas as pd
import numpy  as np
# =================================================================================================

# == Import FPL Data ========================
fileFPL = 'fplJSON.json'
fplJson = json.load(open(fileFPL, 'r', encoding="utf8"))
fplKeys = list(fplJson.keys())
dfFPLElem   = pd.DataFrame(fplJson['elements'])
dfFPLSlim   = dfFPLElem[['second_name','team','element_type','selected_by_percent','now_cost','minutes','transfers_in','value_season','total_points']]
np.set_printoptions(threshold=sys.maxsize)
# print(dfFPLElem)
print(dfFPLSlim)
# ===========================================


