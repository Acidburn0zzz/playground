
from comar.service import *

serviceType = "local"
serviceConf = "cmocka"
serviceDefault = "conditional"

serviceDesc = _({"en": "Cmocka",
                 "tr": "Cmocka"})

@synchronized
def start():
    startService(command="/usr/sbin/cmocka",
                 args = config.get("args", "destroy"),
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/cmocka",
                donotify=True)

def ready():
    import os
    status = is_on()
    if status == "on" or (status == "conditional" and os.path.exists("/sys/coffee/ready")):
        start()

def status():
    return checkDaemon("/var/run/cmocka.pid")

