import requests
from bs4 import BeautifulSoup
import re
import json

with open('data/URLs.txt', 'r') as file:
    urls = file.readlines()[0].split(' ')

output = []

for url in urls:
    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')

        pattern_for_title = r'<h1 class="text-4xl lg:text-5xl max-w-2xl mb-4">\s*(.*?)\s*</h1>'
        match_for_title = re.search(pattern_for_title, soup.prettify())

        if match_for_title:
            title = match_for_title.group(1)
        else:
            title = "Push Protocol's Project" 

        pattern_for_shot = r'<p class="lg:text-lg text-black-500 clamp-3">\s*(.*?)\s*</p>'
        match_for_shot = re.search(pattern_for_shot, soup.prettify())

        if match_for_shot:
            shot = match_for_shot.group(1)
        else:
            shot = "An extraordinary project that implemented Push SDK."

        source_code = soup.find('a', string='Source Code')

        if source_code and 'href' in source_code.attrs:
            github_repo = source_code['href']
        else:
            github_repo = url
        
        project_obj = {"title": title, "shot": shot, "source_code": github_repo, "url": url}
        output.append(project_obj)
    else:
        pass

with open('data/PROJECTS.json', 'w') as json_file:
    json.dump(output, json_file, indent=4)