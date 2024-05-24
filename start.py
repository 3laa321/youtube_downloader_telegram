from lib import *


# ------------bot start-----------
@bot.message_handler(commands=['start', 'language'])
def send_start(message):
		bot.reply_to(message, text='hi bro, choose language', reply_markup=markup_inline())

@bot.callback_query_handler(func=lambda message: True)
def callbak_query(call):
		path_us = str(call.from_user.id)

		if call.data == 'ar':
				bot.answer_callback_query(call.id, "اللغة الآن هي العربية ✅.")
				outfile = open('user_data/' + path_us, 'w')
				outfile.write('ar')
				bot.send_message(call.from_user.id, text=ar_help, reply_markup=markup_inline_help())
				bot.delete_message(call.from_user.id, call.message.message_id)

		elif call.data == 'en':
				bot.answer_callback_query(call.id, "The language now is English ✅.")
				outfile = open('user_data/' + path_us, 'w')
				outfile.write('en')
				bot.send_message(call.from_user.id, text=en_help, reply_markup=markup_inline_help())
				bot.delete_message(call.from_user.id, call.message.message_id)
