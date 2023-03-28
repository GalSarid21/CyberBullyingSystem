from DbWriter.tweepy_setup import TweepyWrapper


def run_tweepy_stream_test():
    tweepy = TweepyWrapper("Data\\local.ini")
    tweets = tweepy.stream_tweets()
    a=1