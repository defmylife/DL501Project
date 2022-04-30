import subprocess, os, multiprocessing, threading

import testscript1, testscript2
from testscript1 import run1
from testscript2 import run2

# Sequential -----------------------------------------------------------
# os.system("python testscript1.py && testscript2.py")

# Sequential -----------------------------------------------------------
# subprocess.run("python testscript1.py & python testscript2.py", shell=True)

# Sequential -----------------------------------------------------------
# subprocess.run("python testscript1.py", shell=True)
# subprocess.run("python testscript2.py", shell=True)

# (RuntimeError) -------------------------------------------------------
# script1 = multiprocessing.Process(target=run1)
# script2 = multiprocessing.Process(target=run2)
# script1.start()
# script2.start()

# Threading ------------------------------------------------------------
# more info :   https://docs.python.org/3/library/threading.html
#               http://marcuscode.com/lang/python/threads

script1 = threading.Thread(target=run1)
script2 = threading.Thread(target=run2)

script1.start()
script2.start()
