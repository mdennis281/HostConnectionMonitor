from app.libraries import (
    platform,
    subprocess,
    os
)

class Pinger:
    def __init__(self, host):
        self.host = host

    def ping(self):

        # Returns True if self.host responds to a ping request.

        # Option for the number of packets as a function of
        param = '-n' if platform.system().lower()=='windows' else '-c'

        # Building the command. Ex: "ping -c/-n 1 google.com"
        command = ['ping', param, '1', self.host]

        FNULL = open(os.devnull, 'w')

        return subprocess.call(command, stdout=FNULL, stderr=subprocess.STDOUT) == 0
