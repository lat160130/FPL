# Fantasy Premier League 

# == Import Block =================================================================================
import json
import sys
import pandas as pd
import numpy  as np
# =================================================================================================


# == Import FPL Data ==============================================================================
fileFPL = 'fplJSON.json'
filePlayerList = 'fpl21-22-playerlist.csv'
fplJson = json.load(open(fileFPL, 'r', encoding="utf8"))
fplKeys = list(fplJson.keys())
dfFPLElem   = pd.DataFrame(fplJson['elements'])
dfFPLSlim   = dfFPLElem[['second_name','team','element_type','selected_by_percent','now_cost','minutes','transfers_in','value_season','total_points']]
# np.set_printoptions(threshold=sys.maxsize)
# print(dfFPLElem)
# print(dfFPLSlim)


dfFPL2022 = pd.read_csv(filePlayerList, header=None, delim_whitespace=True, names = ('Name', 'Club', 'Total points', 'Price'))



dfFPL2022['Total points'] = dfFPL2022['Total points'].astype(float)

dfFPL2022['Price']        = dfFPL2022['Price'].str.replace('£', '')
dfFPL2022['Price']        = dfFPL2022['Price'].astype(float)


dfFPL2022['Total Pts/Price'] = dfFPL2022['Total points'] / dfFPL2022['Price']
dfFPL2022 = dfFPL2022.sort_values(by=['Total Pts/Price'], ascending=False)
print(dfFPL2022)
# =================================================================================================


