import telebot
import pyowm
import pyowm.exceptions
import time
from telebot import types
from pyowm.exceptions import api_response_error
from secrets import BOT_TOKEN, OWM_TOKEN
from utils import coins, methods

bot = telebot.TeleBot(BOT_TOKEN, threaded=False)
owm = pyowm.OWM(OWM_TOKEN)


@bot.message_handler(commands=['start'])
def command_start(message):
	start_markup = telebot.types.ReplyKeyboardMarkup(True, False)
	start_markup.row('/start', '/help', '/hide_keyboard')
	start_markup.row('/weather', '/cryptocoins')
	bot.send_message(message.chat.id, "🤖 The bot has started!\n⚙ Enter /help to see bot's functions")
	bot.send_message(message.from_user.id, "⌨️ The Keyboard is added!", reply_markup=start_markup)


@bot.message_handler(commands=['hide_keyboard'])
def command_hide_keyboard(message):
	hide_markup = telebot.types.ReplyKeyboardRemove()
	bot.send_message(message.chat.id, "⌨💤...", reply_markup=hide_markup)


@bot.message_handler(commands=['help'])
def command_help(message):
	bot.send_message(message.chat.id, "☁ /weather - Current weather forecast in such format: .Toronto or  .Japan\n" \
									  "💎 /cryptocoins - Current Cryptocurrency price")


@bot.message_handler(commands=['weather'])
def command_weather(message):
	bot.send_message(message.chat.id, "🌞 Enter a City or Country\nIn such format:  .Toronto or  .Japan")


@bot.message_handler(func=lambda msg: msg.text is not None and msg.text.startswith('.') and not msg.text.endswith('.'))
def command_forecast(message):
	words = message.text.split()
	in_text = methods.find_dot(words)
	if in_text == '.':
		pass
	else:
		parsed_msg = message.text.split('.')
	try:
		observation = owm.weather_at_place(str(parsed_msg[1]))
	except pyowm.exceptions.api_response_error.NotFoundError:
		bot.send_message(message.chat.id, "❌  Wrong place, check mistakes and try again!")

	weather = observation.get_weather()
	temperature = weather.get_temperature('celsius')["temp"]
	wind = weather.get_wind()['speed']
	clouds = weather.get_clouds()
	humidity = weather.get_humidity()
	forecast_answer = "🏙 In " + str(
		parsed_msg[1]) + " is currently " + weather.get_detailed_status() + "\n🌡️  " + str(
		temperature) + " °C" + "\n💨  " + str(wind) + " m/s" + "\n🌫️  " + str(clouds) + " %" + "\n💦  " + str(
		humidity) + " %"
	bot.send_message(message.chat.id, forecast_answer)


@bot.message_handler(commands=['cryptocoins'])
def command_cryptocoins(message):
	coins_markup = types.InlineKeyboardMarkup(row_width=2)
	btc = types.InlineKeyboardButton("Bitcoin(BTC)", callback_data='BTC') #TODO make shorter with for loop
	ltc = types.InlineKeyboardButton("Litecoin(LTC)", callback_data='LTC')
	eth = types.InlineKeyboardButton("Ethereum(ETH)", callback_data='ETH')
	etc = types.InlineKeyboardButton("Ethereum Classic(ETC)", callback_data='ETC')
	xmr = types.InlineKeyboardButton("Monero(XMR)", callback_data='XMR')
	dash = types.InlineKeyboardButton("Dash(DASH)", callback_data='DASH')
	zec = types.InlineKeyboardButton("Zcash(ZEC),", callback_data='ZEC')
	xpr = types.InlineKeyboardButton("Ripple(XPR)", callback_data='XPR')
	coins_markup.add(btc, ltc, eth, etc, xmr, dash, zec, xpr)
	bot.send_message(message.chat.id, "🏦Choose a coin:", reply_markup=coins_markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_cryptocoins(call):
	try:
		if call.message:
			switcher = {
				'BTC': f"💰Bitcoin: ${coins.btc_price}",
				'ETH': f"💰Ethereum: ${coins.eth_price}",
				'LTC': f"💰Litecoin: ${coins.ltc_price}",
				'ETC': f"💰Ethereum Classic: ${coins.etc_price}",
				'ZEC': f"💰Zcash: ${coins.zec_price}",
				'XPR': f"💰Ripple: ${coins.xrp_price}",
				'DASH': f"💰Dash: ${coins.dash_price}",
				'XMR': f"💰Monero: {coins.xmr_price[0]}",
			}
			response = switcher.get(call.data)
			if response:
				bot.send_message(call.message.chat.id, response)
	except Exception as e:
		print(repr(e))


while True:
	try:
		bot.infinity_polling(True)
	except Exception:
		time.sleep(1)
