import serial
from firebase import Firebase
import pyrebase

ser = serial.Serial('/dev/ttyACM1', 9600, 8, 'N', 1, timeout=5)

while True:
    #print(ser.readline())
    temp = float(ser.readline())
    hum = float(ser.readline())
    moisture = int(ser.readline())
    light = int(ser.readline())
    dict = {'temp': temp, 'humidity': hum, 'moisture': moisture, 'light':light}
    print(dict)


#ser = serial.Serial('/dev/ttyACM1', 9600, 8, 'N', 1, timeout=5)
ser = serial.Serial('/dev/ttyACM1', 9600)

#with serial.Serial('/dev/ttyACM1', 19200, timeout=1) as ser:
#ser.write(str.encode('D'))

config = {
  "apiKey": "Xi8aNtSu1YimWwyJHwo36kKGWSSI1cJaewHKxc63",
  "authDomain": "smart-watering-system-12266.firebase.com",
  "databaseURL": "https://smart-watering-system-12266-default-rtdb.europe-west1.firebasedatabase.app/",
  "storageBucket": "smart-watering-system-12266"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

#while True:
    #print(ser.readline())
temp = float(ser.readline())
hum = float(ser.readline())
moisture = int(ser.readline())
light = int(ser.readline())
data = {'temp': temp, 'humidity': hum, 'moisture': moisture, 'light':light}
print(data)
    

firebase = Firebase(config)
    
# Get a reference to the database service
db = firebase.database()
db.child("SensorData").child("soil sensor").set(data)
#db.child("SensorData").child("SensorName")
#data = {"name": "Joe Tilsed"}
#db.child("users").push(data)

statusVal = db.child("SensorData").child("status").get()
status = statusVal.val()
ser.write(str.encode(status))  
