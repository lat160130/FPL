# This file will pick the "optimal" 14 players for fantasy premier league.
# This function will read in a table of all the premier league players, another function written in this folder
# will assign a point value associated to each player.  Then, in accordance with the player's value, pick
# the optimal 14.



# == Import Block =================================================================================
import pandas as pd
import numpy  as np
# =================================================================================================



filePL  = 'fpl_21_22_playerlist.xlsx' # test file of players from the fpl 21-22 season.
dfPL = pd.read_excel(filePL)  # import data from excel




