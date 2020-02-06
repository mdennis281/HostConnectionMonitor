from app import Monitor

connectionMonitor = Monitor('8.8.8.8')

'''

other examples:
connectionMonitor = Monitor(
	'google.com',
	output='out.log',
	testLength=1500  #seconds
)

connectionMonitor = Monitor(
	'10.0.0.100',
	output='outServer.log',
	pingFrequency=2,  #seconds
	maxFailCount=0 #number of pings before classified as outage
)


'''

connectionMonitor.start() 
