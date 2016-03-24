from local_settings import *
import twitter
api = twitter.Api(consumer_key = CONSUMER_KEY,
                  consumer_secret = CONSUMER_SECRET,
                  access_token_key = ACCESS_TOKEN,
                  access_token_secret = ACCESS_TOKEN_SECRET)

# Update your status
def tweet(message):
  api.PostUpdate(message)
