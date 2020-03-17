import requests
from bs4 import BeautifulSoup

fb_request = requests.get('https://finance.yahoo.com/quote/FB?p=FB')
soup = BeautifulSoup(fb_request.text, "html.parser")
fb_parsed = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find_all(text=True, recursive=True)
fb_price = f'${fb_parsed[0]}'
fb_stats = f'📉Statistics:  {fb_parsed[1]}'
fb_stocks = f'{fb_price}\n{fb_stats}'


tsla_request = requests.get('https://finance.yahoo.com/quote/TSLA?p=TSLA')
soup = BeautifulSoup(tsla_request.text, "html.parser")
tsla_parsed = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find_all(text=True, recursive=True)
tsla_price = f'${tsla_parsed[0]}'
tsla_stats = f'📉Statistics:  {tsla_parsed[1]}'
tsla_stocks = f'{tsla_price}\n{tsla_stats}'


goog_request = requests.get('https://finance.yahoo.com/quote/GOOG?p=GOOG')
soup = BeautifulSoup(goog_request.text, "html.parser")
goog_parsed = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find_all(text=True, recursive=True)
goog_price = f'${goog_parsed[0]}'
goog_stats = f'📉Statistics:  {goog_parsed[1]}'
goog_stocks = f'{goog_price}\n{goog_stats}'


amzn_request = requests.get('https://finance.yahoo.com/quote/AMZN?p=AMZN')
soup = BeautifulSoup(amzn_request.text, "html.parser")
amzn_parsed = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find_all(text=True, recursive=True)
amzn_price = f'${amzn_parsed[0]}'
amzn_stats = f'📉Statistics:  {amzn_parsed[1]}'
amzn_stocks = f'{amzn_price}\n{amzn_stats}'


apl_request = requests.get('https://finance.yahoo.com/quote/AAPL?p=AAPL')
soup = BeautifulSoup(apl_request.text, "html.parser")
apl_parsed = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find_all(text=True, recursive=True)
apl_price = f'${apl_parsed[0]}'
apl_stats = f'📉Statistics:  {apl_parsed[1]}'
apl_stocks = f'{apl_price}\n{apl_stats}'


msft_request = requests.get('https://finance.yahoo.com/quote/MSFT?p=MSFT')
soup = BeautifulSoup(msft_request.text, "html.parser")
msft_parsed = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find_all(text=True, recursive=True)
msft_price = f'${msft_parsed[0]}'
msft_stats = f'📉Statistics:  {msft_parsed[1]}'
msft_stocks = f'{msft_price}\n{msft_stats}'


intl_request = requests.get('https://finance.yahoo.com/quote/INTC?p=INTC')
soup = BeautifulSoup(intl_request.text, "html.parser")
intl_parsed = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find_all(text=True, recursive=True)
intl_price = f'${intl_parsed[0]}'
intl_stats = f'📉Statistics:  {intl_parsed[1]}'
intl_stocks = f'{intl_price}\n{intl_stats}'

nvda_request = requests.get('https://finance.yahoo.com/quote/NVDA?p=NVDA')
soup = BeautifulSoup(nvda_request.text, "html.parser")
nvda_parsed = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find_all(text=True, recursive=True)
nvda_price = f'${nvda_parsed[0]}'
nvda_stats = f'📉Statistics:  {nvda_parsed[1]}'
nvda_stocks = f'{nvda_price}\n{nvda_stats}'


stocks = {
	"Facebook": "FB",
	"Tesla": "TSLA",
	"Google": "GOOG",
	"Amazon": "AMZN",
	"Apple": "APL",
	"Microsoft": "MSFT",
	"Intel": "INTL",
	"NVIDIA": "NVDA"
}
