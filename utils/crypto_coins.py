import requests
import bs4 #For Monero price only, becouse API doesn't work for this coin

r = requests.get('https://www.coingecko.com/en/coins/monero')
soup = bs4.BeautifulSoup(r.text, "html.parser")
xmr_price = soup.find_all('span', {'class': 'no-wrap'})[0].find_all(text=True, recursive=True)

btc_response = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot")
btc_data = btc_response.json()
btc_price = btc_data["data"]["amount"]

eth_response = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/spot")
eth_data = eth_response.json()
eth_price = eth_data["data"]["amount"]

ltc_response = requests.get("https://api.coinbase.com/v2/prices/LTC-USD/spot")
ltc_data = ltc_response.json()
ltc_price = ltc_data["data"]["amount"]

dash_response = requests.get("https://api.coinbase.com/v2/prices/DASH-USD/spot")
dash_data = dash_response.json()
dash_price = dash_data["data"]["amount"]

zec_response = requests.get("https://api.coinbase.com/v2/prices/ZEC-USD/spot")
zec_data = zec_response.json()
zec_price = zec_data["data"]["amount"]

etc_response = requests.get("https://api.coinbase.com/v2/prices/ETC-USD/spot")
etc_data = etc_response.json()
etc_price = etc_data["data"]["amount"]

xrp_response = requests.get("https://api.coinbase.com/v2/prices/XRP-USD/spot")
xrp_data = xrp_response.json()
xrp_price = xrp_data["data"]["amount"]

coins = {
	"Bitcoin(BTC)": "BTC",
	"Litecoin(LTC)": "LTC",
	"Ethereum(ETH)": "ETH",
	"Ethereum Classic(ETC)": "ETC",
	"Zcash(ZEC)": "ZEC",
	"Dash(DASH)": "DASH",
	"Ripple(XPR)": "XRP",
	"Monero(XMR)": "XMR"
}
