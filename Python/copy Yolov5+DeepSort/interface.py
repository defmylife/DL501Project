import threading
# more info :   https://docs.python.org/3/library/threading.html
#           :   http://marcuscode.com/lang/python/threads

from track import runTrack

yoloScript = threading.Thread(target=runTrack)
# testScript = threading.Thread(target=)

yoloScript.start()
# testScript.start()