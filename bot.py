import telebot
import pyowm
import pyowm.exceptions
import time
from telebot import types
from pyowm.exceptions import api_response_error
from newsapi import NewsApiClient
from secrets import BOT_TOKEN, OWM_TOKEN, NEWS_TOKEN  #from config import *
from utils.weather import get_forecast
from utils.world_time import get_time
from utils.news import get_article
from utils.stocks import *
from utils.crypto_coins import *

bot = telebot.TeleBot(BOT_TOKEN, threaded=False)
owm = pyowm.OWM(OWM_TOKEN)
api = NewsApiClient(api_key=NEWS_TOKEN)


@bot.message_handler(commands=['start'])
def command_start(message):
	start_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
	start_markup.row('/start', '/help', '/hide')
	start_markup.row('/weather', '/crypto', '/world_time')
	start_markup.row('/stocks', '/news')
	bot.send_message(message.chat.id, "🤖 The bot has started!\n⚙ Enter /help to see bot's function's")
	bot.send_message(message.from_user.id, "⌨️ The Keyboard is added!\n⌨️ /hide To remove kb ", reply_markup=start_markup)


@bot.message_handler(commands=['hide'])
def command_hide(message):
	hide_markup = telebot.types.ReplyKeyboardRemove()
	bot.send_message(message.chat.id, "⌨💤...", reply_markup=hide_markup)


@bot.message_handler(commands=['help'])
def command_help(message):
	bot.send_message(message.chat.id, "☁ /weather - current weather forecast\n" 
									  "💎 /crypto - current cryptocoins price\n" 
									"⌛️ /world_time - current time in any place\n" 
									"📊 /stocks - current stocks prices\n"
									"📰 /news - latest bbc article")


@bot.message_handler(commands=['weather'])
def command_weather(message):
	weather_sent = bot.send_message(message.chat.id, "🗺 Enter the City or Country\n🔍 In such format:  Toronto  or  japan")
	bot.register_next_step_handler(weather_sent, send_forecast)


def send_forecast(message):
	try:
		get_forecast(message.text)
	except pyowm.exceptions.api_response_error.NotFoundError:
		bot.send_message(message.chat.id, "❌  Wrong place, check mistakes and try again!")
	forecast = get_forecast(message.text)
	bot.send_message(message.chat.id, forecast)


@bot.message_handler(commands=['world_time'])
def command_world_time(message):
	world_time_sent = bot.send_message(message.chat.id, '🗺 Enter the City or Country\n🔍 In such format:  Moscow  or  china')
	bot.register_next_step_handler(world_time_sent, send_time)


def send_time(message):
	try:
		get_time(message.text)
	except IndexError:
		bot.send_message(message.chat.id, "❌ Wrong place, check mistakes and try again")
	current_time = get_time(message.text)
	bot.send_message(message.chat.id, current_time)


@bot.message_handler(commands=['crypto'])
def command_crypto(message):
	coins_markup = types.InlineKeyboardMarkup(row_width=1)
	for key, value in coins.items():
		coins_markup.add(types.InlineKeyboardButton(text=key, callback_data=value))
	bot.send_message(message.chat.id, "🏦 Choose the coin:", reply_markup=coins_markup)


@bot.message_handler(commands=['stocks'])
def command_stocks(message):
	stocks_markup = types.InlineKeyboardMarkup(row_width=1)
	for key, value in stocks.items():
		stocks_markup.add(types.InlineKeyboardButton(text=key, callback_data=value))
	bot.send_message(message.chat.id, "📃 Choose the company:", reply_markup=stocks_markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_crypto_stocks(call):
	if call.message:
		coins_switcher = {
			'BTC': f"💰Bitcoin:  ${btc_price}",
			'LTC': f"💰Litecoin:  ${ltc_price}",
			'ETH': f"💰Ethereum:  ${eth_price}",
			'ETC': f"💰Ethereum Classic:  ${etc_price}",
			'ZEC': f"💰Zcash:  ${zec_price}",
			'DSH': f"💰Dash:  ${dsh_price}",
			'XRP': f"💰Ripple:  ${xrp_price}",
			'XMR': f"💰Monero:  {xmr_price}"
		}
		stocks_switcher = {
			'AMZN': f"📊Amazon:  {amzn_stocks}",
			'GOOG': f"📊Google:  {goog_stocks}",
			'APL': f"📊Apple:  {apl_stocks}",
			'FB': f"📊Facebook:  {fb_stocks}",
			'MSFT': f"📊Microsoft:  {msft_stocks}",
			'TSLA': f"📊Tesla:  {tsla_stocks}",
			'NVDA': f"📊NVIDIA:  {nvda_stocks}",
			'INTL': f"📊Intel:  {intl_stocks}"
		}

		stock_response = stocks_switcher.get(call.data)
		if stock_response:
			bot.send_message(call.message.chat.id, stock_response)
		coin_response = coins_switcher.get(call.data)
		if coin_response:
			bot.send_message(call.message.chat.id, coin_response)


@bot.message_handler(commands=['news'])
def command_news(message):
	bot.send_message(message.chat.id, "🆕 Latest BBC article:\n")
	bot.send_message(message.chat.id, get_article(), parse_mode='HTML')


while True:
	try:
		bot.infinity_polling(True)
	except Exception:
		time.sleep(1)
