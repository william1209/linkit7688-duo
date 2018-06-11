import serial
import time
import requests

global ser
ser = serial.Serial('/dev/ttyS0',9600)

device_id = "DWSCVjnQ"
device_key = "060QmR5kutfJvp5s"


url = "http://api.mediatek.com/mcs/v2/devices/" + device_id
url += "/datapoints.csv"



def upload(value,length):
        data = data_channel+str(value)
        r = requests.post(url,headers = {"deviceKey" : device_key,'Content-Type':'text/csv'},data=data)
        print r.text
        



print "Start"

while True:
    

    if ser.read()=='a':
        IncommingNum = ser.read()
        temp = str(ser.read(int(IncommingNum)))

        a = 8

        data_channel = "temp,,"
                
        upload(temp,a)

    
    if ser.read()=='b':
                
        IncommingNum = ser.read()
        humi = str(ser.read(int(IncommingNum)))

        b = 8
        data_channel = "humi,,"

        upload(humi,b)

    if ser.read()=='c':
        
        IncommingNum = ser.read()
        hi = str(ser.read(int(IncommingNum)))
        c=8
        data_channel = "hi,,"

        upload(hi,c)

    if ser.read()=='d':
        IncommingNum = ser.read()
        gas = str(ser.read(int(IncommingNum)))
        d=8
        data_channel = "gas,,"

        upload(gas,d)

    time.sleep(30)





