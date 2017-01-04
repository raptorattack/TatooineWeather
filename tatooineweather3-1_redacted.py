###             Tatooine Weather Rev. 3             ###
###                                                 ###
###     Created by: Adam and Emily Brockmeier       ###
###                                                 ###
###     Date: Jan. 4th, 2016                        ###
###                                                 ###
###     Program that pulls weather information      ###
###     from wunderground.com and edits it          ###
###     to seem like harsh weather conditions       ###
###     on Star Wars planet Tatooine.               ###


# Rev. 3 CHANGELOG:
#
# *Fixed for compatibility with Python 3! :D
# *Moved the timestamp into the loop
# *Edited format of the tweet to show degrees
# *Limited decimal precision of tweet variables to fix long numbers

import time
from twython import Twython
import json
import urllib
from time import strftime


#WEATHER STUFF
url = 'http://api.wunderground.com/api/[yourkeyhere]/conditions/q/AU/Alice_Springs.json'

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

#PRINT THE VALUES
    #print("Current Temp: %s F\n" % (temp_tat))
    #print("Windspeed: %s mph\n" % (wind_tat))
    #print("Humidity: %s %c" % (hum_tat,37))

#UPLOAD TO TWITTER
    twitter.update_status(status="Current Temp: %.6s%cF\nWindspeed: %.5s mph\nHumidity: %.4s%c"%(temp_tat,176,wind_tat,hum_tat,37))
    
#PRINT TIME STAMP
    DATE = time.strftime("%m/%d/%Y, %-I:%M%p")
    print("%s" % DATE)
    
    time.sleep(3600)
