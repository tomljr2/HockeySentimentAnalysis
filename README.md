This is a set of programs to give a way to see who the most popular players
are on /r/hockey, and to perform a sentiment analysis on players to see how
they are perceived by users on /r/hockey. Made by Justin Tomlinson.

Files:

	MostFrequentWords.py
	
		This file is used to get the most frequently used words in
		/r/hockey. It does this by taking x number of random 
		submissions and all of the comments in that post. 

		It will remove any stopwords, any non-alphabetic
		words, and it will convert all words to lowercase. Then
		it will take the words and their frequency and save them in
		a file called TopWords.txt. From here, you can roughly find 
		the most commonly mentioned players.

How to use:

	To use MostFrequentWords.py, in the command line type:
	
	python MostFrequentWords.py

	You will need praw, nltk, and a file you will create called 
	authentication.py which contains the following constants:

		USERNAME - your reddit username
		PASSWORD - your reddit password
		CLIENTID - the client id supplied for developers by reddit
		CLIENTSECRET - the secret id supplied for developers by reddit

	There is also a constant in MostFrequentWords called NUMSUBMISSIONS
	that is 1,000 by default. This is how many random submissions it will
	look through. You can assume that there is around 20-30 comments per
	submission, so if you want 1,000 comments, then 40-50 submissions
	should be enough. In my case, I want closer to 30,000.
