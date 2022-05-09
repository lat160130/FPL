# Fantasy Premier League 

# == Import Block =================================================================================
import json
import sys
import pandas as pd
import numpy  as np
# =================================================================================================


# == Important Constants ==
num_gwks     = 38 
init_money   = 100
avg_mnth_pts = 364 # Best performing players are hitting 364 points per month, this is approximately 4 game weeks per month
avg_gw_pts   = avg_mnth_pts / 4 # this comes to 91 points per game week
# =========================

# == Import FPL Data ==============================================================================
fileFPL = 'fplJSON.json'
filePlayerList = 'fpl21-22-playerlist.csv'
fileFPLX = 'fpl_21_22_playerlist.xlsx'
fplJson = json.load(open(fileFPL, 'r', encoding="utf8"))
fplKeys = list(fplJson.keys())
dfFPLElem   = pd.DataFrame(fplJson['elements'])
dfFPLSlim   = dfFPLElem[['second_name','team','element_type','selected_by_percent','now_cost','minutes','transfers_in','value_season','total_points']]
# np.set_printoptions(threshold=sys.maxsize)
# print(dfFPLElem)
# print(dfFPLSlim)


dfFPL2022 = pd.read_excel(fileFPLX)


dfFPL2022['Points'] = dfFPL2022['Points'].astype(float)

dfFPL2022['Price']        = dfFPL2022['Price'].str.replace('£', '')
dfFPL2022['Price']        = dfFPL2022['Price'].astype(float)


dfFPL2022['Total Pts/Price'] = dfFPL2022['Points'] / dfFPL2022['Price']
dfFPL2022['Total pts / gameweek'] = dfFPL2022['Points'] / num_gwks
dfFPL2022['Total pts/ Price / gwks'] = dfFPL2022['Total Pts/Price'] / num_gwks


print(dfFPL2022.sort_values(by=['Total Pts/Price'], ascending=False).head(30))
print(dfFPL2022.sort_values(by=['Total pts / gameweek'] , ascending=False).head(30))
# =================================================================================================


