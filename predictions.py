import pandas as pd
from bs4 import BeautifulSoup
import requests
import flask
from flask import jsonify
import csv
import numpy
import datetime


#Function that calculates win % or returns 50% if no record
def split_record(record_string):
    cleaned=record_string.strip(',').split('-')
    if int(cleaned[0])+int(cleaned[1])==0:
        return 0
    else:
        return round(int(cleaned[0])/(int(cleaned[1])+int(cleaned[0])),2)


def preview_ext(url,home_abv,year,month,day,gno):

    #Scrape Pandas Tables
    tables=pd.read_html(url)

    #Names
    home_name=tables[1][1][0].split('2019 ')[1]
    away_name=tables[0][1][0].split('2019 ')[1]


    #Number of Games Played This Season/Test if We Should Record Data
    game_no=int(tables[0][1][3])

    #Scrape Soup
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')


    #Ugly Away Pitcher Data
    away_pitcher=str(soup.find_all('h2')[2]).split()

    #Away Pitcher Handedness
    away_pitcher_hand=away_pitcher[5]
    if away_pitcher_hand=='RHP,':
        away_pitcher_rh=1
    else: 
        away_pitcher_rh=0


    #Away Pitcher Record
    try:
        away_pitcher_record=float(split_record(away_pitcher[6]))
    except: 
        away_pitcher_record=0

    #Away Pitcher ERA
    try:
        away_pitcher_era=float(away_pitcher[7].strip(')</h2>'))
    except:
        away_pitcher_era=0

    #Away Pitcher Innings Pitched, may contain prior year data if before May
    try:
        away_pitcher_ip=float(tables[8]['IP'][0])
    except:
        away_pitcher_ip=0

    #Ugly Home Pitcher Data
    home_pitcher=str(soup.find_all('h2')[5]).split()

    #Home Pitcher Handedness
    home_pitcher_hand=home_pitcher[5]
    if home_pitcher_hand=='RHP,':
        home_pitcher_rh=1
    elif home_pitcher_hand=='LHP,':
        home_pitcher_rh=0
    else:
        home_pitcher_rh=2

    #Home Pitcher Record
    try:
        home_pitcher_record=float(split_record(home_pitcher[6]))
    except:
        home_pitcher_record=0

    #Home Pitcher ERA
    try:
        home_pitcher_era=float(home_pitcher[7].strip(')</h2>'))
    except:
        home_pitcher_era=0

    #Home Pitcher Innings Pitched, may contain prior year data if before May
    try:
        home_pitcher_ip=float(tables[5]['IP'][0])
    except:
        home_pitcher_ip=0


    #Away Team Main Table
    team=tables[0]

    #Away Team Overall Win/Loss Record
    away_record=split_record(team[1][1])


    #Away Team Win/Loss Record in Last 10 Games
    away_last_ten=split_record(team[1][10])

    #Away Team Record as Away Team 
    away_venue_record=split_record(team[1][14])

    #Away Team Record vs Home Team Pitcher Type
    if home_pitcher_rh==1:
        away_pitcher_type_record=split_record(team[1][16])
    else:
        split_record(team[1][17])

    #Home Team Main Table
    team=tables[1]

    #Home Team Overall Win/Loss Record
    home_record=split_record(team[1][1])


    #Home Team Win/Loss Record in Last 10 Games
    home_last_ten=split_record(team[1][10])

    #Home Team Record as Home Team 
    home_venue_record=split_record(team[1][13])

    #Home Team Record vs Away Team Pitcher Type
    if away_pitcher_rh==1:
        home_pitcher_type_record=split_record(team[1][16])
    else:
        home_pitcher_type_record=split_record(team[1][17])

    #Away Team Batting Table, may contain prior year data if before May
    batting=tables[4]

    #Away Team Ops vs Home Pitcher Type
    if home_pitcher_rh==1:
        away_ops_vs_pitcher_type=batting['OPS vRH'][len(batting)-1]
    else:
        away_ops_vs_pitcher_type=batting['OPS vLH'][len(batting)-1]

    #Home Team Batting Table, may contain prior year data if before May
    batting=tables[7]

    #Home Team Ops vs Away Pitcher Type
    if away_pitcher_rh==1:
        home_ops_vs_pitcher_type=batting['OPS vRH'][len(batting)-1]
    else:
        home_ops_vs_pitcher_type=batting['OPS vLH'][len(batting)-1]

    #Home Team Away Team Matchup Record
    head2head=tables[2]

    #Number of Matchups this Season
    try:
        matchup_count=head2head.loc[head2head['Winner'] == 'Away'].index[0]

        #Home Team Win % vs this Away Team
        season_matchups=head2head.head(matchup_count)
        home_matchup_wins=len(season_matchups.loc[head2head['Winner']==home_abv])
        home_matchup_record=home_matchup_wins/matchup_count
    except:
        matchup_count=0
        home_matchup_record=.5

    preview_data= [home_name,away_name,game_no,away_pitcher_record,away_pitcher_era,away_pitcher_ip,
    home_pitcher_record,home_pitcher_era,home_pitcher_ip,
    away_record,away_last_ten,away_venue_record,away_pitcher_type_record,
    home_record,home_last_ten,home_venue_record,home_pitcher_type_record,
    away_ops_vs_pitcher_type,home_ops_vs_pitcher_type,
    matchup_count,home_matchup_record]


    return preview_data 

columns = ["home_name","away_name","game_no","away_pitcher_record","away_pitcher_era","away_pitcher_ip",
"home_pitcher_record","home_pitcher_era","home_pitcher_ip",
"away_record","away_last_ten","away_venue_record","away_pitcher_type_record",
"home_record","home_last_ten","home_venue_record","home_pitcher_type_record",
"away_ops_vs_pitcher_type","home_ops_vs_pitcher_type",
"matchup_count","home_matchup_record"]  


teams=['ATL','ARI','BAL','BOS','CHN','CHA','CIN','CLE','COL','DET','HOU','KCA','ANA','LAN','MIA','MIL','MIN','NYN','NYA','OAK','PHI','PIT','SDN','SFN','SEA','SLN','TBA','TEX','TOR','WAS']

# getting current date and time
date_list = datetime.date.today()
date_list=list(date_list.timetuple())
date_list

df=[]
for t in teams:
    try:
        home_abv=t
        day= '02'
        month='07'
        year='2019'
#         year= f'{date_list[0]}'
#         month= f'{date_list[1]}'
#         day= f'{date_list[2]}'
        gno='0'
        url=f'https://www.baseball-reference.com/previews/{year}/{home_abv}{year}{month}{day}{gno}.shtml'
        df.append(preview_ext(url,home_abv,year,month,day,gno))

     
    except:
        pass


d1 = {'games': df}
df2 = pd.DataFrame(d1)


df2[["home_name","away_name","game_no","away_pitcher_record","away_pitcher_era","away_pitcher_ip","home_pitcher_record","home_pitcher_era","home_pitcher_ip",
"away_record","away_last_ten","away_venue_record","away_pitcher_type_record",
"home_record","home_last_ten","home_venue_record","home_pitcher_type_record",
"away_ops_vs_pitcher_type","home_ops_vs_pitcher_type",
"matchup_count","home_matchup_record"]] = pd.DataFrame(df2.games.values.tolist(), index= df2.index)


df3 = pd.DataFrame(df2['games'].values.tolist(), columns=["home_name","away_name","game_no","away_pitcher_record","away_pitcher_era","away_pitcher_ip",
"home_pitcher_record","home_pitcher_era","home_pitcher_ip",
"away_record","away_last_ten","away_venue_record","away_pitcher_type_record",
"home_record","home_last_ten","home_venue_record","home_pitcher_type_record",
"away_ops_vs_pitcher_type","home_ops_vs_pitcher_type",
"matchup_count","home_matchup_record"])


X = df3.drop(["home_name","away_name"], axis=1)


# Scale the data using MinMaxScaler
from sklearn.preprocessing import MinMaxScaler
X_scaler = MinMaxScaler().fit(X)

X_scaled = X_scaler.transform(X)

import pickle

# Load from file
with open('finalized_model.sav', 'rb') as file:  
    pickle_model = pickle.load(file)

# Predict target values
Ypredict = pickle_model.predict(X_scaled)  


predict_outcome = Ypredict

df3['predicted_outcome']= predict_outcome
df3 = df3.astype({"predicted_outcome": int})

df3["predicted_winner"] = ["Home Team" if ele  == 1 else "Away Team" for ele in df3["predicted_outcome"]]

display_data = df3[["home_name","away_name", "predicted_winner"]].copy()

dict = display_data.to_dict(orient='records')

display_data.to_csv ("static/js/display_data.csv")