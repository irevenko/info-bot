# InfoBot 🤖
An all-round bot made to learn Python <br />
[Telegram link](https://t.me/info2019_bot) or @info2019_bot <br />
Bot is deployed on Heroku, so it might sleep after 30 mins of being inactive but could wake up (big delay around 30 secs) <br />
If you want to access the bot ask me and i'll launch it locally<br />
If bot is not working or you found a bug - please contact me in telegram @irevenko

# This bot is written using ✏️
* [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
* [pyowm](https://github.com/csparpa/pyowm) 
* [coinbase](https://gist.github.com/chris-gong/b24130f5ea0c6c93e3c24bfb4aca27fd)
* [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) + [requests](https://requests.readthedocs.io/en/master/) (for scrapping the Monero coin price & current time scrapping & stocks scrapping & news scrapping) 
* [googletrans](https://pypi.org/project/googletrans/)

# What can this bot do❓
* Display current weather forecast 🌄
* Display current world time at any place ⏲
* Display current crypto coins price 💸
* Display current top companies stocks price 📈
* Display latest BBC news 📰
* Translate from English 🔀

# Screenshots 📸
|   |   |   |
|:---:|:---:|:---:|
|<img src="https://i.imgur.com/6SvV1uH.png" width="275">|<img src="https://i.imgur.com/ncleleT.png" width="275">|<img src="https://i.imgur.com/HohkaKi.png" width="275">|
|Start & Help & Keyboard|Time & Weather|Crypto|
<img src="https://i.imgur.com/yFqudtu.png" width="275">|<img src="https://i.imgur.com/sLCDNrQ.png" width="275">|<img src="https://i.imgur.com/3uLkArO.png" width="275">|
|Stocks|News|Translator

# Quick Start 🚀
``` Register your bot at @BotFather in Telegram and add commands``` <br />
```Get API key at openweathermap.org  ``` <br />

``` git clone https://github.com/irevenko/InfoBot.git``` <br />
```cd InfoBot ``` <br />

```pip install requirements.txt ``` <br />
```OR```<br />
```python -m pip install -r requirements.txt```<br />
``` go to config.py and fill tokens```<br />
```BOT_TOKEN = ' '```<br />
```OWM_TOKEN = ' '```<br />
```Then you can launch the bot```
```py bot.py```

# What I Learned 🧠
* How to work with API's (pyowm)
* How to work with JSON's (coinmarket api)
* How to scrap a site (yahoo finance + google search for time + BBC news  with Beatiful Soup)
* How HTTP/HTTPS works
* Function Decorators 
* Lambda Functions
* Try Except, Dictionaries, imports
* How to deploy on heroku
* Polling and web hooks

# License 📑 
(c) 2020 Ilya Revenko. [MIT License](https://tldrlegal.com/license/mit-license)
