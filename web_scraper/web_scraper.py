import requests
from bs4 import BeautifulSoup
import json

domain = 'https://en.wikipedia.org'
wikipedia_url = f'{domain}/wiki/History_of_Mexico'
response = requests.get(wikipedia_url)
html_text = response.text

def get_citations_needed_count(wikipedia_url):
    result = requests.get(wikipedia_url)
    soup = BeautifulSoup(result.content, 'html.parser')
    find_all = soup.findAll('a',title='Wikipedia:Citation needed')
    return len(find_all)

def get_citations_needed_report(wikipedia_url):
    result = requests.get(wikipedia_url)
    soup = BeautifulSoup(result.content, 'html.parser')
    find_all_p = soup.findAll('p')
    all_p_has_citations = ""
    for p in find_all_p:
        if p.findChildren('span'):
            all_p_has_citations += p.text
            all_p_has_citations += '\n\n'

    return all_p_has_citations.strip()
# json_data = json.dumps(find_all)
# print(json_data)
# with open('json_data.json','w') as file:
#     file.write(json_data)


if __name__ == "__main__":
    print(get_citations_needed_count(wikipedia_url))
    print(get_citations_needed_report(wikipedia_url))