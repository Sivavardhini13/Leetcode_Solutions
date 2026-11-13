# Leetcode 2878 : Get the Size of a DataFrame
# Difficulty : Easy

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)