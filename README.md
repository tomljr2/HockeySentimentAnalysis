This program uses pushshift to collect comments containing some substring in Reddit 
from a specfic subreddit and perform a sentiment analysis on the comment to give an
idea of the opinion that people have towards that specific item. This was made with
hockey players in mind, however, it is general-purpose enough to work for any topic
in any subreddit. Made by Justin Tomlinson.

How to use:

	Using the script is quite simple. Simply, use the following command:

		python PlayerSentimentAnalysis.py -p  <Player> -s <Subreddit>

	The flags do the following:

		-p <PlayerName>		Player to analyze
		-s <Subreddit>		Subreddit to get comments from
		-c <NumberOfComments>	Number of comments to analyze
		-h,--help		Show the help menu

	If used correctly, it will output a count of positive (pos), negative (neg),
	and neutral (neu) comments about that player.
