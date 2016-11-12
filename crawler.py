import re
import requests
from bs4 import BeautifulSoup


def get_seasons(season):
    episodes = []
    for episode in range(1, 15):
        voice_original = '&voice=3'
        if episode <= 9:
            url = 'http://southpark.cc-fan.ru/series.php?id=' + str(season) + '0' + str(episode) + voice_original
        else:
            url = 'http://southpark.cc-fan.ru/series.php?id=' + str(season) + str(episode) + voice_original
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        link = soup.findAll('script')[19].string
        file = re.search(r'http:/\/m.+mp4', link)
        # return file.group(0)
        episodes.append(file.group(0))
    print(episodes)
    return episodes

x = str(input('Enter season: '))
get_seasons(x)
