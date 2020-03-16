import telebot
import pyowm
import pyowm.exceptions
import time
from telebot import types
from pyowm.exceptions import api_response_error
from secrets import BOT_TOKEN, OWM_TOKEN  #from config import *
from utils.weather import get_current_forecast
from utils.world_time import get_current_time
from utils.crypto_coins import *

bot = telebot.TeleBot(BOT_TOKEN, threaded=False)
owm = pyowm.OWM(OWM_TOKEN)


@bot.message_handler(commands=['start'])
def command_start(message):
	start_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
	start_markup.row('/start', '/help', '/hide')
	start_markup.row('/weather', '/crypto', '/world_time')
	bot.send_message(message.chat.id, "🤖 The bot has started!\n⚙ Enter /help to see bot's function's")
	bot.send_message(message.from_user.id, "⌨️ The Keyboard is added!\n⌨️ /hide To remove kb ", reply_markup=start_markup)


@bot.message_handler(commands=['hide'])
def command_hide(message):
	hide_markup = telebot.types.ReplyKeyboardRemove()
	bot.send_message(message.chat.id, "⌨💤...", reply_markup=hide_markup)


@bot.message_handler(commands=['help'])
def command_help(message):
	bot.send_message(message.chat.id, "☁ /weather - Current weather forecast\n" \
									  "💎 /crypto - Current Cryptocurrency price\n" \
									"⌛️ /world_time - Current time in any Country")


@bot.message_handler(commands=['weather'])
def command_weather(message):
	weather_sent = bot.send_message(message.chat.id, "🌞 Enter the City or Country\n🖊 In such format:  Toronto  or  japan")
	bot.register_next_step_handler(weather_sent, send_forecast)


def send_forecast(message):
	try:
		get_current_forecast(message.text)
	except pyowm.exceptions.api_response_error.NotFoundError:
		bot.send_message(message.chat.id, "❌  Wrong place, check mistakes and try again!")

	forecast = get_current_forecast(message.text)
	bot.send_message(message.chat.id, forecast)


@bot.message_handler(commands=['world_time'])
def command_world_time(message):
	world_time_sent = bot.send_message(message.chat.id, '🖊 Enter the Country\n🖊In such format:  Spain or china')
	bot.register_next_step_handler(world_time_sent, send_time)


def send_time(message):
	try:
		get_current_time(message.text)
	except IndexError:
		bot.send_message(message.chat.id, "❌ Wrong place, check mistakes and try again")

	current_time = get_current_time(message.text)
	bot.send_message(message.chat.id, current_time)


@bot.message_handler(commands=['crypto'])
def command_crypto(message):
	coins_markup = types.InlineKeyboardMarkup(row_width=1)
	for key, value in coins.items():
		coins_markup.add(types.InlineKeyboardButton(text=key, callback_data=value))
	bot.send_message(message.chat.id, "🏦 Choose a coin:", reply_markup=coins_markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_crypto(call):
	if call.message:
		switcher = {
			'BTC': f"💰Bitcoin: ${btc_price}",
			'LTC': f"💰Litecoin: ${ltc_price}",
			'ETH': f"💰Ethereum: ${eth_price}",
			'ETC': f"💰Ethereum Classic: ${etc_price}",
			'ZEC': f"💰Zcash: ${zec_price}",
			'DASH': f"💰Dash: ${dash_price}",
			'XRP': f"💰Ripple: ${xrp_price}",
			'XMR': f"💰Monero: {xmr_price[0]}"
		}
		coin_response = switcher.get(call.data)
		bot.send_message(call.message.chat.id, coin_response)


while True:
	try:
		bot.infinity_polling(True)
	except Exception:
		time.sleep(1)
