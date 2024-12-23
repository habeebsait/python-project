import serial
from twilio.rest import Client

# Twilio credentials

auth_token = '03a18259fa48789b4a4d9aae5d54b657'
client = Client( auth_token)

# Set up the serial connection to Arduino (Adjust 'COM3' or '/dev/ttyUSB0' for your system)
arduino = serial.Serial('/dev/tty.usbserial-130', 9600)  # Change 'COM3' to the appropriate port

def send_sms():
    message = client.messages.create(
        body="Alert from Arduino!",
        from_='+14152126930',
        to='+916366699999'
    )
    print(f"SMS sent! Message SID: {message.sid}")

try:
    print("Listening for messages from Arduino...")
    while True:
        if arduino.in_waiting > 0:
            alert = arduino.readline().decode('utf-8').strip()
            if alert == "ALERT":
                print("Alert received from Arduino")
                send_sms()

except KeyboardInterrupt:
    print("Program interrupted.")
finally:
    arduino.close()
