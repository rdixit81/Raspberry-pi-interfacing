import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(24, GPIO.OUT)
pwm = GPIO.PWM(24, 50)
pwm.start(0)

while True:
    for i in range(100):
        pwm.ChangeDutyCycle(i)
        time.sleep(0.03)
    for i in range(100, 0, -1):
        pwm.ChangeDutyCycle(i)
        time.sleep(0.03)
