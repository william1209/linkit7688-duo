import serial
import requests
import time

#ser = serial.Serial('/dev/ttyS0',57600)
ser = None
device_id = "DEVICE ID"

device_key = "DEVICE KEY"
data_channel = "led"
data_channel +=",,"



url = "http://api.mediatek.com/mcs/v2/devices/" + device_id
url += "/datapoints.csv"
url1 = "http://api.mediatek.com/mcs/v2/devices/Do6kc6wx/datachannels/led/datapoints.csv"


def setup():
	global ser
	ser = serial.Serial("/dev/ttyS0", 9600)


def loop():
	r = requests.get(url1,headers = {"deviceKey" : device_key,'Content-Type':'text/csv'})
    turn = str(r.text[18]) 
    ser.write(turn)
    

setup()


print "start"


if __name__ == '__main__':  
	while True :
		loop()
		
