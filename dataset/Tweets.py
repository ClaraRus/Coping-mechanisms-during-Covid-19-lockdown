import re

from dataset.Data import Data


class Tweet(Data):
    def __init__(self, date, text, location, path_file, hashtags):
        super().__init__(date, text, location, path_file)
        self.hashtags = hashtags

    # uses a regex to detect usernames and replaces them by USERNAME
    def replace_username(self, in_string):
        return re.sub('@(\w){1,15}', 'USERNAME', in_string)

    # uses a regex to detect hashtags and replaces them by HASHTAG
    def replace_hashtag(self, in_string):
        return re.sub('#(\w)*', 'HASHTAG', in_string)

    # uses a regex to detect links and replaces them by LINK
    def replace_link(self, in_string):
        return re.sub('(http:)?//t.co/\w*', 'LINK', in_string)

    def preprocess_data(self):
        # TO DO: date in the same format

        self.text = self.replace_username(self.text)
        self.text = self.replace_hashtag(self.text)
        self.text = self.replace_link(self.text)

        # We keep retweets as we maybe d1o not have the original tweet in the sampled dataset, only remove duplicates
        self.text.replace('RT ', '')

    def __eq__(self, other):
        return self.text == other.text
