# Loop over results of each game and predict winner
# # Dispay winner on website2"

# Pandas

import pandas as pd
from today_preview import split_record, preview_ext

# teams=['ATL','ARI','BAL','BOS','CHN','CHA','CIN','CLE','COL','DET','HOU','KCA','ANA','LAN','MIA','MIL','MIN','NYN','NYA','OAK','PHI','PIT','SDN','SFN','SEA','SLN','TBA','TEX','TOR','WAS']
# team = ATL
data = pd.read_csv(f"results.csv")
# data = pd.read_csv(f"results{team}.csv")
# raw = ['Detroit Tigers', 'Washington Nationals', 83, 0.58, 0.5, 114.1, 0.0, 5.95, 39.1, 0.5, 0.7, 0.48, 0.52, 0.35, 0.2, 0.3, 0.32, 0.7290000000000001, 0.662, 2, 0.5]\n",
# data = pd.Dataframe(data=raw),
data.head()

# Drop the null columns where all values are null
X = data.drop(["home_name","away_name"], axis=1)
X
   
# Scale the data using MinMaxScaler\n",
from sklearn.preprocessing import MinMaxScaler
X_scaler = MinMaxScaler().fit(X)
X_scaled = X_scaler.transform(X)

# Use Pickle
import pickle

# Load from file\n",
with open('finalized_model.sav', 'rb') as file: 
    pickle_model = pickle.load(file)

# Predict target values
Ypredict = pickle_model.predict(X_scaled)
print(Ypredict)

HomeTeam = str(data["home_name"])
AwayTeam = str(data["away_name"])
if Ypredict == '1':
    print (HomeTeam)
else:
    print (AwayTeam)

