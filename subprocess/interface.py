import subprocess, os, multiprocessing, threading

import testscript1, testscript2
from testscript1 import run1, writeData
from testscript2 import run2, readData

# OS (Sequential) -----------------------------------------------------------
# os.system("python testscript1.py && testscript2.py")

# Subprocessing (Sequential) ------------------------------------------------
# subprocess.run("python testscript1.py & python testscript2.py", shell=True)

# Multiprocessing (RuntimeError) --------------------------------------------
# script1 = multiprocessing.Process(target=run1)
# script2 = multiprocessing.Process(target=run2)
# script1.start()
# script2.start()

# Threading (working separately :D) -----------------------------------------
# more info :   https://docs.python.org/3/library/threading.html
#               http://marcuscode.com/lang/python/threads
#
# (basic counting)
# script1 = threading.Thread(target=run1)
# script2 = threading.Thread(target=run2)
#
# (basic communication using write/read text file with different sample time)
script1 = threading.Thread(target=writeData)
script2 = threading.Thread(target=readData)

script1.start()
script2.start()
