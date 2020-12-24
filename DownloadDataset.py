import urllib.request as url
import re

def get_links():
    f = open('./Tweets.txt','r')
    text = f.read()
    f.close()
    #links = text.split('\n')
    links = re.findall('"https:.+" ',text)
    f = open('./Tweets_Links.txt', 'w')
    for link in links:
        f.write(str(link))
        f.write('\n')
    f.close()

print('Beginning file download with urllib2...')
f = open('./Tweets_Links.txt', 'r')
text = f.read()
links = text.replace("\"", "").split('\n')
index=0
for link in links:
    print(link)
    save_path = str(index)
    if index >=31:
        save_path += ".zip"
    else: save_path += '.csv'
    url.urlretrieve(link, './Tweets/'+save_path)
    index=index+1

