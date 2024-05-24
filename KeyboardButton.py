from telebot.types import BotCommand, InlineKeyboardButton, InlineKeyboardMarkup


#------------------------------ Choose the language ----------------
def markup_inline():
	markup = InlineKeyboardMarkup()
	markup.width = 2
	markup.add ( InlineKeyboardButton("🇸🇦 العربيه", callback_data="ar"))
	markup.add (InlineKeyboardButton("🇺🇸 English", callback_data="en"))

	return markup

#----------------------------Help-----------------------------------

def markup_inline_help():
	markup_help = InlineKeyboardMarkup()
	markup_help.add(InlineKeyboardButton("Channel 📢", url="https://t.me/russia_lhub"))

	return markup_help