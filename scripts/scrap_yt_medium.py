import requests
from bs4 import BeautifulSoup
import re
import json
from youtube import youtube

# Scrap Youtube

url = 'https://www.youtube.com/@pushprotocol/videos'
vid_obj = {}

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    pattern = r'"url":"(/watch\?v=[\w-]+)"'
    extracted_urls = re.findall(pattern, soup.prettify())
    
    videos = []

    i = 0
    for url in extracted_urls:
        if i == 5:
            break
        data = youtube(url)
        videos.append(data)
        i = i+1

    vid_obj = videos
    
else:
    print(f"Failed to retrieve the webpage: Status code {response.status_code}")


# Scrap Medium


url = 'https://medium.com/push-protocol'
art_obj = []

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    a_tags = soup.find_all('a', class_='u-block')
    extracted_data = []

    for a_tag in a_tags:
        url = a_tag['href']
        name = a_tag.find('span', class_='u-textScreenReader').text.strip()
        extracted_data.append({"name": name, "url": url})
    
    art_obj = extracted_data
    
else:
    print(f"Failed to retrieve the webpage: Status code {response.status_code}")


with open('markdowns/INTRODUCTION.md', 'w') as file:

    file.write('<h3 align="center">Recent Releases</h3>\n\n')
    file.write('#### Top Videos\n')

    for vid in vid_obj:
        file.write(f"- [{vid['title']}]({vid['url']})")
        file.write('\n')

    file.write('#### Top Articles\n')
    i = 0
    for vid in art_obj:
        if i == 5:
            break
        file.write(f"- [{vid['name']}]({vid['url']})")
        file.write('\n')
        i = i+1

    file.write('#### Top Projects\n')

    with open('data/PROJECTS.json', 'r') as f:
        project_obj = json.load(f)

        for project in project_obj:
            file.write(f"- **{project['title']}**: {project['shot']} [Code]({project['source_code']}) | [Link]({project['url']})")
            file.write('\n')