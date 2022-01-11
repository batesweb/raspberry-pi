import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

ledPin = 11
buttonPin = 12
lightOn = False

def handleButton(channel):
    global lightOn
    print(GPIO.input(buttonPin))
    if not GPIO.input(buttonPin):
        print("Button falling.")
        if lightOn:
            print("turn light off")
            GPIO.output(ledPin,GPIO.LOW)
            lightOn = False
        else:
            print("turn light on")
            GPIO.output(ledPin,GPIO.HIGH)
            lightOn = True



GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(ledPin, GPIO.OUT)

GPIO.add_event_detect(buttonPin,GPIO.BOTH,callback=handleButton) # Setup event on pin 10 rising edge

message = input("Press enter to quit\n\n") # Run until someone presses enter


GPIO.cleanup() # Clean up
