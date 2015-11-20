import time
import sys
import signal
import alsaseq
import logging

from listener import Listener
from scheduler import Scheduler

import sync
import com
import command

# logging.basicConfig(filename='debug.log',level=logging.DEBUG)

sock = com.connect('20:14:12:17:01:67')
if not sock:
    logging.error('connection to laser gun failed')
    exit(-1)

alsaseq.client( 'LaserGun', 0, 1, False )

listener = Listener(sock)
scheduler = Scheduler()

scheduler.start()
listener.start()

def terminate():
    print 'Interrupted'
    com.stopGun(sock)
    sync.qLock.acquire()
    sync.queue.put( (command.TRG_OFF, None) )
    sync.qLock.release()
    sync.terminate.set()     
    sync.queueEvent.set()
    scheduler.join()
    listener.join()
    sys.exit(0)

time.sleep(1)

com.stopGun(sock)
if not com.resetGun(sock):
    terminate()
if not com.calibrateGun(sock):
    terminate()
if not com.startGun(sock):
    terminate()

try:
    while True:
        time.sleep(1)
except:
    terminate()



