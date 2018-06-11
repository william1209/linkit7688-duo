import serial
import requests
import time

#ser = serial.Serial('/dev/ttyS0',57600)
ser = None
device_id = "D8jkGJUK"

device_key = "tLQ2DVpMGfZTqC3P"
data_channel = "light"
data_channel +=",,"



url = "http://api.mediatek.com/mcs/v2/devices/" + device_id
url += "/datapoints.csv"
url1 = "http://api.mediatek.com/mcs/v2/devices/Dnk8OvM9/datachannels/light/datapoints.csv"


def setup():
        global ser
        ser = serial.Serial("/dev/ttyS0", 9600)

def get():  

		r = requests.get(url1,headers = {"deviceKey" : device_key,'Content-Type':'text/csv'})
		if r.text[20]==0 or 1 :                                                             
        	turn = str(r.text[20])                                                          
        	#print r.text                                                                   
        	ser.write(turn)                                                                 
        	time.sleep(0.5)
        
                                                               
                                                                                        
setup()                                                                                 
                                                                                        
                                                                                        
print "start"                                                                           
                                                                                        
                                                                                        
if __name__ == '__main__':                                                              
	while True :                                                                      
    	get()   


