import argparse, sys
import requests
import json
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#Parse the command line arguments to allow ease of use for the user
parser = argparse.ArgumentParser(usage = 'usage: PlayerSentimentAnalysis.py [-h] -p <PlayerName> -s <Subreddit> [-c <NumberOfComments>]')
optional = parser._action_groups.pop()
required = parser.add_argument_group('required arguments')

required.add_argument('-p', type = str, help = 'Player/item that you want to test', required = True)
required.add_argument('-s', type = str, help = 'Subreddit to search in', required = True)
optional.add_argument('-c', type = int, help = 'The number of comments to test')
parser._action_groups.append(optional)

#Set the player and subreddit to the argument given,
#and set the number of comments if it was given
PLAYER = parser.parse_args().p
SUBREDDIT = parser.parse_args().s
if parser.parse_args().c == None:
   NUMCOMMENTS = 1000
else:
   NUMCOMMENTS = parser.parse_args().c

#Call the API to get the comments
url = 'https://api.pushshift.io/reddit/search/comment/?q=' + PLAYER + '&size=' + str(NUMCOMMENTS) + '&subreddit=' + SUBREDDIT
response = requests.get(url)

#Get the sentiment intensity analyzer
sia = SentimentIntensityAnalyzer()
pos = 0
neu = 0
neg = 0

#Get a score for each comment and increment
#the positive, negative, and neutral counters
for comment in response.json()['data']:
   ss = sia.polarity_scores(comment['body'])
   if ss.values()[3] > 0:
      pos = pos + 1
   elif ss.values()[3] < 0:
      neg = neg + 1
   else:
      neu = neu + 1

#Print the results
print 'pos = ' + str(pos) + '\tneu = ' + str(neu) + '\tneg = ' + str(neg)

