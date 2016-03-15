# Example file tells you how to use twisis for twitter analytics
import twisis # Import module

# Create object with two parameters
# 1. hashtag - for which you want to do analysis
# 2. no_tweets - for how many tweets you want to do analysis
twisis_obj = twisis.Twisis('fashion', 2) 

# call hashtag_analysis for twisis object
done = twisis_obj.hashtag_analysis()

# print data
print done