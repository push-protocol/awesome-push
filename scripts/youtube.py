import requests
from bs4 import BeautifulSoup

def youtube(url):
    response = requests.get('https://www.youtube.com'+url)
    vid_url = 'https://www.youtube.com'+url
    title = 'Push Video' 
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title.text
    
    return {'url': vid_url, 'title': title}