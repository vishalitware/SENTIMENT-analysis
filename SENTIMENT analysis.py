
# coding: utf-8

# In[1]:


from textblob import TextBlob


# In[2]:


Feedback1 = "the movie was awesome"
Feedback2 = " the movie was very good"
blob1 = TextBlob(Feedback1)
blob2 = TextBlob(Feedback2)
print(blob1.sentiment)
print(blob2.sentiment)


# In[3]:


import tweepy
from textblob import TextBlob


# In[7]:


consumer_key=''
consumer_token =''
access_token=''
access_token_secret=''
auth = tweepy.oAuthandeler(consumer_key.consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)
public_tweets = api.serach ('')
for tweet in public_tweets:
 print(tweet.text)
analysis = TextBlob(tweet.text)
print(analysis.sentiment)

