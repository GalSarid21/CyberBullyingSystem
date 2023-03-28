import tweepy
from configparser import ConfigParser


class TweepyWrapper():

    def __init__(self, config_file_name: str) -> None:
        config = ConfigParser()
        config.read(config_file_name)
        self.__api_key = config.get('Twitter', 'ApiKey')
        self.__api_secret = config.get('Twitter', 'ApiSecret')
        self.__bearer_token = config.get('Twitter', 'BearerToken')
        self.__access_token = config.get('Twitter', 'AccessToken')
        self.__access_token_secret = config.get('Twitter', 'AccessTokenSecret')
    
    def stream_tweets(self):
        client = tweepy.Client(self.__bearer_token, 
                               self.__api_key, self.__api_secret,
                               self.__access_token, self.__access_token_secret)
        auth = tweepy.OAuth1UserHandler(self.__api_key, self.__api_secret,
                                        self.__access_token, self.__access_token_secret)
        api = tweepy.API(auth)
        stream_client = _MyStreamClient(client = client, bearer_token=self.__bearer_token)
        search_terms = ['python', 'programming', 'coding']
        for term in search_terms:
            stream_client.add_rules(tweepy.StreamRule(term))
        stream_client.filter(tweet_fields=['referenced_tweets', 'author_id'])
        return stream_client.get_tweets()
    

class _MyStreamClient(tweepy.StreamingClient):

    def __init__(self, client, bearer_token):
        super().__init__(bearer_token=bearer_token)
        self.__client = client
        self.__tweets = {}
        self.__limit = 3

    def on_connect(self) -> None:
        print('connected\n')

    def on_disconnect(self) -> None:
        print('disconnected\n')

    def on_errors(self, errors):
        self.disconnect()
        return super().on_errors(errors)

    def on_tweet(self, tweet):
        if tweet.referenced_tweets is None:
            author_id = tweet.data['author_id']
            user = self.__client.get_user(id=author_id)
            user_name = user.data['name']
            print(f'user_name: {user_name} | tweet: {tweet.text}\n')
            entry = {str(user_name): str(tweet.text)}
            self.__tweets.update(entry)
        
        if len(self.__tweets) == self.__limit:
            self.disconnect()
            return False
        return True

    def get_tweets(self):
        return self.__tweets

