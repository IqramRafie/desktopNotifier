import requests
import xml.etree.ElementTree as ET

RSS_FEED_URL = "https://www.freemalaysiatoday.com/"

def loadRSS():
    resp = requests.get(RSS_FEED_URL)

    return resp.content

def parseXML(rss):

    root = ET.fromstring(rss)

    newsitems = []

    for item in root.findall('./home-news'):
        news = {}
        
        for child in item:

            if child.tag == '{http://search.yahoo.com/mrssss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')

        newsitems.append(news)
    
    return newsitems

def topStories():

    rss = loadRSS()

    newsitems = parseXML(rss)
    return newsitems