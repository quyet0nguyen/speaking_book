import os
import threading
import sys

command1 = 'python -m rasa run actions'

command2 = 'python -m rasa run --enable-api'

command3 = 'python ./chatbotTelegram.py'

x1 = threading.Thread(target=os.system, args=(command1,))
x1.start()
x2 = threading.Thread(target=os.system, args=(command2,))
x2.start()
x3 = threading.Thread(target=os.system, args=(command3,))
x3.start()