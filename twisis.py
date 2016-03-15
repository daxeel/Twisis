#! /usr/bin/env python
#
# MODULE NAME  : Twisis
# DESCRIPTION  : Python module for twitter Analysis
# AUTHOR       : Daxeel Soni
# AUTHOR EMAIL : sayhi@daxeelsoni.in
# AUTHOR WEB   : www.daxeelsoni.in
# FEATURES     : 1. Tweets Sentimental Analysis from hashtag (Intial feature)
#              - More features are under development.
#
# Copyright (c) 2016, Daxeel Soni
# All rights reserved.

import tweepy
import urllib

class Twisis(object):
	"""Python module for twitter Analysis"""

	# Connecting twitter API
	auth = tweepy.OAuthHandler('jiHQF74FShbbOEkg1pYX5bZj1', 'dIKY6SDkfGqyLCja9zsf4qtw7jVOFD2aG4cdI6FQs2sJtABxEH')
	auth.set_access_token('2547263228-pKM4XiZeRzOFCu9yREehZtL1vsJojW0jCCXEyCy', 'QYLMt9MpBJeKVOmzyap1dAMrv6aNZsd8mNbTcUI86sRnh')
	api = tweepy.API(auth)

	def __init__(self, hashtag, no_tweets):
		super(Twisis, self).__init__()
		self.hashtag = hashtag
		self.no_tweets = no_tweets
		
	def hashtag_analysis(self):
		final_data = []

		for each in range(self.no_tweets):
			print "Analysing tweet number : " + str(each+1) + '...'
			temp_dict = {}

			# Getting tweet
			tweet = Twisis.api.search('#'+self.hashtag)[each].text

			try:
				data = urllib.urlencode({"text": tweet}) 
				senti_request = urllib.urlopen("http://text-processing.com/api/sentiment/", data)
				senti_response = eval(senti_request.read())

				label = senti_response['label']
				positive_number = senti_response['probability']['pos']
				negative_number = senti_response['probability']['neg']
				neutral_number = senti_response['probability']['neutral']

				temp_dict['tweet'] = tweet
				temp_dict['label'] = label
				temp_dict['positive_number'] = positive_number
				temp_dict['negative_number'] = negative_number
				temp_dict['neutral_number'] = neutral_number

				final_data.append(temp_dict)
			except:
				print tweet

		return final_data



