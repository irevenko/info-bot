import requests
from bs4 import BeautifulSoup


def get_time(place):
	page = requests.get('https://www.google.com/search?client=firefox-b-d&q=time+in+'+place)
	soup = BeautifulSoup(page.text, "html.parser")
	parsed_time = soup.find_all('div', {'class': 'BNeawe iBp4i AP7Wnd'})[1].find_all(text=True, recursive=True)
	time = f'⏰ In {place} is {parsed_time[0]}'
	return time
