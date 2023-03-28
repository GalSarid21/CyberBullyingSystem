from DbWriter.tweepy_setup import TweepyWrapper


def run_tweepy_stream_test():
    tweepy = TweepyWrapper("Data\\local.ini", ['python', 'programming', 'coding'], 20)
    tweets = tweepy.stream_tweets()
    a=1