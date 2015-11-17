#!/usr/bin/env python

# system tools
import os, sys, pprint

# api tools
import requests, base64, json

# handy
from unidecode import unidecode

sys.path.append('..')  
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings') 

import django
django.setup()

from main.models import Tweets

CONSUMER_KEY = 'PNCy4kyT48gsLMZwQFTeyq9YK'  
CONSUMER_SECRET = 'mileb5QHPNJaDgPXHUgHlUNjkAwKM1zFvnmqJNJlOftIshLBU5'

# the base twitter url for sending api requests
URL = 'https://api.twitter.com/oauth2/token'

# the search term to be used
SEARCH_TERM = 'techcrunch'

# base twiter url for sending api request
credentials = base64.urlsafe_b64encode('%s:%s' % (CONSUMER_KEY, CONSUMER_SECRET))

custom_headers = {  
                    'Authorization': 'Basic %s' % (credentials),
                    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                 }

grant_type_data = 'grant_type=client_credentials'

# putting it all togerther
response = requests.post(URL, headers=custom_headers, data=grant_type_data)

# what is in this thing
print response.json()

# dump the token to  variable
access_token = response.json().get('access_token')
# access_token = response.json()['access_token']

search_headers = {'Authorization': 'Bearer %s' % (access_token)}

response = requests.get('https://api.twitter.com/1.1/search/tweets.json?q=%s&count=100' % SEARCH_TERM, headers=search_headers)
# print response.json()

pp = pprint.PrettyPrinter(indent=2)

# print response.json().get('statuses')[0].keys()
# print response.json().get('statuses')[0]['text']
# print response.json().get('statuses')[0]['user'].keys()

# pp.pprint(response.json().get('statuses'))
# pp.pprint(response.json().get('statuses')[1]['user'])

# profile_image_url, screen_name, created_at, time)zone, location

# tweet_list=response.json().get('statuses')

# for tweet in tweet_list:
#     tweet_location = tweet.get('user').get('location')

#     if tweet_location !=''and tweet_location != None:

#         print "TWEET------------"
#         print tweet.get('user').get('profile_image_url')
#         print tweet.get('user').get('screen_name')
#         print tweet.get('user').get('created_at')
#         # print tweet.get('user').get('time)zone')
#         print tweet.get('user').get('location')
#         print "TWEET-TEXT--------"
#         print tweet.get('text')

# include a field for search term on the tweet model

tweet_list = response.json().get('statuses')

for tweet in tweet_list:
    tweet_location = tweet.get('user').get('location')

    if tweet_location != None and tweet_location != '':
        if unidecode(tweet.get('text')) != None:
            new_tweet, created = Tweets.objects.get_or_create(text=str(unidecode(tweet.get('text'))))
            if tweet.get('user').get('profile_image_url') != None:
                new_tweet.profile_image_url = str(unidecode(tweet.get('user').get('profile_image_url')))
            if tweet.get('user').get('screen_name') != None:
                new_tweet.screen_name = str(unidecode(tweet.get('user').get('screen_name'))) 
                new_tweet.created_at = tweet.get('user').get('created_at')
                new_tweet.location = str(unidecode(tweet_location))
                new_tweet.search_term = SEARCH_TERM

            new_tweet.save()
            print new_tweet
            print ''
