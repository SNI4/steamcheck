import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.5.810 Yowser/2.5 Safari/537.36'
}

def parse(username, url):
    #username = username + ' ; '
    if 'id' in url[:36]:
        url = f'https://steamcommunity.com/id/{url[30:]}/friends/'
    elif 'profiles' in url[:36]:
        url = f'https://steamcommunity.com/profiles/{url[36:]}/friends/'
    r = requests.get(url, headers=headers)
    page = BeautifulSoup(r.text, 'html.parser')
    if username in str(page.find_all('a', class_='selectable_overlay')):
        return(f'[{r.status_code}] | [{url}] | [+]')
    else:
        return(f'[{r.status_code}] | [{url}] | [-]')