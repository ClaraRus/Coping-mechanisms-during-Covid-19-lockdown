import json
import pickle
import os

from dataset.Data import Data
from dataset.Tweets import Tweet




def read_json_file(path_json):
    tweets = []
    with open(path_json, encoding='utf-8') as json_file:
        json_list = list(json_file)

        for json_str in json_list:
           tweets_json = json.loads(json_str)
           for t in tweets_json:
            date = t['created_at']
            text = t['full_text']
            location = t['user']['location']
            hashtags = t['entities']['hashtags']

            tweet = Tweet(date, text, location, path_json, hashtags)
            tweet.preprocess_data()
            tweets.append(tweet)
    return tweets


def load_tweets_dataset(path_folder):
    tweets = []
    for file in os.listdir(path_folder):
        tweets.extend(read_json_file(os.path.join(path_folder, file)))

    return tweets


def read_data_file(directory):
    data = []
    for f in sorted(os.listdir(directory)):
        with open(os.path.join(directory, f), 'r') as file:
            if f[:-4] == 'TXT':
                if 'Dementia' in f:
                    location = 'Oxford'
                    text = file.read()
                    date = '2020'
                    d = Data(date, text, location, os.path.join(directory, f))
                    data.append(d)
                if 'BBC' in f:
                    location = f.split('_')[1]
                    lines = file.readlines()
                    date = lines[0].split(':').strip()
                    text = ' '.join([line for line in lines if
                                     'Date' not in line and '-->' not in line and not line.strip().isnumeric()])
                    d = Data(date, text, location, os.path.join(directory, f))
                    data.append(d)

                if 'UNICEF' in f:
                    date = '2020'
                    text = file.read()
                    location = f.split('_')[1]
                    d = Data(date, text, location, os.path.join(directory, f))
                    data.append(d)
                else:
                    location = 'Melbroune'
                    texts = file.read()
                    date = '2020'
                    for text in texts.split('\n'):
                        if len(text.strip() > 0):
                            d = Data(date, text, location, os.path.join(directory, f))
                            data.append(d)
    return data


def load_data(path_dataset):
    data = []
    for directory in sorted(os.listdir(path_dataset)):
      path = os.path.join(path_dataset, directory)
      if os.path.isdir(path):
        print(directory)
        if directory == 'Tweets_Filter':
            data.extend(load_tweets_dataset(path))
        elif not directory == 'Tweets':
            data.extend(read_data_file(path))

    with open(os.path.join(path_dataset,'dataset.data'), 'wb') as filehandle:
        # store the data as binary data stream
        pickle.dump(data, filehandle)

    return data


if __name__ == "__main__":
    path_dataset = 'C:\\Users\\Clara2\\Documents\\Radboud_Master\\Text and Multimedia Mining\\'
    load_data(path_dataset)