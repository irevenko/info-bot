import telebot
import pyowm
import pyowm.exceptions
import time
from telebot import types
from pyowm.exceptions import api_response_error
from secrets import BOT_TOKEN, OWM_TOKEN  #from config import *
from utils import weather, crypto_coins, world_time

bot = telebot.TeleBot(BOT_TOKEN, threaded=False)
owm = pyowm.OWM(OWM_TOKEN)


@bot.message_handler(commands=['start'])
def command_start(message):
	start_markup = telebot.types.ReplyKeyboardMarkup(True, False)
	start_markup.row('/start', '/help', '/hide_keyboard')
	start_markup.row('/weather', '/crypto_coins', '/world_time')
	bot.send_message(message.chat.id, "🤖 The bot has started!\n⚙ Enter /help to see bot's function's")
	bot.send_message(message.from_user.id, "⌨️ The Keyboard is added!", reply_markup=start_markup)


@bot.message_handler(commands=['hide_keyboard'])
def command_hide_keyboard(message):
	hide_markup = telebot.types.ReplyKeyboardRemove()
	bot.send_message(message.chat.id, "⌨💤...", reply_markup=hide_markup)


@bot.message_handler(commands=['help'])
def command_help(message):
	bot.send_message(message.chat.id, "☁ /weather - Current weather forecast\n" \
									  "💎 /crypto_coins - Current Cryptocurrency price")


@bot.message_handler(commands=['weather'])
def command_weather(message):
	sent = bot.send_message(message.chat.id, "🌞 Enter a City or Country\n🖊 In such format:  Toronto  or  Japan")
	bot.register_next_step_handler(sent, get_forecast)


def get_forecast(message):
	try:
		owm.weather_at_place(message.text)
	except pyowm.exceptions.api_response_error.NotFoundError:
		bot.send_message(message.chat.id, "❌  Wrong place, check mistakes and try again!")
	forecast = weather.get_weather(message.text)
	bot.send_message(message.chat.id, forecast)


@bot.message_handler(commands=['crypto_coins'])
def command_crypto_coins(message):
	coins_markup = types.InlineKeyboardMarkup(row_width=1)
	for key, value in crypto_coins.coins.items():
		coins_markup.add(types.InlineKeyboardButton(text=key, callback_data=value))
	bot.send_message(message.chat.id, "🏦Choose a coin:", reply_markup=coins_markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_crypto_coins(call):
	try:
		if call.message:
			switcher = {
				'BTC': f"💰Bitcoin: ${crypto_coins.btc_price}",
				'LTC': f"💰Litecoin: ${crypto_coins.ltc_price}",
				'ETH': f"💰Ethereum: ${crypto_coins.eth_price}",
				'ETC': f"💰Ethereum Classic: ${crypto_coins.etc_price}",
				'ZEC': f"💰Zcash: ${crypto_coins.zec_price}",
				'DASH': f"💰Dash: ${crypto_coins.dash_price}",
				'XRP': f"💰Ripple: ${crypto_coins.xrp_price}",
				'XMR': f"💰Monero: {crypto_coins.xmr_price[0]}"
			}
			response = switcher.get(call.data)
			if response:
				bot.send_message(call.message.chat.id, response)
	except Exception as e:
		print(repr(e))


@bot.message_handler(commands=['world_time'])
def command_world_time(message):
	sent = bot.send_message(message.chat.id, '🖊 Enter the Country')
	bot.register_next_step_handler(sent, send_time)


def send_time(message):
	try:
		world_time.get_time(message.text)
	except IndexError:
		bot.send_message(message.chat.id, "❌ Mistype or not a country, check mistakes and try again")

	current_time = world_time.get_time(message.text)
	bot.send_message(message.chat.id, current_time)


while True:
	try:
		bot.infinity_polling(True)
	except Exception:
		time.sleep(1)
