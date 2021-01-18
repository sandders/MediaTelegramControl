from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup
from pyautogui import press


def get_token():
    with open('telegram_bot_token.txt') as file:
        return file.readline()


try:
    bot = TeleBot(get_token())
except FileNotFoundError:
    with open('telegram_bot_token.txt', 'w'):
        print('''
        telegram_bot_token.txt was created. Put your Telegram Bot Token there and try again.
        Use @BotFather to create your own bot and obtain token.\n\n''')
    input('Press any button to exit.')
    exit()


def keymap():
    keyboard = ReplyKeyboardMarkup()
    keyboard.row('⏮', '⏸▶', '⏭')
    keyboard.row('🔽', '🔼')
    return keyboard


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Ready', reply_markup=keymap())


@bot.message_handler(content_types=['text'])
def main_handler(message):
    if message.text == '⏸▶':
        press('playpause')
        bot.send_message(message.chat.id, f'Command {message.text} has been executed', reply_markup=keymap())
    elif message.text == '⏮':
        press('prevtrack')
        bot.send_message(message.chat.id, f'Command {message.text} has been executed', reply_markup=keymap())
    elif message.text == '⏭':
        press('nexttrack')
        bot.send_message(message.chat.id, f'Command {message.text} has been executed', reply_markup=keymap())
    elif message.text == '🔽':
        press('volumedown')
        bot.send_message(message.chat.id, f'Command {message.text} has been executed', reply_markup=keymap())
    elif message.text == '🔼':
        press('volumeup')
        bot.send_message(message.chat.id, f'Command {message.text} has been executed', reply_markup=keymap())
    else:
        bot.send_message(message.chat.id, 'Use buttons provided below', reply_markup=keymap())


if __name__ == '__main__':
    try:
        print('''
        Server running.
        How to use:
        1) Play content on PC. you can use Windows Media Player, YTMusic, YouTube, VLC, Vimeo, Spotify and other apps 
        and sites that support button controls;
        2) Leave this app running.
    
        P.S. Might not work after long pause.
        ''')
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        input()
