# HostConnectionMonitor
 A solution to log/monitor connection to the internet/a host.
 
 
 ## Usage
 ```python
 connectionMonitor = Monitor('8.8.8.8')
 connectionMonitor.start()
 ```
 The above will ping 8.8.8.8 indefinitely and report any connection outages
  
## Optional Paramaters
**output='FILE_PATH'** 
  * Variable Type: String
  * Default: None (print to console)
  
**pingFrequency=SECONDS**
  * Description: Time to wait between pings
  * Variable Type: int
  * Default: 5
  * Unit: Seconds
  
**maxFailCount=COUNT**
  * Description: Number of failed pings before classified as an outage
  * Variable Type: int
  * Default: 1
 
**testLength=SECONDS**
  * Description: The number of seconds that the test will run
  * Variable Type: int
  * Default: None (indefinitely)
  * Unit: Seconds

## Examples

```python
connectionMonitor = Monitor(
	'google.com',
	output='out.log',
	testLength=1500
)
connectionMonitor.start() 
```

```python
connectionMonitor = Monitor(
	'10.0.0.100',
	output='outServer.log',
	pingFrequency=2, 
	maxFailCount=0
)
connectionMonitor.start() 
```
