import syslog
import datetime

ct = datetime.datetime.now()
syslog.syslog("We've written to the syslog file, Mr. Coolman. The time is:" +str(ct))
