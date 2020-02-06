from app.libraries.pinger import Pinger
from app.libraries import time as t

class Monitor:
    def __init__(self,host,**kwargs):
        self.host = host
        self.pinger = Pinger(host)

        self.pingFrequency = kwargs.get('pingFrequency',5)
        self.maxFailCount  = kwargs.get('maxFailCount',1)
        self.output        = kwargs.get('output',False)
        self.testLength    = kwargs.get('testLength', 0)

        self.isAlive = True
        self.failCount = 0
        self.endTime = (t.time() + self.testLength) if self.testLength else 0


    def start(self):
        self._output('Monitor Started.')
        self._testConnection()

    def _testConnection(self):
        while self.pinger.ping():
            if not self._isTimeRemain():
                self._output('Monitor finished. End time reached.')
                return
            self._waitInterval()

        self.failCount += 1
        self.isAlive = False

        while self.failCount < self.maxFailCount:
            if self.pinger.ping():
                self._testConnection()
            else:
                self.failCount += 1

            if not self._isTimeRemain():
                self._output('Monitor finished. End time reached.')
                return

        self._waitConnectionRestored()
        self._testConnection()

    def _waitConnectionRestored(self):
        failTime = t.time()
        self._output('Connection to '+self.host+' lost.')
        while not self.pinger.ping():
            self.failCount += 1
            if not self._isTimeRemain():
                self._output('Monitor finished. End time reached.')
                return
            self._waitInterval()
        outageTotal = round((t.time()-failTime)/60,1)
        self._output('Connection Restored. '+str(outageTotal)+' min down.')


    def _isTimeRemain(self):
        if not self.endTime: # if testLength not specified (run forever)
            return True
        if t.time() > self.endTime:
            return False
        else:
            return True

    def _waitInterval(self):
        t.sleep(self.pingFrequency)

    def _output(self,message):
        now = t.strftime('%Y-%m-%d %H:%M:%S', t.localtime())
        message = now+'\t'+message
        if self.output:
            f = open(self.output,'a')
            f.write(message+'\n')
            f.close()
        else:
            print(message)
