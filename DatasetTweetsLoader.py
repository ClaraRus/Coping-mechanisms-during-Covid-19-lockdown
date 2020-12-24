import json

import pandas as pd
import os
import random

MAX_NUM_SAMPLES = 1500

def is_retweet(string, tweets):
    if string.startswith('RT '):
        if len([t for t in tweets if t['full_text'].replace('RT ', '') == string.replace('RT ', '')]) > 0:
            return True
    return False



def is_lockdown_tweet(string):
    keywords = ['homeschooling', 'hometasking', 'quarantine', 'lockdown', 'work from home',
                'workfromhome', 'working from home', 'workingfromhome', 'stayhomestaysafe', 'homeschool',
                'stayathome', 'stayhome', 'selfisolating', 'self isolating']

    for key in keywords:
        if key in string:
            return True
    return False


def filter_tweets(path_json, out_path):
    file_name = os.path.join(out_path, path_json.split('\\')[-1])
    print(file_name)
    tweets = []
    index = 0
    with open(path_json, encoding='utf-8') as json_file:
        json_list = list(json_file)
        for json_str in json_list:
            print(index)
            index +=1
            if json_str.startswith('{'):
                t = json.loads(json_str)
                text = t['full_text']
                if is_retweet(text, tweets) or not is_lockdown_tweet(text) or 'beer' in text: #corono beer tweets are filtered out
                    continue
                tweets.append(t)

    print(len(tweets))
    if len(tweets) > MAX_NUM_SAMPLES:
        tweets = random.sample(tweets, MAX_NUM_SAMPLES)
    if len(tweets) > 0:
        with open(file_name, 'w') as outfile:
             json.dump(tweets, outfile)



def convert_tweets_to_csv():
    path = 'C:\\Users\\Clara2\\Documents\\Radboud_Master\\Text and Multimedia Mining\\Tweets\\Tweets\\'
    for file in os.listdir(path):
        print(file)
        dataframe = pd.read_csv(path + file, header=None)
        dataframe = dataframe[0]
        dataframe.to_csv(
            'C:\\Users\\Clara2\\Documents\\Radboud_Master\\Text and Multimedia Mining\\Tweets\\Tweets Ready\\' + file,
            index=False, header=None)


def sample_tweets():
    in_path = 'C:\\Users\\Clara2\\Documents\\Radboud_Master\\Text and Multimedia Mining\\Tweets\\Tweets Ready\\'
    out_path = 'C:\\Users\\Clara2\\Documents\\Radboud_Master\\Text and Multimedia Mining\\Tweets\\Tweets_Sampled_50000\\'
    files = os.listdir(in_path)
    for index in sorted(range(0, len(files))):
        with open(os.path.join(in_path, files[index]), 'r') as f:
            if index == 1 or index == 2:  # represents the same day
                ids += f.read()
            else:
                ids = f.read()

            if index >= 2:
                ids = ids.split('\n')
                sampled_ids = random.sample(ids, 50000)
                with open(os.path.join(out_path, files[index]), 'w') as out_f:
                    out_f.write('\n'.join(sampled_ids))


if __name__ == "__main__":
    # convert_tweets_to_csv()
    # sample_tweets()

    path = 'C:\\Users\\Clara2\\Documents\\Radboud_Master\\Text and Multimedia Mining\\Tweets\\Tweets_Hydrator_50000\\corona_tweets_42.jsonl'
    out_path = 'C:\\Users\\Clara2\\Documents\\Radboud_Master\\Text and Multimedia Mining\\Tweets\\Tweets_Filter\\'
    filter_tweets(path, out_path)
