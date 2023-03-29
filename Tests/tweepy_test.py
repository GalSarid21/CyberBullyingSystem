from configparser import ConfigParser
from DbWriter.tweepy_setup import TweepyWrapper


def run_tweepy_stream_test():
    config = ConfigParser()
    config.read("Data\\local.ini")
    tweepy = TweepyWrapper(config)
    tweets = tweepy.stream_tweets()