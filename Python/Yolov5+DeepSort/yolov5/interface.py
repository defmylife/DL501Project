import threading
# more info :   https://docs.python.org/3/library/threading.html
#           :   http://marcuscode.com/lang/python/threads

from detect import main

yoloScript = threading.Thread(target=main)
# testScript = threading.Thread(target=)

yoloScript.start()
# testScript.start()