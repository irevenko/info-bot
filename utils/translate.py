from googletrans import Translator

trans = Translator()


def to_ru(words):
	t = trans.translate(words, src='en', dest='ru')
	return t.text


def to_de(words):
	t = trans.translate(words, src='en', dest='de')
	return t.text


def to_pl(words):
	t = trans.translate(words, src='en', dest='pl')
	return t.text


def to_es(words):
	t = trans.translate(words, src='en', dest='es')
	return t.text


def to_ja(words):
	t = trans.translate(words, src='en', dest='ja')
	return t.text


def to_fr(words):
	t = trans.translate(words, src='en', dest='fr')
	return t.text


languages = ["Russian", "German", "Japanese", "Polish", "Spanish", "French"] 