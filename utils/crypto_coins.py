import requests
import bs4 #For Monero price only, becouse API doesn't work for this coin

xmr_request = requests.get('https://www.coingecko.com/en/coins/monero')
soup = bs4.BeautifulSoup(xmr_request.text, "html.parser")
raw_xmr = soup.find_all('span', {'class': 'no-wrap'})[0].find_all(text=True, recursive=True)
xmr_price = ''.join([str(elem) for elem in raw_xmr]) 

btc_request = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot")
btc_data = btc_request.json()
btc_price = btc_data["data"]["amount"]

eth_request = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/spot")
eth_data = eth_request.json()
eth_price = eth_data["data"]["amount"]

ltc_request = requests.get("https://api.coinbase.com/v2/prices/LTC-USD/spot")
ltc_data = ltc_request.json()
ltc_price = ltc_data["data"]["amount"]

dsh_request = requests.get("https://api.coinbase.com/v2/prices/DASH-USD/spot")
dsh_data = dsh_request.json()
dsh_price = dsh_data["data"]["amount"]

zec_request = requests.get("https://api.coinbase.com/v2/prices/ZEC-USD/spot")
zec_data = zec_request.json()
zec_price = zec_data["data"]["amount"]

etc_request = requests.get("https://api.coinbase.com/v2/prices/ETC-USD/spot")
etc_data = etc_request.json()
etc_price = etc_data["data"]["amount"]

xrp_request = requests.get("https://api.coinbase.com/v2/prices/XRP-USD/spot")
xrp_data = xrp_request.json()
xrp_price = xrp_data["data"]["amount"]

coins = {
	"Bitcoin(BTC)": "BTC",
	"Litecoin(LTC)": "LTC",
	"Ethereum(ETH)": "ETH",
	"Ethereum Classic(ETC)": "ETC",
	"Zcash(ZEC)": "ZEC",
	"Dash(DSH)": "DSH",
	"Ripple(XPR)": "XRP",
	"Monero(XMR)": "XMR"
}
