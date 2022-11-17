import os
import sys
import time

import random
import dircache
import subprocess
dir = 'songs/anger/'
filename = random.choice(dircache.listdir(dir))
print "filename",filename
path = os.path.join(dir, filename)
print "path",path
subprocess.Popen(['mpg123', '-q', path]).wait()

