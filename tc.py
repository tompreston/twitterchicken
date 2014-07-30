"""
PiFace Digital Twitter Chicken Demo
This will pull the latest tweets from USER and say them using espeak and
also wobble the chicken.
"""
from twitter import *
import time
import subprocess
import pifacedigitalio
from keys import (ACCESS_TOKEN,
                  ACCESS_TOKEN_SECRET,
                  API_KEY,
                  API_SECRET)


USER = "_stevechicken"
CHECK_INTERVAL = 5


def chicken_wobble(wobble):
    pfd.relays[0].value = wobble


def say(message):
    subprocess.call(['espeak "{}"'.format(message)], shell=True)


if __name__ == '__main__':
    t = Twitter(auth=OAuth(ACCESS_TOKEN,
                           ACCESS_TOKEN_SECRET,
                           API_KEY,
                           API_SECRET))
    pfd = pifacedigitalio.PiFaceDigital()

    last_tweet_id = 0

    print "Getting tweets for @{}".format(USER)
    while True:
        # get the latest tweet
        latest_tweet = t.statuses.user_timeline(screen_name=USER)[0]
        # say it and wobble chicken, if we haven't already said it
        if latest_tweet['id'] > last_tweet_id:
            print latest_tweet['text']
            chicken_wobble(True)
            say(latest_tweet['text'])
            chicken_wobble(False)
            last_tweet_id = latest_tweet['id']
        # wait for some time until we check again
        time.sleep(CHECK_INTERVAL)
