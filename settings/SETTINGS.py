""" SETTINGS
What the bot should post on Twitter:
If a Type is True than the Bot post it. (If a Type is False than the Bot dont post it)
"""

lang = "en"

# Leaks CONFIG
leaks =             True
leaksimagetext =    f"Twin1 Leaks" # Text in the Image
leaksimageurl =     "https://i.pinimg.com/originals/33/11/92/3311924db62ceef62a4a7ee87017280f.jpg" # Need to be a URL | The best is a colored background
# Shop CONFIG
shop =              True
shopimagetext =     f"Fortnite Item Shop" # Text in the Image
shopimageurl =      "https://i.pinimg.com/originals/33/11/92/3311924db62ceef62a4a7ee87017280f.jpg" # Need to be a URL | The best is a colored background
#### OTHER Features ####
newsfeed =          True
staging =           True
blogposts =         True
ingamebugmessage =  True
featuredislands =   True
playlist =          True
intervall = 30 # Under 20 Seconds is not allowed.


""" TWITTER_TOKEN
Enter here you Twitter Tokens from https://developer.twitter.com/en/apps
"""
TWITTER_TOKEN = {
    "consumer_key": "consum",
    "consumer_secret": "consuer",
    "access_token_key": "consumer",
    "access_token_secret": "consume",
}

nopost = False # A FUNCTION FOR TESTING! Leave it on False or the Bot dont work!!!!
