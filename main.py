from lib import *
from start import *
from download import *


#-----------------------------------


# ------------bot running-----------
print(" your bot is running ")

bot.infinity_polling()
bot.polling(none_stop=True)