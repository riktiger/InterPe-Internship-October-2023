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
#venue_dataset = pd.read_csv('/home/aritrabag/Documents/internship_projects/venues.csv')

#team_list = teams_dataset['batting_team'].unique()
#print(team_list)
teams = ['Royal Challengers Bangalore', 'Delhi Capitals','Mumbai Indians', 'Kings XI Punjab', 'Kolkata Knight Riders', 'Sunrisers Hyderabad', 'Rajasthan Royals', 'Chennai Super Kings']

#venue_list = venue_dataset['venue'].unique()
#print(venue_list)
venues = ['Rajiv Gandhi International Stadium, Uppal , Hyderabad',  'M Chinnaswamy Stadium , Bangalore', 'Wankhede Stadium , Mumbai', 'Holkar Cricket Stadium , Indore', 'Eden Gardens , Kolkata',  'Feroz Shah Kotla , Delhi',  'Punjab Cricket Association IS Bindra Stadium, Mohali , Chandigarh', 'Punjab Cricket Association Stadium, Mohali , Chandigarh',  'Sawai Mansingh Stadium , Jaipur', 'MA Chidambaram Stadium, Chepauk , Chennai', 'Dr DY Patil Sports Academy , Mumbai', 'Newlands , Cape Town',  "St George's Park , Port Elizabeth" ,'Kingsmead , Durban' , 'SuperSport Park , Centurion', 'Buffalo Park , East London',  'New Wanderers Stadium , Johannesburg', 'De Beers Diamond Oval , Kimberley','OUTsurance Oval , Bloemfontein', 'Brabourne Stadium , Mumbai', 'Sardar Patel Stadium, Motera , Ahmedabad' , 'Barabati Stadium , Cuttack',  'Vidarbha Cricket Association Stadium, Jamtha , Nagpur' , 'Himachal Pradesh Cricket Association Stadium , Dharamsala',  'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium , Visakhapatnam',  'Subrata Roy Sahara Stadium , Pune',  'Shaheed Veer Narayan Singh International Stadium , Raipur', 'JSCA International Stadium Complex , Ranchi',  'Sheikh Zayed Stadium , Abu Dhabi' ,'Sharjah Cricket Stadium , Sharjah', 'Maharashtra Cricket Association Stadium , Pune',  'Punjab Cricket Association IS Bindra Stadium, Mohali , Mohali', 'M Chinnaswamy Stadium , Bengaluru', 'M. A. Chidambaram Stadium , Chennai', 'Feroz Shah Kotla Ground , Delhi' , 'M. Chinnaswamy Stadium , Bengaluru',  'Rajiv Gandhi Intl. Cricket Stadium , Hyderabad',  'IS Bindra Stadium , Mohali' ,'ACA-VDCA Stadium , Visakhapatnam']

predictor = pickle.load(open('/home/aritrabag/Documents/internship_projects/predictor.pkl','rb'))
st.title('IPL Dream Team')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Batting Team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Bowling Team',sorted(teams))

venue = st.selectbox('Venue',sorted(venues))

target = st.number_input('1st Innings Target Target')

col3,col4,col5 = st.columns(3)

with col3:
    runs = st.number_input(' Current Score')
with col4:
    overs = st.number_input('Overs completed')
with col5:
    wickets = st.number_input('Wickets Lost')

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
    win = result[0][1]
    st.header(batting_team + "- " + str(round(win*100)) + "%")
    st.header(bowling_team + "- " + str(round(loss*100)) + "%")