import threading

from detect import main

yoloScript = threading.Thread(target=main)
# testScript = threading.Thread(target=)

yoloScript.start()
# testScript.start()