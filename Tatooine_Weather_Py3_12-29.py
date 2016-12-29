# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time
from twython import Twython
import json
import urllib
from time import strftime



DATE = time.strftime("%m/%d/%Y, %-I:%M%p")

#WEATHER STUFF
url = 'http://api.wunderground.com/api/480a8ee15db8f9cb/conditions/q/AU/Alice_Springs.json'
#TWITTER STUFF
CONSUMER_KEY = 'GRb3yhIvVr3dN4vmqNfWzrALC' #add your twitter information from the twitter API setup
CONSUMER_SECRET = 'jYpqUfP9OywaVMfrBxRwEkuHSynrm5wqkRKBnUraBaTu2u6kae'
ACCESS_KEY = '810155976305287169-RbqInyDOqfiXuDfIbZroPUTpvoKmNBg'
ACCESS_SECRET = 'TzeXSbgTMz3nj49OxxSNKB7cTf945aJVN65MaNNQnE5Bn'
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

#PRINT THE VALUES
    #print("Current Temp: %s F\n" % (temp_tat))
    #print("Windspeed: %s mph\n" % (wind_tat))
    #print("Humidity: %s %c" % (hum_tat,37))
    
#PRINT TIME STAMP
    print("%s" % DATE)

#UPLOAD TO TWITTER
    twitter.update_status(status="Current Temp: %.6s F\nWindspeed: %s mph\nHumidity: %s%c"%(temp_tat,wind_tat,hum_tat,37))
    time.sleep(600)
    
  