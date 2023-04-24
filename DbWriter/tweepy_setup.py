import tweepy
import time
from datetime import datetime
from DAL.twitter_dto import TweetDto
from configparser import ConfigParser
from Utils.string import StringUtils
from typing import Iterable


class TweepyWrapper():

    def __init__(self, config: ConfigParser, search_terms_str: str) -> None:
        self.__api_key = config.get('Twitter', 'ApiKey')
        self.__api_secret = config.get('Twitter', 'ApiSecret')
        self.__bearer_token = config.get('Twitter', 'BearerToken')
        self.__access_token = config.get('Twitter', 'AccessToken')
        self.__access_token_secret = config.get('Twitter', 'AccessTokenSecret')
        self.__limit = int(config.get('Twitter', 'Limit'))
        self.__timeout_seconds = float(config.get('Twitter', 'TimeOut'))
        self.__retries = int(config.get('Twitter', 'Retries'))
        self.__search_terms = search_terms_str.split(',')
    
    def stream_tweets(self) -> Iterable[TweetDto]:
        for _try in range(0, self.__retries):
            try:
                client = tweepy.Client(self.__bearer_token, 
                                    self.__api_key, self.__api_secret,
                                    self.__access_token, self.__access_token_secret)
                auth = tweepy.OAuth1UserHandler(self.__api_key, self.__api_secret,
                                                self.__access_token, self.__access_token_secret)
                api = tweepy.API(auth, wait_on_rate_limit=True)
                    
                stream_client =  _MyStreamClient(client, self.__bearer_token, self.__limit, self.__timeout_seconds)
                previousRules = stream_client.get_rules().data
                if previousRules:
                    stream_client.delete_rules(previousRules)
                for term in self.__search_terms:
                    stream_client.add_rules(tweepy.StreamRule(term))
                stream_client.filter(tweet_fields=['referenced_tweets', 'author_id', 'lang'])
                break
            except Exception as e:
                print(f'Cought exception: {e}\nInitiate time.sleep')
                time.sleep(120)
                print(f'Start retry number: {_try + 1}')
        return stream_client.get_tweets()
    

class _MyStreamClient(tweepy.StreamingClient):

    def __init__(self, client: tweepy.Client, bearer_token: str, limit: int, timeout_seconds: float) -> None:
        super().__init__(bearer_token=bearer_token)
        self.__client = client
        self.__limit = limit
        self.__start_time = None
        self.__timeout_seconds = timeout_seconds
        self.__tweets = []

    def on_connect(self) -> None:
        self.__start_time = datetime.utcnow()
        print('\nconnected\n')

    def on_disconnect(self) -> None:
        print('disconnected\n')

    def on_errors(self, errors):
        self.disconnect()
        return super().on_errors(errors)

    def on_tweet(self, tweet) -> bool:
        if tweet.referenced_tweets is None:
            author_id = tweet.data['author_id']
            user = self.__client.get_user(id=author_id)
            user_name = user.data['name']
            
            is_english_user_name = StringUtils.is_english_chars(user_name)
            is_english_text = tweet.data['lang'] == 'en' and StringUtils.is_english_chars(tweet.text)
            is_content_exists = any(tweet.text.lower() == t.content.lower() for t in self.__tweets)
            
            if is_english_text and is_english_user_name and not is_content_exists:
                print(f'user_name: {user_name} | tweet: {tweet.text}\n')
                self.__tweets.append(TweetDto(user_name, tweet.text))
        
        duration = datetime.utcnow() - self.__start_time
        if len(self.__tweets) >= self.__limit or duration.seconds >= self.__timeout_seconds:
            self.disconnect()
            return False
        return True

    def get_tweets(self) -> Iterable[TweetDto]:
        return self.__tweets

