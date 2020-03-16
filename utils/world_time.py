import requests
from bs4 import BeautifulSoup


def get_current_time(place):
    try:
        page = requests.get('https://24timezones.com/'+place+'/time')
        soup = BeautifulSoup(page.text, "html.parser")
        hours = soup.find_all('span', {'class': 'hours'})[0].find_all(text=True, recursive=True)
        minutes = soup.find_all('span', {'class': 'minutes'})[0].find_all(text=True, recursive=True)
        seconds = soup.find_all('span', {'class': 'seconds'})[0].find_all(text=True, recursive=True)
        am_or_pm = soup.find_all('sup')[0].find_all(text=True, recursive=True)
        time = f'⏰  In {place} is {hours[0]}:{minutes[0]}:{seconds[0]} {am_or_pm[0].upper()}'
        return time
    except IndexError:
        page = requests.get('https://24timezones.com/'+place+'/time')
        soup = BeautifulSoup(page.text, "html.parser")
        parsed_time = soup.find_all('span', {'id': 'currentTime0'})[0].find_all(text=True, recursive=True)
        time = f'⏰  In {place} is currently {parsed_time[0][:10]}'
        return time
