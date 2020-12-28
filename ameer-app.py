# Short code
import tweepy
api_key = '5yzVD5AevD0iS1Vtq8xdtjTHM'
api_secret_key = 'wm4qfl0T8eQZJil1BZiTrIpgmbpOtCeJSxZ5KqCYpb9OCJy5nR'
access_token='1298472286278696960-KofXQp0X6uQ4x40zxZaB0J5MttcuRr'
access_token_secret= '1pjsFSdPEroro5sAltriSYvNFF9wHEMo3QUssnNnf1yp2'

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

import time
while True:
  user = api.get_user('AnanyaMallik3')
  follower= user.followers_count
  api.update_profile(name= f'Ananya {follower} follows')
  print(f'Ananya {follower} follows')
  time.sleep(60)
