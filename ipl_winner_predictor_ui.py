#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 00:23:22 2023

@author: aritrabag
"""

#import numpy as np
import pandas as pd
import pickle
import streamlit as st

#teams_dataset = pd.read_csv('/home/aritrabag/Documents/internship_projects/teams.csv')
venue_dataset = pd.read_csv('/home/aritrabag/Documents/internship_projects/venues.csv')

#team_list = teams_dataset['batting_team'].unique()
#print(team_list)
teams = ['Royal Challengers Bangalore', 'Delhi Capitals','Mumbai Indians', 'Kings XI Punjab', 'Kolkata Knight Riders', 'Sunrisers Hyderabad', 'Rajasthan Royals', 'Chennai Super Kings']

#venue_list = venue_dataset['venue'].unique()
#print(venue_list)
venues = ['Rajiv Gandhi International Stadium, Uppal , Hyderabad' ,
 'M. Chinnaswamy Stadium , Bengaluru', 'Wankhede Stadium , Mumbai',
 'Holkar Cricket Stadium , Indore', 'Eden Gardens , Kolkata',
 'Feroz Shah Kotla , Delhi',
 'Punjab Cricket Association IS Bindra Stadium, Mohali , Chandigarh',
 'Sawai Mansingh Stadium , Jaipur',
 'MA Chidambaram Stadium, Chepauk , Chennai',
 'Dr DY Patil Sports Academy , Mumbai', 'Newlands , Cape Town',
 "St George's Park , Port Elizabeth", 'Kingsmead , Durban',
 'SuperSport Park , Centurion', 'Buffalo Park , East London',
 'New Wanderers Stadium , Johannesburg',
 'De Beers Diamond Oval , Kimberley', 'OUTsurance Oval , Bloemfontein',
 'Brabourne Stadium , Mumbai', 'Sardar Patel Stadium, Motera , Ahmedabad',
 'Barabati Stadium , Cuttack',
 'Vidarbha Cricket Association Stadium, Jamtha , Nagpur',
 'Himachal Pradesh Cricket Association Stadium , Dharamsala',
 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium , Visakhapatnam',
 'Subrata Roy Sahara Stadium , Pune',
 'Shaheed Veer Narayan Singh International Stadium , Raipur',
 'JSCA International Stadium Complex , Ranchi',
 'Sheikh Zayed Stadium , Abu Dhabi' 'Sharjah Cricket Stadium , Sharjah',
 'Maharashtra Cricket Association Stadium , Pune']

predictor = pickle.load(open('/home/aritrabag/Documents/internship_projects/predictor.pkl','rb'))
st.title('IPL Dream Team')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Batting Team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Bowling Team',sorted(teams))

venue = st.selectbox('Venue',sorted(venues))

target = st.number_input('Target',step = 1)

col3,col4,col5 = st.columns(3)

with col3:
    runs = st.number_input(label =' Current Score', step = 1)
with col4:
    overs = st.number_input(label = 'Overs completed', min_value = 0.0, max_value = 20.0, step = 0.1)
with col5:
    wickets = st.number_input(label = 'Wickets Lost', min_value = 0, max_value = 10, step = 1)

if st.button('Who Will Win the Match ?'):
    runs_left = target - runs
    balls_bowled = int(overs)*6 + (overs-int(overs))*10
    balls_left = 120 - balls_bowled
    wickets_left = 10 - wickets
    crr = runs/balls_bowled
    rrr = (runs_left*6)/balls_left

    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'venue':[venue],'target':[target],'runs_left':[runs_left],'balls_left':[balls_left],'rrr':[rrr],'crr':[crr],'wickets left':[wickets_left]})

    result = predictor.predict_proba(input_df)
    loss = result[0][0]
    draw = result[0][1]
    win = result[0][2]
    st.header(batting_team + "- " + str(round(win*100,2)) + "%")
    st.header(bowling_team + "- " + str(round(loss*100,2)) + "%")
    st.header("Chance of a Super-Over to Settle a Draw " + "- " + str(round(draw*100,2)) + "%")