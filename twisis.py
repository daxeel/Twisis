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

# Import required modules
import tweepy
import urllib
import plotly
from plotly.graph_objs import Bar, Layout

class Twisis(object):
	"""Python module for twitter Analysis"""

	# Connecting twitter API
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	def __init__(self, hashtag, no_tweets):
		super(Twisis, self).__init__()
		self.hashtag = hashtag
		self.no_tweets = no_tweets
		
	def hashtag_analysis(self, plot, a_type):
		final_data = []

		for each in range(self.no_tweets):
			print "Analysing tweet number : " + str(each+1) + '...'
			temp_dict = {}

			# Getting tweet
			tweet = Twisis.api.search('#'+self.hashtag)[each].text
			tweet = tweet.encode('utf-8')

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

		if plot==True:
			# Get positivity number of tweets for y axis
			pos_data = []
			plot_title = ""
			for each in final_data:
				if a_type=='pos':
					pos_data.append(each['positive_number'])
					plot_title = "Positive sentimental analytics for recent tweets of #"+self.hashtag
				elif a_type=='neg':
					pos_data.append(each['negative_number'])
					plot_title = "Negative sentimental analytics for recent tweets of #"+self.hashtag
				elif a_type=='neu':
					pos_data.append(each['neutral_number'])
					plot_title = "Neutral sentimental analytics for recent tweets of #"+self.hashtag

			# Create label list for x axix
			labels = []
			for each in range(len(pos_data)):
				labels.append("Tweet-" + str(each+1))

			# Plot the graph
			plotly.offline.plot({
				"data": [
				    Bar(x=labels, y=pos_data)
				],
				"layout": Layout(
				    title=plot_title
				)
			})
		return final_data