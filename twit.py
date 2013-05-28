from twitter import *
from local_settings import *

t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

# Update your status
def tweet(message):
  t.statuses.update(status=message)
