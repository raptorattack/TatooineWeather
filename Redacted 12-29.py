#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 12:29:46 2016

@author: emilygomez
"""

###             Tatooine Weather Rev. 1             ###
###                                                 ###
###     Created by: Adam and Emily Brockmeier       ###
###                                                 ###
###     Date: Dec. 17th, 2016                       ###
###     Updated on: Dec. 29th, 2016                 ###
###                                                 ###
###     Program that pulls weather information      ###
###     from wunderground.com and edits it          ###
###     to seem like harsh weather conditions       ###
###     on Star Wars planet Tatooine.               ###

import time
from twython import Twython
import json
import urllib
from time import strftime



DATE = time.strftime("%m/%d/%Y, %-I:%M%p")

#WEATHER STUFF
url = 'http://api.wunderground.com/api/YourWundergroundKeyHere/conditions/q/AU/Alice_Springs.json'
#TWITTER STUFF
CONSUMER_KEY = '***' #add your twitter information from the twitter API setup
CONSUMER_SECRET = '***'
ACCESS_KEY = '***'
ACCESS_SECRET = '***'
twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

while True:
#PULL THE ORIGINAL VALUES
    json_string = urllib.request.urlopen(url).read().decode('UTF-8')
    parsed_json = json.loads(json_string)
    temp_f = parsed_json['current_observation']['temp_f']
    wind_mph = parsed_json['current_observation']['wind_mph']
    relative_humidity = parsed_json['current_observation']['relative_humidity']

#CHANGE THE VALUES TO TATOOINE VALUES
    temp_tat = temp_f*1.8
    wind_tat = wind_mph*13.84
    hum_tat = float(relative_humidity.strip('%'))/100.0

    
#PRINT TIME STAMP
    print("%s" % DATE)

#UPLOAD TO TWITTER
    twitter.update_status(status="Current Temp: %.6s F\nWindspeed: %s mph\nHumidity: %s%c"%(temp_tat,wind_tat,hum_tat,37))
    time.sleep(7200)