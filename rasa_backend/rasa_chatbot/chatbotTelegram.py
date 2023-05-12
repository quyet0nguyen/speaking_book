import time,datetime,pytz
import telepot
import requests
import json
import ssl
from threading import Thread
import threading
import os
from pprint import pprint
import urllib3
import telepot.api
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import threading

try:
    import Queue as queue
except ImportError:
    import queue

mess_queue = queue.Queue(maxsize=1000)

# myproxy_url = "http://10.57.10.34:3128"


# telepot.api._pools = {'default': urllib3.ProxyManager(proxy_url=myproxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),}

# telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=myproxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

TOKEN = '6152261354:AAESuEuqqAPWdYbw0VXFl4gO7mAAgXJduQ4' 

bot = telepot.Bot(TOKEN)

title = []
queue_msg = []
total_thread = 0

def call_rasa_api(sender,message):
    url = "http://0.0.0.0:5005/webhooks/rest/webhook"
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "sender": sender,
        "message": message
    }    
    jsonData = json.dumps(data)
    urllib3.disable_warnings()
    print("starting send request to rasa")
    response = requests.post(url,headers= headers, data=jsonData, verify=ssl.CERT_NONE) #tao request ban len api rasa
    print(response)
    returnButtons = []
    if(response.json()==[]):
        return 'Bot khĂ´ng cĂ³ cĂ¢u tráº£ lá»i cho cĂ¢u há»i nĂ y.'
    else:
        result = ''
        for i in range(len(response.json())):
            if('buttons' in response.json()[i]):
                result = result + response.json()[i]['text']
                buttonNum = 0
                listButton = response.json()[i].get('buttons')
                for button in listButton:
                    buttonNum+=1
                    returnButtons.append(button['title'])
                    title.append(button['title'])
                    a = returnButtons.pop()
                return result
            else:
                for data in response.json()[i]:
                    if('text' in data):
                        result = result + response.json()[i][data].replace('<br>', '\n') + '\n'
                    else:
                        pass
        return result.rstrip('\n')

def handle_msg(msg):
    command = msg['text']
    if command.startswith('/bot'):
        command = command.split('/bot ')[1]
    command = command.replace('@tcld_bot','')
    return command

def convert(timestamp):
    timestamp = datetime.datetime.fromtimestamp(timestamp)
    return(timestamp.strftime('%d-%m-%Y %H:%M:%S'))


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    receive_time = datetime.datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).strftime('%d-%m-%Y %H:%M:%S')
    print(content_type, chat_type, chat_id)
    global message_with_inline_keyboard    #bien thay doi khi click vao button
    message_id = msg['message_id']          # message id
    from_id = msg['from']['id']             # group id
    send_time = convert(msg['date'])        # send time

    phoneNumber = ReplyKeyboardMarkup(keyboard=[
                     [KeyboardButton(text='Share phone number', request_contact=True),
                      KeyboardButton(text='Location', request_location=True)
                     ]
                 ], one_time_keyboard=True, resize_keyboard=True)

    if (content_type == 'text'):
        command = handle_msg(msg)  #xu ly command xem lieu co bat dau bang /bot hay co @bot o phia sau
        if(chat_type == 'group' or chat_type == 'supergroup'):
            if (command[0] == '/' and command != '/help'):
                msg = "Bot tcld hiá»‡n khĂ´ng há»— trá»£ tra cá»©u trong group"
                bot.sendMessage(chat_id,"<b>" + msg + "</b>", parse_mode='HTML')
            elif('reply_to_message' in msg):
                return
            else:
                responseUser = call_rasa_api(chat_id, command)
                buttons = []
                for each in title:
                    buttons.append(
                    [InlineKeyboardButton(text = each, callback_data = each)]
                    )
                button_list = InlineKeyboardMarkup(inline_keyboard=buttons)
                message_with_inline_keyboard = bot.sendMessage(chat_id, "<b>" + responseUser + "</b>", reply_markup=button_list, reply_to_message_id = message_id, parse_mode='HTML')
                title.clear()
        else:
            if (command[0] == '/' and command != '/help'):
                msg = "Bot tcld hiá»‡n khĂ´ng há»— trá»£ tra cá»©u lá»‡nh"
                bot.sendMessage(chat_id,"<b>" + msg + "</b>", parse_mode='HTML')
            else:
                responseUser = call_rasa_api(chat_id, command)
                buttons = []   
                for each in title:
                    buttons.append(
                    [InlineKeyboardButton(text = each, callback_data = each)]
                    )
                button_list = InlineKeyboardMarkup(inline_keyboard=buttons)

                message_with_inline_keyboard = bot.sendMessage(chat_id,"<b>" + responseUser + "</b>", reply_markup=button_list, parse_mode='HTML')
                title.clear()

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)

    chat_id = msg['message']['chat']['id']
    print(chat_id)

    chat_type = msg['message']['chat']['type']

    # bot.answerCallbackQuery(query_id, text='Got it: {}'.format(query_data))
    global message_with_inline_keyboard
    msg_idf = telepot.message_identifier(message_with_inline_keyboard)
    if(query_data[0] == '/'):
        # response = command_api(from_id, query_data)
        bot.editMessageText(msg_idf, '<b>Báº¡n chá»n: {}</b>'.format(query_data), parse_mode='HTML')
        msg = "Bot tcld hiá»‡n khĂ´ng há»— trá»£ xá»­ lĂ½ lá»‡nh"
        bot.sendMessage(chat_id,"<b>" + msg + "</b>", parse_mode='HTML')
    else:
        response = call_rasa_api(from_id, query_data)
        bot.editMessageText(msg_idf, '<b>Báº¡n chá»n: {}</b>'.format(query_data), parse_mode='HTML')
        bot.sendMessage(from_id, '<b>' + response + '</b>', parse_mode='HTML')

def put_message(msg):
    print(f'message: {msg}')
    mess_queue.put(msg)

def listen_queue():
    while True:
        if (mess_queue.empty()):
            time.sleep(0.2)
        else:
            try:
                msg = mess_queue.get()
                handle(msg)
            except:
                time.sleep(0.2)

def thread_listen_queue():
    list_thread = [None] * 5
    for t in list_thread:
        t = threading.Thread(target=listen_queue)
        t.start()

def thread_loop():
    MessageLoop(bot, {'chat': put_message,
                'callback_query': on_callback_query}).run_as_thread()

    while True:
        time.sleep(0.2)
        
if __name__ == '__main__':

    queue_thread = threading.Thread(target=thread_listen_queue)
    queue_thread.start()
    queue_thread.join()
    print('running queue...')

    msg_thread = threading.Thread(target=thread_loop)
    msg_thread.start()
    msg_thread.join()
    print ('Listening ...')
    # Keep the program running.
    while 1:
        time.sleep(0.5)