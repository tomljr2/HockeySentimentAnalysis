import praw
import re
from collections import Counter
from nltk.corpus import stopwords

#This is from a file I made called authentication.py. It includes four
#constants. USERNAME (my username), PASSWORD (my password), CLIENTID
#(the developer id that I was given from reddit), and CLIENTSECRET (the
#secret id that was also supplied by reddit). If you want to run these
#scripts yourself, then you will need to create your own file with these
#constants for praw to work properly.
from authentication import *


#Number of submissions to look through. Just assume each submission
#takes 3 seconds and you can do the math as to how long you expect
#the program to take
NUMSUBMISSIONS = 1000

#We want to get an instance of reddit with the authentication we supplied
reddit = praw.Reddit(client_id = CLIENTID,
                     client_secret = CLIENTSECRET,
                     user_agent = "Hockey Emotions by /u/heavie1",
                     username = USERNAME,
                     password = PASSWORD)

subreddit = reddit.subreddit("hockey")

i=0
#Collect 1000 random submissions, take all of the comments, and
#store them together
for x in range(0,NUMSUBMISSIONS):
   for c in subreddit.random().comments:
      if i == 0:
         comments = c.body
      else:
         try:
            comments = comments + c.body
         except:
            i = i - 1
      i = i+1

#Turn the string of comments into a list of words
clist = comments.split()

#Remove the stopwords
clist = [word for word in clist if word not in stopwords.words('english')]

#Remove the words with non-alphabetic character
clist = [word for word in clist if word in re.sub('[^A-Za-z]','',word)]

#Convert all words to be lowercase
clist = [word.lower() for word in clist]

#Store the frequencies of each word into a file
file = open('TopWords.txt','w')
freq = Counter(clist).most_common()
for kv in freq:
	file.write(kv[0] + '\t\t\t' + str(kv[1]) + '\n')
file.close()
print i
